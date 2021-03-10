from tkinter import *
import time

class Cronometro():
	def __init__(self, instancia):
		self.inst = instancia

		fonte = ('Verdana', 40)
		fontem = ('Verdana', 30)

		self.tempo = Label(self.inst, text='00:00:00:000', font=fonte, pady=50)
		self.tempo.pack()


		# ================== BOTÕES ==================

		framebut = Frame(self.inst)

		self.bINICIA = Button(framebut, text='INICIA', font=fontem, command=self.Atualiza)
		ANOTA = Button(framebut, text='SALVA', font=fontem)

		self.bINICIA.pack(side=LEFT)
		ANOTA.pack(side=LEFT)

		# ============================================

		framebut.pack()


		self.ms = self.s = self.m = self.h = 0

	def Atualiza(self):
		
		self.ms += 1

		# Nome dos métodos que vão ser usados
		lista = [('ms', 1000), ('s', 60), ('m', 60), ('h', 1000)]
		
		# Percorre os valores dentro da lista, além de obter o índice
		for i, elemento in enumerate(lista):

			# Formata a classe em um dicionário e utiliza dos nomes para acessar os atributos da classe Cronometro
			if self.__dict__[elemento[0]] >= elemento[1]:
				
				self.__dict__[lista[i+1][0]] += 1   # Obtem o indíce adiante e aumenta em 1
				self.__dict__[elemento[0]] = 0      # Reseta o valor do indíce anterior

		self.Formata()
		self.inst.after(1, self.Atualiza) # Atualiza a cada 1 milissegundo

	def Formata(self):
		self.tempo['text'] = '%.2i:%.2i:%.2i:%.3i' %(int(self.h), int(self.m), int(self.s), int(self.ms))


inst = Cronometro(Tk()).inst
inst.mainloop()
