import requests
from bs4 import BeautifulSoup
import pymysql

#---- GET DATA FROM AMAZON WITHLIST BOOKS AND PUT INTO MYSQL DATABASE ----

# get the html code from the page
page = requests.get('https://www.amazon.com.br/hz/wishlist/ls/1QPZQPIXMAFL?ref_=wl_share')

# find specific data with selected tags
soup = BeautifulSoup(page.text, 'html.parser')
bookname = soup.find_all('h3')
bookauthor = soup.find_all("span", class_='a-size-small a-color-tertiary')
photos = soup.find_all('img')
price1 = soup.find_all('span', class_=('a-price-whole','a-size-base a-color-price awl-item-availability-msg'))
price2 = soup.find_all('span', class_=('a-price-fraction', 'a-size-base a-color-price awl-item-availability-msg'))
dbbooknamelist = list()
booknamelist = list()

try:
    # make connection to database
    conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='dados',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    # put the db data into an list
    with conexao.cursor() as c:
        c.execute('SELECT nome FROM livros')
        result = c.fetchall()
        for x in result:
            dbbooknamelist.append(x['nome'])

    for x in range(len(bookauthor)):

        # set the variables with the content of the book
        name = bookname[x].text
        author = bookauthor[x].text

        if price1[x].text == 'Não disponível.':
            price = 'NA'
        else:
            price = f'R${price1[x].text}{price2[x].text}'.replace(',', '.')

        #add all current withlist book names to an list
        booknamelist.append(name)

        # acess the html of the image and make a newfile.jpg with the name of the book
        urlimg = photos[x+8]['src']
        page = requests.get(urlimg)
        with open(f'images/{bookname[x].text[:10]}.jpg', 'wb') as f:
            f.write(page.content)

        with conexao.cursor() as c:
            # verify if the data does not already exist and if exist update the price
            if name in dbbooknamelist:
                c.execute(f"UPDATE livros set preco='{price}' WHERE nome='{name}'")
                conexao.commit()
                continue

            #insert data into database
            sql = 'INSERT INTO livros (nome, autor, preco, imagem) VALUES (%s, %s, %s, %s)'
            c.execute(sql, (name, author, price, f'LOAD_FILE("images/{name[:10]}.jpg")'))
            conexao.commit()

    #delete items that does not exist anymore in the withlist but are in db
    with conexao.cursor() as c:
        for x in dbbooknamelist:
            if x not in booknamelist:
                c.execute(f"DELETE FROM livros WHERE nome = '{x}' LIMIT 1")
                conexao.commit()

    conexao.close()

except IndexError as l:
     print(f'ERROR: {l} - {type(l)}')
except Exception as e:
    print(f'ERROR: {e} - {type(e)}')
