from flask_restful import Resource, reqparse
import backend.functions as functions

class Funcionario(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_funcionario', type=int, required=False)
        parser.add_argument('cod_usuario', type=int, required=False)
        parser.add_argument('cod_cargo', type=int, required=False)
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('cod_especialidade', type=int, required=False)
        parser.add_argument('nome', type=str, required=False)
        parser.add_argument('data_nascimento', type=str, required=False)
        parser.add_argument('cpf', type=str, required=False)
        parser.add_argument('ramal', type=str, required=False)
        parser.add_argument('cro', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'funcionarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500
        
        #Organizando os dados que serão retornados
        data = []
        for item in response['data']:
            data.append({
                'cod_funcionario': item[0],
                'cod_usuario': item[1],
                'cod_cargo': item[2],
                'cod_situacao': item[3],
                'cod_especialidade': item[4],
                'nome': item[5],
                'data_nascimento': item[6],
                'cpf': item[7],
                'cro': item[8]
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
        parser.add_argument('cod_cargo', type=int, required=True, help="Campo 'cod_cargo' é obrigatório.")
        parser.add_argument('cod_situacao', type=int, required=True, help="Campo 'cod_situacao' é obrigatório.")
        parser.add_argument('cod_especialidade', type=int, required=False)
        parser.add_argument('nome', type=str, required=True, help="Campo 'nome' é obrigatório.")
        parser.add_argument('data_nascimento', type=str, required=True, help="Campo 'data_nascimento' é obrigatório.")
        parser.add_argument('cpf', type=str, required=True, help="Campo 'cpf' é obrigatório.")
        parser.add_argument('ramal', type=str, required=False)
        parser.add_argument('cro', type=str, required=False)
        args = parser.parse_args()
        
        login = functions.gerar_login(args)
        falha = functions.verifica_falha_requisicao(login)

        if falha is not None:
            return falha, 500
        
        #Adicionando cod_usuario dentro de argumentos para cadastrar funcionario
        args['cod_usuario'] = login['cod_usuario']

        response = functions.monta_sql_insert_tabela_unica(args, 'funcionarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201

    #Tratativa de requisição PUT
    def put(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_funcionario', type=int, required=True, help="Campo 'cod_funcionario' é obrigatório.")
        parser.add_argument('cod_cargo', type=int, required=False)
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('cod_especialidade', type=int, required=False)
        parser.add_argument('nome', type=str, required=False)
        parser.add_argument('data_nascimento', type=str, required=False)
        parser.add_argument('cpf', type=str, required=False)
        parser.add_argument('ramal', type=str, required=False)
        parser.add_argument('cro', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_update_tabela_unica(args, 'funcionarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    
    #Tratativa de requisição DELETE
    def delete(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_funcionario', type=int, required=True, help="Campo 'cod_funcionario' é obrigatório.")
        args = parser.parse_args()

        response = functions.monta_sql_delete_tabela_unica(args, 'funcionarios')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201
    

class FuncionarioSituacao(Resource):

    #Tratativa de requisição GET
    def get(self):

        #Adicionando possíveis argumentos para a requisição
        parser = reqparse.RequestParser()
        parser.add_argument('cod_situacao', type=int, required=False)
        parser.add_argument('descricao', type=str, required=False)
        args = parser.parse_args()

        response = functions.monta_sql_select_tabela_unica(args, 'funcionarios_situacoes')
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

        response = functions.monta_sql_insert_tabela_unica(args, 'funcionarios_situacoes')
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

        response = functions.monta_sql_update_tabela_unica(args, 'funcionarios_situacoes')
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

        response = functions.monta_sql_delete_tabela_unica(args, 'funcionarios_situacoes')
        falha = functions.verifica_falha_requisicao(response)

        if falha is not None:
            return falha, 500

        return response, 201