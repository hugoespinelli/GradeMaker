
class Turma:

	codigo = ''
	turma = None
	tempos = []

	def __init__(self, turma, tempos):
		self.codigo = turma['codigo']
		self.turma = turma['turma']
		self.tempos = tempos
		self.professor = turma['professor']
		self.disciplina = turma['disciplina']
		# self.nota = turma['nota']
