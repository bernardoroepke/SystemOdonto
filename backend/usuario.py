from flask_restful import Resource, reqparse
import functions
import mysql.connector
import os

#Dados de conexão com banco de dados
db_host = os.environ.get('DBHOST')
db_user = os.environ.get('DBUSER')
db_password = os.environ.get('DBPASSWORD')
db_database = os.environ.get('DBDATABASE')

from flask_restful import Resource, reqparse
import functions

class Usuario(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('login', type=str, required=False)
        parser.add_argument('senha', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'usuarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_usuario': item[0],
                'login': item[1],
                'senha': item[2],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):
        return {
            'status': 0,
            'msg': 'Método POST não aceito.'
        },

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=True, help="Campo 'cod_usuario' é obrigatório.")
        parser.add_argument('login', type=str, required=False)
        parser.add_argument('senha', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'usuarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=True, help="Campo 'cod_usuario' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'usuarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201


class Telefone(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_email', type=int, required=False)
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('descricao', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_email': item[0],
                'cod_usuario': item[1],
                'descricao': item[2],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=True, help="Campo 'cod_usuario' é obrigatório.")
        parser.add_argument('descricao', type=str, required=True, help="Campo 'descricao' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_insert_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('descricao', type=str, required=True, help="Campo 'descricao' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_email', type=int, required=True, help="Campo 'cod_email' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201


class Email(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_email', type=int, required=False)
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('descricao', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_email': item[0],
                'cod_usuario': item[1],
                'descricao': item[2],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=True, help="Campo 'cod_usuario' é obrigatório.")
        parser.add_argument('descricao', type=str, required=True, help="Campo 'descricao' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_insert_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('descricao', type=str, required=True, help="Campo 'descricao' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_email', type=int, required=True, help="Campo 'cod_email' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'emails')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201


class UsuarioPrivilegio(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('cod_privilegio', type=int, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'usuarios_privilegios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_usuario': item[0],
                'cod_privilegio': item[1],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=True, help="Campo 'cod_usuario' é obrigatório.")
        parser.add_argument('cod_privilegio', type=int, required=True, help="Campo 'cod_privilegio' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_insert_tabela_unica(args, 'usuarios_privilegios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):
        return {
            'status': 0,
            'msg': 'Método PUT não aceito.'
        }
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=True, help="Campo 'cod_usuario' é obrigatório.")
        parser.add_argument('cod_privilegio', type=int, required=True, help="Campo 'cod_privilegio' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica_2_parametros(args, 'usuarios_privilegios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
