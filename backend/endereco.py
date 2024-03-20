from flask_restful import Resource, reqparse
import functions

class Endereco(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_endereco', type=int, required=False)
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('logradouro', type=str, required=False)
        parser.add_argument('numero', type=str, required=False)
        parser.add_argument('bairro', type=str, required=False)
        parser.add_argument('cidade', type=str, required=False)
        parser.add_argument('cep', type=str, required=False)
        parser.add_argument('uf', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'enderecos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_endereco': item[0],
                'cod_usuario': item[1],
                'logradouro': item[2],
                'numero': item[3],
                'bairro': item[4],
                'cidade': item[5],
                'cep': item[6],
                'uf': item[7],
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
        parser.add_argument('logradouro', type=str, required=True, help="Campo 'logradouro' é obrigatório.")
        parser.add_argument('numero', type=str, required=True, help="Campo 'numero' é obrigatório.")
        parser.add_argument('bairro', type=str, required=True, help="Campo 'bairro' é obrigatório.")
        parser.add_argument('cidade', type=str, required=True, help="Campo 'cidade' é obrigatório.")
        parser.add_argument('cep', type=str, required=True, help="Campo 'cep' é obrigatório.")
        parser.add_argument('uf', type=str, required=True, help="Campo 'uf' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_insert_tabela_unica(args, 'enderecos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_endereco', type=int, required=True, help="Campo 'cod_endereco' é obrigatório.")
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('logradouro', type=str, required=False)
        parser.add_argument('numero', type=str, required=False)
        parser.add_argument('bairro', type=str, required=False)
        parser.add_argument('cidade', type=str, required=False)
        parser.add_argument('cep', type=str, required=False)
        parser.add_argument('uf', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'enderecos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_endereco', type=int, required=True, help="Campo 'cod_endereco' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'enderecos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
