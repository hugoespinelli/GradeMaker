from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from consts import DISCIPLINA_URL,TURMA_URL, ALUNO_ONLINE_LOGIN_URL, REQUISITOS_URL
import json
import re

class AlunoOnlineCrawler():

	def __init__(self, aluno):

		self.aluno = aluno

	def logarPaginaPrincipal(self):
		self.driver = webdriver.Chrome()
		self.driver.get(ALUNO_ONLINE_LOGIN_URL)
		email = self.driver.find_element_by_name('matricula')
		email.clear()
		email.send_keys(self.aluno.matricula)

		senha = self.driver.find_element_by_name('senha')
		senha.clear()
		senha.send_keys(self.aluno.password)
		senha.send_keys(Keys.RETURN)

	def getCodigos(self):
		if (self.aluno.buscaPorPeriodo):
			return self.getCodigosDisciplinasAlunoOnline(self.aluno.periodos)
		return self.aluno.codigos


	def salvaInfoDisciplinas(self):
		self.logarPaginaPrincipal()
		codigos = self.getCodigos()
		print(codigos)
		print('chegou dps codigo')
		turmas = self.getTurmasBy(codigos)
		print('chegou dps turma')
		self.getAllProfessoresAndDisciplinas(turmas)
		print('chegou dps professores e disciplinas')
		self.salvarArquivos(turmas)
		self.driver.close()

	def getProfessorAndDisciplina(self, turma):
		self.driver.get(TURMA_URL + turma['codigo'])
		nome_disciplina = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/div/table/tbody/tr[1]/th/div").text
		nome_disciplina = nome_disciplina.replace("Disciplina:", "")
		tbody = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/div/table")
		turma_escolhida = str(int(turma['turma']) + 1)
		professor = tbody.find_element_by_xpath('/html/body/table/tbody/tr[3]/td/div/table/tbody/tr['+turma_escolhida+']/td/div/div[2]/div[8]/div[2]')
		turma['professor'] = professor.text
		turma['disciplina'] = nome_disciplina
		return turma


	def getCodigosDisciplinasAlunoOnline(self, periodos):
		disciplinas = []
		self.driver.get(REQUISITOS_URL)
		tbody = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/table/tbody/tr[1]/td/table/tbody")
		trs = tbody.find_elements_by_tag_name('tr')
		trs.pop(0)

		for tr in trs:
			tds = tr.find_elements_by_tag_name('td')
			if int(tds[3].text) in periodos:
				matchObj = re.search("(\d\d\d\d\d)", tds[0].text)
				disciplinas.append(matchObj.group())

		print(disciplinas)
		return disciplinas


	def getTurmasBy(self, disciplinas):
		horarios = []
		for disciplina in disciplinas:
			self.driver.get(DISCIPLINA_URL + disciplina)
			#driver.save_screenshot(disciplina+'.png')
			tbody = self.driver.find_element_by_xpath("/html/body/table/tbody/tr[3]/td/div/div[7]/table/tbody")
			trs = tbody.find_elements_by_tag_name('tr')
			trs.pop(0)
			trs.pop(0)
			print(len(trs))
			for tr in trs:
				tds = tr.find_elements_by_tag_name('td')
				if(len(tds) > 1):
					turma = {
						'codigo': disciplina,
						'turma': tds[0].text,
						'tempos': tds[9].text
					}
					horarios.append(turma)

		return horarios

		
	def getAllProfessoresAndDisciplinas(self, turmas):
		for turma in turmas:
			turma = self.getProfessorAndDisciplina(turma)


	def salvarArquivos(self, turmas):
		file = open("disciplinas.json", "w+")
		file.write(json.dumps(turmas))
		file.close()



