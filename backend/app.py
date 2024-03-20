from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
from usuario import *
from privilegio import *
from cliente import *
from funcionario import *
from endereco import *
from fornecedor import *
from atendimento import *
from cargo import *
from especialidade import *
from plano_saude import *
from agenda import *
from ramal import *
from prontuario import *
from procedimento import *
from equipamento import *
from estoque import *
from material import *
from ordem_servico import *
from configuracao_sistema import *

app = Flask(__name__)
api = Api(app)
CORS(app)

api.add_resource(Usuario, '/usuario')
api.add_resource(UsuarioPrivilegio, '/usuario/privilegio')
api.add_resource(Privilegio, '/privilegio')
api.add_resource(Cliente, '/cliente')
api.add_resource(ClienteSituacao, '/cliente/situacao')
api.add_resource(Funcionario, '/funcionario')
api.add_resource(FuncionarioSituacao, '/funcionario/situacao')
api.add_resource(Endereco, '/endereco')
api.add_resource(Fornecedor, '/fornecedor')
api.add_resource(Atendimento, '/atendimento')
api.add_resource(AtendimentoSituacao, '/atendimento/situacao')
api.add_resource(Cargo, '/cargo')
api.add_resource(Especialidade, '/especialidade')
api.add_resource(Telefone, '/telefone')
api.add_resource(Email, '/email')
api.add_resource(PlanoSaude, '/planosaude')
api.add_resource(Agenda, '/agenda')
api.add_resource(Ramal, '/ramal')
api.add_resource(Prontuario, '/prontuario')
api.add_resource(ProntuarioProcedimento, '/prontuario/procedimento')
api.add_resource(Procedimento, '/procedimento')
api.add_resource(Equipamento, '/equipamento')
api.add_resource(EquipamentoSituacao, '/equipamento/situacao')
api.add_resource(Estoque, '/estoque')
api.add_resource(Material, '/material')
api.add_resource(OrdemServico, '/ordemservico')
api.add_resource(OrdemServicoSituacao, '/ordemservico/situacao')
api.add_resource(ConfiguracaoSistema, '/configuracaosistema')

app.run(host='0.0.0.0', debug=True)