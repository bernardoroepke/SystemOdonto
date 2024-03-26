from flask_restful import Resource, reqparse
import backend.functions as functions

class Estoque(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_estoque', type=int, required=False)
        parser.add_argument('cod_material', type=int, required=False)
        parser.add_argument('quantidade', type=int, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'estoques')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_estoque': item[0],
                'cod_material': item[1],
                'quantidade': item[2],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_material', type=str, required=True, help="Campo 'cod_material' é obrigatório.")
        parser.add_argument('quantidade', type=int, required=True, help="Campo 'quantidade' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_insert_tabela_unica(args, 'estoques')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_estoque', type=int, required=True, help="Campo 'cod_estoque' é obrigatório.")
        parser.add_argument('cod_material', type=int, required=False)
        parser.add_argument('quantidade', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_update_tabela_unica(args, 'estoques')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_estoque', type=int, required=True, help="Campo 'cod_estoque' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_delete_tabela_unica(args, 'estoques')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
