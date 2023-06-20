from operacoesbd import *

conexao = abrirBancoDados('localhost', 'root', 'thay2313080121', 'minhaouvidoriateste1')

ListagemConsulta = 'select * from manifestacao'

manifestacao = listarBancoDados(conexao, ListagemConsulta)

for m in manifestacao:
    print('Código:', m[0], '/', 'Título:', m[2], '/', 'Autor:', m[4])

encerrarBancoDados(conexao)