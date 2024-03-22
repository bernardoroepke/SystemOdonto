from flask_restful import Resource, reqparse
import backend.functions as functions
import mysql.connector
import os

#Dados de conexão com banco de dados
db_host = os.environ.get('DBHOST')
db_user = os.environ.get('DBUSER')
db_password = os.environ.get('DBPASSWORD')
db_database = os.environ.get('DBDATABASE')

class Atendimento(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_atendimento', type=int, required=False)
        parser.add_argument('cod_cliente', type=int, required=False)
        parser.add_argument('cod_funcionario', type=int, required=False)
        parser.add_argument('cod_procedimento', type=int, required=False)
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('data_inicio', type=str, required=False)
        parser.add_argument('data_fim', type=str, required=False)
        parser.add_argument('observacao', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'atendimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_atendimento': item[0],
                'cod_cliente': item[1],
                'cod_funcionario': item[2],
                'cod_procedimento': item[3],
                'cod_situacao': item[4],
                'data_inicio': item[5],
                'data_fim': item[6],
                'observacao': item[7]
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_cliente', type=int, required=True, help="Campo 'cod_cliente' é obrigatório.")
        parser.add_argument('cod_funcionario', type=int, required=True, help="Campo 'cod_funcionario' é obrigatório.")
        parser.add_argument('cod_procedimento', type=int, required=True, help="Campo 'cod_procedimento' é obrigatório.")
        parser.add_argument('cod_situacao', type=int, required=True, help="Campo 'cod_situacao' é obrigatório.")
        parser.add_argument('data_inicio', type=str, required=True, help="Campo 'data_inicio' é obrigatório.")
        parser.add_argument('data_fim', type=str, required=True, help="Campo 'data_fim' é obrigatório.")
        parser.add_argument('observacao', type=str, required=False)
        args = parser.parse_args()
        
        response = functions.monta_sql_insert_tabela_unica(args, 'atendimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_atendimento', type=int, required=True, help="Campo 'cod_atendimento' é obrigatório.")
        parser.add_argument('cod_cliente', type=int, required=False)
        parser.add_argument('cod_funcionario', type=int, required=False)
        parser.add_argument('cod_procedimento', type=int, required=False)
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('data_inicio', type=str, required=False)
        parser.add_argument('data_fim', type=str, required=False)
        parser.add_argument('observacao', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'atendimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_atendimento', type=int, required=True, help="Campo 'cod_atendimento' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'atendimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    

class AtendimentoSituacao(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('descricao', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'atendimentos_situacoes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_situacao': item[0],
                'descricao': item[1],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('descricao', type=str, required=True, help="Campo 'descricao' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_insert_tabela_unica(args, 'atendimentos_situacoes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_situacao', type=int, required=True, help="Campo 'cod_situacao' é obrigatório.")
        parser.add_argument('descricao', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'atendimentos_situacoes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_situacao', type=int, required=True, help="Campo 'cod_situacao' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'atendimentos_situacoes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    

class AtendimentoCompleto(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_atendimento', type=int, required=True, help="Campo cod_atendimento é obrigatório.")
        args = parser.parse_args()

        sql = f'''SELECT a.*, c.nome as nome_cliente,\
            f.nome as nome_funcionario,\
            p.descricao as descricao_procedimento,\
            p.preco as preco_procedimento,\
            s.descricao as descricao_situacao
            FROM atendimentos a
            INNER JOIN clientes c ON a.cod_cliente = c.cod_cliente
            INNER JOIN funcionarios f ON a.cod_funcionario = f.cod_funcionario
            INNER JOIN procedimentos p ON a.cod_procedimento = p.cod_procedimento
            INNER JOIN atendimentos_situacoes s ON a.cod_situacao = s.cod_situacao
            WHERE a.cod_atendimento = {args['cod_atendimento']};'''
        
        response = functions.executa_sql_select(sql)
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500
        
        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_atendimento': item[0],
                'cliente': item[1],
                'funcionario': item[2],
                'procedimento': item[3],
                'situacao': item[4],
                'data_inicio': item[5],
                'data_fim': item[6],
                'observacao': item[7],
                'created_at': item[8],
                'updated_at': item[9],
                'nome_cliente': item[10],
                'nome_funcionario': item[11],
                'descricao_procedimento': item[12],
                'preco_procedimento': item[13],
                'descricao_situacao': item[14]
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
