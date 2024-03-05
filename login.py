import psycopg
print(psycopg)
class Usuario:
    def __init__(self, login, senha):
        self.login = login
        self.senha = senha

#verificando se o usuario recebido existe na base 
def existe(usuario):
    #abrir uma conexao com o PostgreSQL
    #obter uma abstracao do tipo "cursor"
    #executar um comando sql
    #verificar um resultado
    #devolver True ou False
    with psycopg.connect(
        host="localhost",
        port=5432,
        dbname="20241_fatec_ipi_pbdi_login_python",
        user="postgres",
        password="123456"
    ) as conexao :
    #obter um cursor 
        with conexao.cursor() as cursor:
            cursor.execute('select * from tb_usuario where login=%s and senha=%s',
            (usuario.login, usuario.senha)
             )
            result = cursor.fetchone()
         #return True if result != None else False
            return result != None 
     
def teste():
   print(existe(Usuario('admin', 'admin')))

teste()
         
