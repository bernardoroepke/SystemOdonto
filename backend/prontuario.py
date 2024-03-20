from flask_restful import Resource, reqparse
import functions

class Prontuario(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_prontuario', type=int, required=False)
        parser.add_argument('cod_cliente', type=int, required=False)
        parser.add_argument('cod_atendimento', type=int, required=False)
        parser.add_argument('anamnese', type=str, required=False)
        parser.add_argument('plano_terapeutico', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'prontuarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_prontuario': item[0],
                'cod_cliente': item[1],
                'cod_atendimento': item[2],
                'anamnese': item[3],
                'plano_terapeutico': item[4],
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
        parser.add_argument('cod_atendimento', type=int, required=True, help="Campo 'cod_atendimento' é obrigatório.")
        parser.add_argument('anamnese', type=str, required=False)
        parser.add_argument('plano_terapeutico', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_insert_tabela_unica(args, 'prontuarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_prontuario', type=int, required=True, help="Campo 'cod_prontuario' é obrigatório.")
        parser.add_argument('cod_cliente', type=int, required=False)
        parser.add_argument('cod_atendimento', type=int, required=False)
        parser.add_argument('anamnese', type=str, required=False)
        parser.add_argument('plano_terapeutico', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'prontuarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_prontuario', type=int, required=True, help="Campo 'cod_prontuario' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'prontuarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    

class ProntuarioProcedimento(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_prontuario', type=int, required=False)
        parser.add_argument('cod_procedimento', type=int, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'prontuarios_procedimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_prontuario': item[0],
                'cod_procedimento': item[1],
            })

        return {
            'status': response['status'],
            'data': data
        }, 200
                
    #Tratativa de requisição POST
    def post(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_prontuario', type=int, required=True, help="Campo 'cod_prontuario' é obrigatório.")
        parser.add_argument('cod_procedimento', type=int, required=True, help="Campo 'cod_procedimento' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_insert_tabela_unica(args, 'prontuarios_procedimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):
        return {
            'status': 0,
            'msg': 'Método PUT não aceito.'
        }
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_prontuario', type=int, required=True, help="Campo 'cod_prontuario' é obrigatório.")
        parser.add_argument('cod_procedimento', type=int, required=True, help="Campo 'cod_procedimento' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica_2_parametros(args, 'prontuarios_procedimentos')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    