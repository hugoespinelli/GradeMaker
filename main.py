
from AlunoOnlineCrawler import AlunoOnlineCrawler
from GradeMaker import exportarExcel
from src.Aluno import Aluno
from consts import MATRICULA, SENHA

aluno = Aluno(MATRICULA, SENHA)
# Botar os codigos das disciplinas que você quer cursar aqui
aluno.setCodigos(
	"05222",
	"03787",
	"04049",
	"05038",
	"04516",
	"04314",
	"01840",
	"05153"
)
# Caso queira puxar o máximo de matérias por periodo, descomente o código abaixo e comente
# o código acima
# aluno.setPeriodos()
crawlerAlunoOnline = AlunoOnlineCrawler(aluno)
crawlerAlunoOnline.salvaInfoDisciplinas()
exportarExcel()