from flask_restful import Resource, reqparse
import backend.functions as functions

class Material(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_material', type=int, required=False)
        parser.add_argument('nome', type=str, required=False)
        parser.add_argument('codigo', type=str, required=False)
        parser.add_argument('tipo', type=str, required=False)
        parser.add_argument('validade', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'materiais')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_material': item[0],
                'cod_situacao': item[1],
                'nome': item[2],
                'codigo': item[3],
                'tipo': item[4],
                'validade': item[5]
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('nome', type=str, required=True, help="Campo 'nome' é obrigatório.")
        parser.add_argument('codigo', type=str, required=False)
        parser.add_argument('tipo', type=str, required=False)
        parser.add_argument('validade', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_insert_tabela_unica(args, 'materiais')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_material', type=int, required=True, help="Campo 'cod_material' é obrigatório.")
        parser.add_argument('nome', type=str, required=False)
        parser.add_argument('codigo', type=str, required=False)
        parser.add_argument('tipo', type=str, required=False)
        parser.add_argument('validade', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_update_tabela_unica(args, 'materiais')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_material', type=int, required=True, help="Campo 'cod_material' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_delete_tabela_unica(args, 'materiais')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
