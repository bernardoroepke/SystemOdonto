from flask_restful import Resource, reqparse
import backend.functions as functions

class Cliente(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_cliente', type=int, required=False)
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('cod_plano_saude', type=int, required=False)
        parser.add_argument('nome', type=str, required=False)
        parser.add_argument('data_nascimento', type=str, required=False)
        parser.add_argument('cpf', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'clientes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_cliente': item[0],
                'cod_usuario': item[1],
                'cod_plano_saude': item[2],
                'nome': item[3],
                'data_nascimento': item[4],
                'cpf': item[5],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('cod_plano_saude', type=int, required=False)
        parser.add_argument('nome', type=str, required=True, help="Campo 'nome' é obrigatório.")
        parser.add_argument('data_nascimento', type=str, required=True, help="Campo 'data_nascimento' é obrigatório.")
        parser.add_argument('cpf', type=str, required=True, help="Campo 'cpf' é obrigatório.")
        args = parser.parse_args()
        
        login = functions.gerar_login(args)
        falha = functions.verifica_falha_requisicao(login)

        if falha is not None:
            return falha, 500
        
        #Adicionando cod_usuario dentro de argumentos para cadastrar cliente
        args['cod_usuario'] = login['cod_usuario']

        response = functions.sql_insert_tabela_unica(args, 'clientes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_cliente', type=int, required=True, help="Campo 'cod_cliente' é obrigatório.")
        parser.add_argument('cod_plano_saude', type=int, required=False)
        parser.add_argument('nome', type=str, required=False)
        parser.add_argument('data_nascimento', type=str, required=False)
        parser.add_argument('cpf', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_update_tabela_unica(args, 'clientes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_cliente', type=int, required=True, help="Campo 'cod_cliente' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_delete_tabela_unica(args, 'clientes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    

class ClienteSituacao(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('descricao', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'clientes_situacoes')
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

        response = functions.sql_insert_tabela_unica(args, 'clientes_situacoes')
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

        response = functions.sql_update_tabela_unica(args, 'clientes_situacoes')
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

        response = functions.sql_delete_tabela_unica(args, 'clientes_situacoes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201


class ClienteCompleto(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_cliente', type=int, required=True, help="Campo cod_cliente é obrigatório.")
        args = parser.parse_args()

        sql = f'''SELECT a.*, p.descricao as descricao_plano_saude,\
                s.descricao as descricao_situacao
                FROM clientes a
                INNER JOIN planos_saude p ON a.cod_plano_saude = p.cod_plano_saude
                INNER JOIN clientes_situacoes s ON a.cod_situacao = s.cod_situacao
                WHERE a.cod_cliente = {args['cod_cliente']};'''
        
        response = functions.sql_select(sql)
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500
        
        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_cliente': item[0],
                'cod_usuario': item[1],
                'cod_plano_saude': item[2],
                'cod_situacao': item[3],
                'nome': item[4],
                'data_nascimento': item[5],
                'cpf': item[6],
                'descricao_plano_saude': item[7],
                'situacao_cliente': item[8]
            })

        return {
            'status': response['status'],
            'data': data
        }, 200


class ClienteProcedimento(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_cliente', type=int, required=True, help="Campo cod_cliente é obrigatório.")
        args = parser.parse_args()

        sql = f'''SELECT a.cod_atendimento as cod_atendimento,
                a.cod_funcionario as cod_funcionario,
                a.cod_procedimento as cod_procedimento,
                a.data_fim as data_fim,
                s.descricao as descricao_situacao,
                f.nome as nome_funcionario,
                p.descricao as descricao_procedimento,
                p.preco as preco_procedimento
                FROM atendimentos a
                INNER JOIN procedimentos p ON a.cod_procedimento = p.cod_procedimento
                INNER JOIN funcionarios f ON a.cod_funcionario = f.cod_funcionario
                INNER JOIN atendimentos_situacoes s ON a.cod_situacao = s.cod_situacao
                WHERE a.cod_cliente = {args['cod_cliente']};'''
            
        response = functions.sql_select(sql)
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500
        
        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_atendimento': item[0],
                'cod_funcionario': item[1],
                'cod_procedimento': item[2],
                'data_fim': item[3],
                'descricao_situacao': item[4],
                'nome_funcionario': item[5],
                'descricao_procedimento': item[6],
                'preco_procedimento': item[7],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200