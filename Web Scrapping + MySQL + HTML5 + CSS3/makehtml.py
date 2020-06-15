import pymysql

conexao = pymysql.connect(
    host='127.0.0.1',
    user='root',
    password='password',
    db='dados',
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor)

with conexao.cursor() as c:
    c.execute('SELECT nome, autor, preco FROM livros')
    result = c.fetchall()

with open('index.html', 'w+') as d:
    d.write("""<!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="utf-8/">
        <title>Amazon Withlist</title>
        <link rel="stylesheet" href="css/style.css" />
    </head>
    <body>
    <header>
    <hgroup>
    <img id="amazonlogo" src="site-resources/amazon.png" width = "150" height="50"">
    <h1 id="title"">WITHLIST </h1>
    </hgroup>
    </header>
    <div id="interface">
    <h1 id="xesque"><a href="https://www.amazon.com.br/hz/wishlist/ls/1QPZQPIXMAFL?ref_=wl_share " target="_blank">My Amazon Withlist</a></h1>
    <h4>Last time updated by Vitu was in 15/06/2020</h4>
    <ul id="books" style="list-style-type:none">""")
    for x in result:
        d.write(f"""
        <li id="img"><img src="images/{x['nome'][:10]}.jpg"></img></li>
        <li id="data"><ul>
        <li><h1>{x['nome']}</h1></li>
        <li><h2>{x['autor']}</h2></li>
        <li><h3>{x['preco']}</h3></li>
        </ul>
        </li>
        <div id= "line"></div>
        """)
    d.write("""
    </ul>
    </div>
    <footer id="rodape">
    <div id="rodape" style="text-align: center;">Copyright 2020 &copy;&trade; - by Vitu Gabriel</div>
    </footer>
    </body>
    </html>
    """)


