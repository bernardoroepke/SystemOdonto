from flask_restful import Resource, reqparse
import backend.functions as functions

class Agenda(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_agenda', type=int, required=False)
        parser.add_argument('cod_atendimento', type=int, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'agendas')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_agenda': item[0],
                'cod_atendimento': item[1],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_atendimento', type=int, required=True, help="Campo 'cod_atendimento' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_insert_tabela_unica(args, 'agendas')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_agenda', type=int, required=True, help="Campo 'cod_agenda' é obrigatório.")
        parser.add_argument('cod_atendimento', type=int, required=False)
        args = parser.parse_args()

        response = functions.sql_update_tabela_unica(args, 'agendas')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_agenda', type=int, required=True, help="Campo 'cod_agenda' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_delete_tabela_unica(args, 'agendas')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
