from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_restful import Api
from backend.classes.usuario import *
from backend.classes.privilegio import *
from backend.classes.cliente import *
from backend.classes.funcionario import *
from backend.classes.endereco import *
from backend.classes.fornecedor import *
from backend.classes.atendimento import *
from backend.classes.cargo import *
from backend.classes.especialidade import *
from backend.classes.plano_saude import *
from backend.classes.agenda import *
from backend.classes.ramal import *
from backend.classes.prontuario import *
from backend.classes.procedimento import *
from backend.classes.equipamento import *
from backend.classes.estoque import *
from backend.classes.material import *
from backend.classes.ordem_servico import *
from backend.classes.configuracao_sistema import *

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
api.add_resource(FuncionarioProcedimento, '/funcionario/procedimento')
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

if  __name__ == '__main__':
    app.run()