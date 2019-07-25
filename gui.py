from noname import *
from AlunoOnlineCrawler import AlunoOnlineCrawler
import re

class myGui(MyFrame6):

	def __init__(self, parent):
		self.parent = parent
		print(self.parent)
		MyFrame6.__init__(self, parent)

	def validateForm(self, event):
		pattern = '[^0-9]'
		matricula = self.matricula.GetValue()
		try:
			matchObj = re.search(pattern, matricula)
			if(matchObj or len(matricula) != 12):
				raise MatriculaInvalida
			self.connectWebsite()
		except Exception as e:
			wx.MessageBox('Matricula invalida!')

	def connectWebsite(self):
		self.status_bar.Show()
		self.progressLogStatusBar('Iniciando busca...')
		matricula = self.matricula.GetValue()
		password = self.password.GetValue()
		driver_ao = AlunoOnlineCrawler(matricula, password)
		driver_ao.getAllInfo(self.progressLogStatusBar)

	def progressLogStatusBar(self, msg):
		self.status_bar.SetStatusText(msg)



app = wx.App(False)
frm = myGui(None)
frm.Show()
app.MainLoop()