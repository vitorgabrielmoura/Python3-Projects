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
    <img id="amazonlogo" src="site-resources/amazon.png" width = "150" height="50"">
    <h1 id="title"">WITHLIST </h1>
    </header>
    <div id="interface">""")
    for x in result:
        d.write(f"""
        <h1>{x['nome']}</h1>
        <h2 style="">{x['autor']}</h2>
        <h3>{x['preco']}</h3>
        """)
    d.write("""
    </div>
    </body>
    </html>
    """)


