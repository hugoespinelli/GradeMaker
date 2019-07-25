

class Aluno():

	def __init__(self, matricula, password):
		self.matricula = matricula
		self.password = password
		self.buscaPorCodigo = False
		self.buscaPorPeriodo = False

	def setPeriodos(self, *periodos):
		self.periodos = periodos
		self.buscaPorPeriodo = True
		self.buscaPorCodigo = False

	def setCodigos(self, *codigos):
		self.codigos = codigos
		self.buscaPorCodigo = True
		self.buscaPorPeriodo = False