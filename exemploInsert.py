from operacoesbd import *

conexao = abrirBancoDados('localhost', 'root', 'thay2313080121', 'minhaouvidoriateste1')

tipo = int(input('Digite o tipo da nova manifestação: '))
titulo = input('Digite o título da nova manifestação: ')
descricao = input('Digite a descrição da nova manifestação: ')
autor = input('Digite o autor da nova manifestação: ')

inserirSql = 'insert into manifestacao (tipo,titulo,descricao,autor) values (%s,%s,%s,%s)'
valores = (tipo, titulo, descricao, autor)

insertNoBancoDados(conexao,inserirSql,valores)

encerrarBancoDados(conexao)