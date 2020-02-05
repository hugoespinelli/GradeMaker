
from dotenv import load_dotenv
load_dotenv()
from AlunoOnlineCrawler import AlunoOnlineCrawler
from GradeMaker import exportarExcel
from src.Aluno import Aluno
from consts import MATRICULA, SENHA

aluno = Aluno(MATRICULA, SENHA)
# Botar os codigos das disciplinas que você quer cursar aqui
aluno.setCodigos(
	"01913",
	"05153",
	"05105",
	"05253",
	"05222",
	"01840",
	"04192",
	"04386"
)
# Caso queira puxar o máximo de matérias por periodo, descomente o código abaixo e comente
# o código acima
# aluno.setPeriodos([1, 5, 6, 7, 8])
crawlerAlunoOnline = AlunoOnlineCrawler(aluno)
crawlerAlunoOnline.salvaInfoDisciplinas()
exportarExcel()