from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from consts import MAMATA_URL
import time
import json
import re

driver = webdriver.Chrome()

def main():

	professores = []
	disciplinas = []
	faculdade = "UERJ"

	def findTeacher(name):		
		if(name in professores):
			return

		professores.append(name)
		input_html = driver.find_element_by_xpath("//*[@id='search-input']")
		input_html.clear()
		input_html.send_keys(name)
		time.sleep(2.5)

		try:
			# isFine = WebDriverWait(driver, 4).until(
			# 	EC.element_located_selection_state_to_be((By.ID, "search-result"), len(driver.find_element_by_id("search-result").find_elements_by_tag_name("a")) > 0)
			# )
			print('entrou')
			element = driver.find_element_by_id("search-result")
			a_links = element.find_elements_by_tag_name("a")

			if(a_links):
				header = a_links[0].find_element_by_tag_name('h4')
				college = a_links[0].find_element_by_tag_name('h5')
				print('professor: ', header.text)
				print('name: ', name)

				if(college.text.find(faculdade) != -1):
					link = a_links[0].get_attribute('href')
					return link
		except:
			print('erro')


	def loadFile(disciplinas):
		with open("disciplinas.json") as s:
			disciplinas = json.load(s)
			return disciplinas

	def getInfoTeacher(link):
		if(not link):
			return
		driver.get(link)
		element = driver.find_element_by_xpath('/html/body/div[2]/div/div[1]/div[2]/div/div[2]')
		return element.text

	def salvarArquivos(turmas):
		file = open("disciplinas.json", "w+")
		file.write(json.dumps(turmas))
		file.close()


	driver.get(MAMATA_URL);
	disciplinas = loadFile(disciplinas)

	for disciplina in disciplinas:
		professores_temp = disciplina['professor'].split("\n")
		for prof in professores_temp:
			disciplina['link'] = findTeacher(prof)

	for disciplina in disciplinas:
		disciplina['nota'] = getInfoTeacher(disciplina['link'])

	salvarArquivos(disciplinas)

	driver.close()

main()


