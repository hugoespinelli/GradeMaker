import copy

class Grade:
	dias = ['SEG', 'TER', 'QUA', 'QUI', 'SEX', 'SAB']
	consts = {
		"SEG": 0,
		"TER": 1,
		"QUA": 2,
		"QUI": 3,
		"SEX": 4,
		"SAB": 5,
		"M": 0,
		"T": 6,
		"N": 12
	}
	ESPACO = 11

	def __init__(self):

		self.turmas = []

		self.horario_livre = [
			[' ' * self.ESPACO] * 18,
			[' ' * self.ESPACO] * 18,
			[' ' * self.ESPACO] * 18,
			[' ' * self.ESPACO] * 18,
			[' ' * self.ESPACO] * 18,
			[' ' * self.ESPACO] * 18];

		self.prioridade = []

	def adicionarTurma(self, turma):

		if (not self.isHorarioLivre(turma)):
			return

		for tempo in turma.tempos:

			for dia in self.dias:

				if (dia in tempo):

					tempo = tempo.replace(dia, "")

					for i in range(0, len(tempo) // 2):
						hora = self.consts[tempo[i * 2]] + int(tempo[i * 2 + 1]) - 1
						self.horario_livre[self.consts[dia]][hora] = turma.disciplina + " -   " + turma.turma

		self.turmas.append(turma)

	def isHorarioLivre(self, turma):
		for tempo in turma.tempos:

			for dia in self.dias:

				if (dia in tempo):

					tempo = tempo.replace(dia, "")

					for i in range(0, len(tempo) // 2):

						if (not self.getTurnoByIndex(self.consts[tempo[i * 2]])[0] in self.prioridade):
							return False

						hora = self.consts[tempo[i * 2]] + int(tempo[i * 2 + 1])

						if (self.horario_livre[self.consts[dia]][hora] != ' ' * self.ESPACO):
							return False

		return True

	def mostrarGrade(self):
		linha = ' ' * 8
		for dia in self.dias:
			linha += dia + ' ' * 4 + '|' + ' ' * 6

		linha += '\n'

		for i in range(0, 18):

			linha += self.getTurnoByIndex(i) + ' '

			for dia in self.dias:
				linha += self.horario_livre[self.consts[dia]][i] + ' | '

			linha += '\n'

		return linha

	def getTurnoByIndex(self, index):
		turno = ''
		if (index < self.consts['T']):
			turno = 'M'
		elif (index < self.consts['N']):
			turno = 'T'
		else:
			turno = 'N'

		index = index % 6 + 1
		turno = turno + str(index)
		return turno

	def getHorariosLivre(self):
		row = zip(*self.horario_livre)
		return row

	def getDias(self):
		return copy.deepcopy(self.dias)

	def getProfessores(self):
		professores = []

		for turma in self.turmas:
			professores.append(turma.professor)

		return professores

	def getDisciplinas(self):
		disciplinas = []

		for turma in self.turmas:
			disciplinas.append(turma.disciplina + " - " + turma.turma)

		return disciplinas

	def getTurmas(self):
		return copy.deepcopy(self.turmas)

	def getCodigosTurmas(self):
		codigos = []

		for turma in self.turmas:
			codigos.append(turma.codigo)

		return codigos

