from flask_restful import Resource, reqparse
import backend.functions as functions

class Fornecedor(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_fornecedor', type=int, required=False)
        parser.add_argument('cnpj', type=str, required=False)
        parser.add_argument('razao_social', type=str, required=False)
        parser.add_argument('email', type=str, required=False)
        parser.add_argument('telefone', type=str, required=False)
        parser.add_argument('logradouro', type=str, required=False)
        parser.add_argument('numero', type=str, required=False)
        parser.add_argument('bairro', type=str, required=False)
        parser.add_argument('cidade', type=str, required=False)
        parser.add_argument('cep', type=str, required=False)
        parser.add_argument('uf', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_select_tabela_unica(args, 'fornecedores')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_fornecedor': item[0],
                'cnpj': item[1],
                'razao_social': item[2],
                'email': item[3],
                'telefone': item[4],
                'logradouro': item[5],
                'numero': item[6],
                'bairro': item[7],
                'cidade': item[8],
                'cep': item[9],
                'uf': item[10],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cnpj', type=str, required=True, help="Campo 'cnpj' é obrigatório.")
        parser.add_argument('razao_social', type=str, required=True, help="Campo 'razao_social' é obrigatório.")
        parser.add_argument('email', type=str, required=True, help="Campo 'email' é obrigatório.")
        parser.add_argument('telefone', type=str, required=True, help="Campo 'telefone' é obrigatório.")
        parser.add_argument('logradouro', type=str, required=True, help="Campo 'logradouro' é obrigatório.")
        parser.add_argument('numero', type=str, required=True, help="Campo 'numero' é obrigatório.")
        parser.add_argument('bairro', type=str, required=True, help="Campo 'bairro' é obrigatório.")
        parser.add_argument('cidade', type=str, required=True, help="Campo 'cidade' é obrigatório.")
        parser.add_argument('cep', type=str, required=True, help="Campo 'cep' é obrigatório.")
        parser.add_argument('uf', type=str, required=True, help="Campo 'uf' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_insert_tabela_unica(args, 'fornecedores')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_fornecedor', type=int, required=True, help="Campo 'cod_fornecedor' é obrigatório.")
        parser.add_argument('cnpj', type=str, required=False)
        parser.add_argument('razao_social', type=str, required=False)
        parser.add_argument('email', type=str, required=False)
        parser.add_argument('telefone', type=str, required=False)
        parser.add_argument('logradouro', type=str, required=False)
        parser.add_argument('numero', type=str, required=False)
        parser.add_argument('bairro', type=str, required=False)
        parser.add_argument('cidade', type=str, required=False)
        parser.add_argument('cep', type=str, required=False)
        parser.add_argument('uf', type=str, required=False)
        args = parser.parse_args()

        response = functions.sql_update_tabela_unica(args, 'fornecedores')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_fornecedor', type=int, required=True, help="Campo 'cod_fornecedor' é obrigatório.")
        args = parser.parse_args()

        response = functions.sql_delete_tabela_unica(args, 'fornecedores')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
