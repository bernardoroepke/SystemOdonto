from datetime import datetime
import mysql.connector
import os

#Dados de conexão com banco de dados
db_host = os.environ.get('DBHOST')
db_user = os.environ.get('DBUSER')
db_password = os.environ.get('DBPASSWORD')
db_database = os.environ.get('DBDATABASE')

#Motivo: Verificar se a resposta da requisição falhou ou não
#Paramns: args(obj, obrigatorio)
#Return: status, msg, erro(obj)
def verifica_falha_requisicao(args):
    if args['status'] == 0:
        return {
            'status': args['status'],
            'msg': args['msg'],
            'erro': args['erro']
        }
    pass

#Motivo: Montar o sql dinamicamente para retornar registro
#Paramns: args(obj, obrigatório) | tabela(string, obrigatório)
#Return: status e data ou erro(obj)
def sql_select_tabela_unica(args, tabela):
    try:
        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        #Verificação se há campos dentro de args
        if all(value is None for value in args.values()):
            sql = f"SELECT * FROM {tabela}"
        else:
            sql = f"SELECT * FROM {tabela} WHERE "

            #Validação dos campos recebidos
            for chave, valor in args.items():
                if valor is not None:
                    sql += f"{chave} = '{valor}' AND "

            sql = sql[:-5]

        cursor = conexao.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conexao.close()

        return {
            'status': 1,
            'data': data
        }
            
    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': f'Falha ao retornar {tabela}',
            'erro': err.msg
        }

#Motivo: Montar o sql dinamicamente para cadastrar registro
#Paramns: args(obj, obrigatório) | tabela(string, obrigatório)
#Return: status, data ou erro(obj)
def sql_insert_tabela_unica(args, tabela):
    try:
        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        sql = f"INSERT INTO {tabela} ("

        #Validação dos campos recebidos
        for chave, valor in args.items():
            if valor is not None and valor != '':
                sql += f"{chave}, "

        sql = sql[:-2]
        sql += ") VALUES ("

        #Validação dos campos recebidos
        for chave, valor in args.items():
            if valor is not None and valor != '':
                sql += f"'{valor}', "

        sql = sql[:-2]
        sql += ");"

        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()

        return {
            'status': 1,
            'msg': f'{tabela} criado com sucesso.'
        }
    
    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': f'Falha ao cadastrar {tabela}',
            'erro': err.msg
        }

#Motivo: Montar o sql dinamicamente para atualizar registro
#Paramns: args(obj, obrigatório) | tabela(string, obrigatório) | cod(string, obrigatório)
#Return: status, data ou erro(obj)
def sql_update_tabela_unica(args, tabela):
    try:
        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        sql = f"UPDATE {tabela} SET "

        #Validação dos campos recebidos
        for chave, valor in args.items():
            if valor is not None:
                sql += f"{chave} = '{valor}', "

        sql = sql[:-2]

        #Finalizando sql com o cod da tabela correspondente
        data = []
        for chave, valor in args.items():
            sql += f" WHERE {chave} = {valor}"
            data.append(chave)
            data.append(valor)
            break

        
        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()

        return {
            'status': 1,
            'msg': f'{data[0]} = {data[1]} foi editado com sucesso.'
        }
        
    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': f'Falha ao editar {tabela}',
            'erro': err.msg,
            'código do erro': err.errno
        }

#Motivo: Montar o sql dinamicamente para deletar registro
#Paramns: args(obj, obrigatório) | tabela(string, obrigatório) | cod(string, obrigatório)
#Return: status, data ou erro(obj)
def sql_delete_tabela_unica(args, tabela):
    try:
        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        #Adicionando no sql o cod da tabela correspondente
        data = []
        for chave, valor in args.items():        
            sql = f"DELETE FROM {tabela} WHERE {chave} = {valor}"
            data.append(chave)
            data.append(valor)
            break

        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()

        return {
            'status': 1,
            'msg': f'{data[0]} = {data[1]} foi deletado com sucesso.'
        }
    
    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': f'Falha ao deletar {tabela}',
            'erro': err.msg
        }
        
def sql_delete_tabela_unica_2_parametros(args, tabela):
    try:
        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        #Adicionando no sql o cod da tabela correspondente
        contador = 0
        for chave, valor in args.items():
            if contador == 0:        
                sql = f"DELETE FROM {tabela} WHERE {chave} = {valor} AND "
                contador += 1
            else:
                sql += f"{chave} = {valor}"
                break

        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()

        return {
            'status': 1,
            'msg': f'{tabela} foi deletado com sucesso.'
        }

    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': f'Falha ao deletar {tabela}',
            'erro': err.msg
        }

#Motivo: Gera login e senha de usuário com base no nome, cpf e data de nascimento
#Paramns: args(obj)
#Return: login e senha(obj)
def gerar_login(args):
    try:
        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )
        #Verificação do campo nome e cpf
        if args['nome'] == '' or args['cpf'] == '' or args['data_nascimento'] == '':
            return {
                'status': 0,
                'msg': 'Nome, data de nascimento e CPF são obrigatórios.'
            }
        
        #Tratativa para gerar login com base no nome e cpf
        primeiro_nome = args['nome'].split()[0].lower()
        tres_ultimos_cpf = args['cpf'][-3:]
        login = primeiro_nome + tres_ultimos_cpf
        
        #Tratativa para gerar senha com base na data de nascimento
        data_nascimento_obj = datetime.strptime(args['data_nascimento'], "%Y-%m-%d")
        senha = data_nascimento_obj.strftime("%d%m%Y")

        sql = f"INSERT INTO usuarios (login, senha) VALUES ('{login}', '{senha}')"

        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()

        cod_usuario = cursor.lastrowid
        
        cursor.close()
        conexao.close()

        return {
            'status': 1,
            'cod_usuario': cod_usuario
        }
    
    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': 'Falha ao gerar login',
            'erro': err.msg
        }

#Motivo: Executa sql select bruto
#Paramns: sql(string)
#Return: status, data ou erro(obj)
def sql_select(sql):
    try:

        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        cursor = conexao.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        cursor.close()
        conexao.close()

        return {
            'status': 1,
            'data': data
        }

    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': f'Falha ao executar sql',
            'erro': err.msg
        }

#Motivo: Executa qualquer sql bruto que não seja select
#Paramns: sql(string)
#Return: status, data ou erro(obj)
def sql_menos_select(sql):
    try:

        #Conexão com o banco            
        conexao = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_database
        )

        cursor = conexao.cursor()
        cursor.execute(sql)
        conexao.commit()
        cursor.close()
        conexao.close()

    except mysql.connector.Error as err:
        conexao.rollback()
        cursor.close()
        conexao.close()

        return {
            'status': 0,
            'msg': f'Falha ao executar sql',
            'erro': err.msg
        }