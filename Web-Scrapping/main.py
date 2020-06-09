import requests
from bs4 import BeautifulSoup
import pymysql

# get the html code from the page
page = requests.get('https://www.amazon.com.br/hz/wishlist/ls/1QPZQPIXMAFL?ref_=wl_share')

# find specific data with selected tags
soup = BeautifulSoup(page.text, 'html.parser')
bookname = soup.find_all('h3')
bookauthor = soup.find_all("span", class_='a-size-small a-color-tertiary')
photos = soup.find_all('img')
price1 = soup.find_all('span', class_='a-price-whole')
price2 = soup.find_all('span', class_='a-price-fraction')

try:
    # make connection to database
    conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='dados',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

    for x in range(len(photos)):
        if x < 8:
            continue

        i = x - 8

        # set the variables with the content of the book
        name = bookname[i].text
        author = bookauthor[i].text
        price = f'{price1[i].text}{price2[i].text}'.replace(',', '.')

        # acess the html of the image and make a newfile with the name of the book
        urlimg = photos[x]['src']
        page = requests.get(urlimg)
        with open(f'images/{bookname[i].text[:10]}.jpg', 'wb') as f:
            f.write(page.content)

        #insert all the date into database
        with conexao.cursor() as c:
            sql = 'INSERT INTO livros (nome, autor, preco, imagem) VALUES (%s, %s, %s, %s)'
            c.execute(sql, (name, author, price, f'LOAD_FILE("images/{name[:10]}.jpg")'))
            conexao.commit()

    conexao.close()
except IndexError:
    pass
except Exception as e:
    print(e, type(e))
