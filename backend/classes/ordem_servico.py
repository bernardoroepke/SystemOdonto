from flask_restful import Resource, reqparse
import backend.functions as functions

class OrdemServico(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_ordem_servico', type=int, required=False)
        parser.add_argument('cod_funcionario', type=int, required=False)
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('data_inicio', type=str, required=False)
        parser.add_argument('data_fim', type=str, required=False)
        parser.add_argument('problema', type=str, required=False)
        parser.add_argument('solucao', type=str, required=False)
        parser.add_argument('observacao', type=str, required=False)
        parser.add_argument('valor', type=str, required=False)
        parser.add_argument('forma_pagamento', type=str, required=False)
        parser.add_argument('garantia', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'ordem_servicos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_ordem_servico': item[0],
                'cod_funcionario': item[1],
                'cod_situacao': item[2],
                'data_inicio': item[3],
                'data_fim': item[4],
                'problema': item[5],
                'solucao': item[6],
                'observacao': item[7],
                'valor': item[8],
                'forma_pagamento': item[9],
                'garantia': item[10]
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_funcionario', type=int, required=True, help="Campo 'cod_funcionario' é obrigatório.")
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('data_inicio', type=str, required=False)
        parser.add_argument('data_fim', type=str, required=False)
        parser.add_argument('problema', type=str, required=False)
        parser.add_argument('solucao', type=str, required=False)
        parser.add_argument('observacao', type=str, required=False)
        parser.add_argument('valor', type=str, required=False)
        parser.add_argument('forma_pagamento', type=str, required=False)
        parser.add_argument('garantia', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_insert_tabela_unica(args, 'ordem_servicos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_ordem_servico', type=int, required=True, help="Campo 'cod_ordem_servico' é obrigatório.")
        parser.add_argument('cod_funcionario', type=int, required=False)
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('data_inicio', type=str, required=False)
        parser.add_argument('data_fim', type=str, required=False)
        parser.add_argument('problema', type=str, required=False)
        parser.add_argument('solucao', type=str, required=False)
        parser.add_argument('observacao', type=str, required=False)
        parser.add_argument('valor', type=str, required=False)
        parser.add_argument('forma_pagamento', type=str, required=False)
        parser.add_argument('garantia', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_update_tabela_unica(args, 'ordem_servicos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_ordem_servico', type=int, required=True, help="Campo 'cod_ordem_servico' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_delete_tabela_unica(args, 'ordem_servicos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201


class OrdemServicoSituacao(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('descricao', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'ordem_servicos_situacoes')
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

        response = functions.sql_insert_tabela_unica(args, 'ordem_servicos_situacoes')
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

        response = functions.sql_update_tabela_unica(args, 'ordem_servicos_situacoes')
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

        response = functions.sql_delete_tabela_unica(args, 'ordem_servicos_situacoes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    