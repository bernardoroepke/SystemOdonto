from flask_restful import Resource, reqparse
import backend.functions as functions

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
                'cod_situacao': item[5],
                'cod_situacao': item[6],
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
    