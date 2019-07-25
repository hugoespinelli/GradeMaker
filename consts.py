import os

MAIN_URL_ALUNO_ONLINE = "https://www.alunoonline.uerj.br/requisicaoaluno/requisicaoacesso.php?requisicao="
ALUNO_ONLINE_LOGIN_URL = MAIN_URL_ALUNO_ONLINE + "LoginAlunoOnline"
DISCIPLINA_URL = MAIN_URL_ALUNO_ONLINE + "DadosDisciplina&disciplinas[0]="
TURMA_URL = MAIN_URL_ALUNO_ONLINE + "HorariosTurmasDisciplina&disciplinas[0]="
REQUISITOS_URL = MAIN_URL_ALUNO_ONLINE + "RequisitosACursar"
MAMATA_URL = "https://carrascomamata.com.br/"

MATRICULA = os.getenv("MATRICULA")
SENHA = os.getenv("SENHA")