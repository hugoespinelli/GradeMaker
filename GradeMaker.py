import json
import re
from src.Turma import Turma
from src.Grade import Grade
from openpyxl import Workbook


def exportarExcel():

	print("Calculando grades...")

	with open("disciplinas.json") as s:
		disciplinas = json.load(s)


	turmas = []


	for disciplina in disciplinas:

		tempos = disciplina["tempos"].replace(" ","")
		tempos = tempos.replace("\n\n", "Z")
		tempos = tempos.replace("\n", "")
		matchObj = re.split(r'Z', tempos)
		tempos_formatados = matchObj
		turma = Turma(disciplina, tempos_formatados)
		turmas.append(turma)


	grades = []


	def isGradeJaInclusa(grades, grade):

		for g in grades:
			if(g.turmas == grade.turmas):
				return True

		return False


	# for i in range(0, len(materias)):
	# 	materias.insert(0, materias.pop())
	# 	fazerGrade(materias)


	def fazerGrade(turmas):

		grade = Grade()
		grade.prioridade.append('N')
		grade.prioridade.append('T')
		grade.prioridade.append('M')

		for turma in turmas:

			if(not turma.codigo in grade.getCodigosTurmas()):
				grade.adicionarTurma(turma)

		if(not isGradeJaInclusa(grades, grade)):
			grades.append(grade)


	def salvaExcel():
		print("Salvando excel...")
		book = Workbook()
		sheet = book.active

		# Escreve professores e disciplinas
		todas_disciplinas = []
		# sheet.append(['DISCIPLINA', 'PROFESSOR', 'NOTA'])
		sheet.append(['DISCIPLINA', 'PROFESSOR', 'NOTA'])
		for grade in grades:
			turmas = grade.getTurmas()

			for turma in turmas:
				if(not turmas in todas_disciplinas):
					todas_disciplinas.append(turmas)
					# sheet.append((turma.disciplina + ' - ' + turma.turma, turma.professor, turma.nota))
					sheet.append((turma.disciplina + ' - ' + turma.turma, turma.professor))

		# Pula linha
		sheet.append([])
		sheet.append([])

		# Escreve a grade
		for grade in grades:

			dias = grade.getDias()
			dias.insert(0, "")
			sheet.append(dias)
			rows = grade.getHorariosLivre()

			turno = 0

			for row in rows:
				turno_lista = []
				turno_lista.append(grade.getTurnoByIndex(turno))
				turno_tupla = tuple(turno_lista)
				sheet.append(turno_tupla+row)
				turno += 1

			sheet.append([])
    

		book.save("horarioGrade.xlsx")


	for i in range(0, len(turmas)):
		turmas.insert(0, turmas.pop())
		print("%d grade realizada..." % i)
		fazerGrade(turmas)
	

	salvaExcel()

	for grade in grades:
		grade.mostrarGrade()