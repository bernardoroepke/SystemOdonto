from flask_restful import Resource, reqparse
import backend.functions as functions

class Procedimento(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_procedimento', type=int, required=False)
        parser.add_argument('descricao', type=str, required=False)
        parser.add_argument('preco', type=float, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'procedimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_procedimento': item[0],
                'descricao': item[1],
                'preco': item[2],
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
        parser.add_argument('preco', type=float, required=True, help="Campo 'preco' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_insert_tabela_unica(args, 'procedimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_procedimento', type=int, required=True, help="Campo 'cod_procedimento' é obrigatório.")
        parser.add_argument('descricao', type=str, required=False)
        parser.add_argument('preco', type=float, required=False)
        args = parser.parse_args()

        response = functions.sql_update_tabela_unica(args, 'procedimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_procedimento', type=int, required=True, help="Campo 'cod_procedimento' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_delete_tabela_unica(args, 'procedimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
