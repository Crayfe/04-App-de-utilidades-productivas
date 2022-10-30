from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
import time, datetime, sys
import os
print (os.getcwd())
from DataManager import DataManager




#VENTANA PRINCIPAL
class Ventana_Principal():

	def __init__(self, root, dataCollection):
		self.ventana = root
		self.ventana.title("Crayfe Utilities")
		self.data = dataCollection
		self.clicked = "Calendario"
		self.frameContent = None
		#BLOQUE MENU
		self.frameMenu = Frame(self.ventana) 
		self.frameMenu.grid(row=0, column=0, sticky="WE", padx = 5, pady = 5)
		self.infolabel = Label(self.frameMenu, text=time.strftime("Fecha de hoy: %d\\%m\\%Y")).grid(row=0,column=0, padx = 5, pady = 5)
		self.principal = Button(self.frameMenu, text="Principal", command=lambda l="Principal":self.menuHandler(l)).grid(row=0,column=1, padx = 5, pady = 5)
		self.calendario = Button(self.frameMenu, text="Calendario", command=lambda l="Calendario": self.menuHandler(l)).grid(row=0,column=2, padx = 5, pady = 5)
		self.calendario = Button(self.frameMenu, text="Tareas", command=lambda l="Tareas": self.menuHandler(l)).grid(row=0,column=3, padx = 5, pady = 5)
		self.config = Button(self.frameMenu, text="Configuración", command=lambda l="Configuración": self.menuHandler(l)).grid(row=0,column=4, padx = 5, pady = 5)
		self.test = Button(self.frameMenu, text="Test", command=lambda l="Test": self.menuHandler(l)).grid(row=0,column=5, padx = 5, pady = 5)
		self.menuHandler(self.clicked)

	def menuHandler(self, opt):
		if not self.clicked == opt:
			if self.frameContent is not None:
				self.frameContent.destroy()
			self.clicked = opt
			if opt == "Principal":
				self.showPrincipal()
			elif opt == "Calendario":
				self.showCalendario()
			elif opt == "Tareas":
				self.showTareas()
			elif opt == "Configuración":
				self.showConfig()
			elif opt == "Test":
				self.showTest()
		else:
			if self.frameContent is None:
				if opt == "Principal":
					self.showPrincipal()
				elif opt == "Calendario":
					self.showCalendario()
				elif opt == "Tareas":
					self.showTareas()
				elif opt == "Configuración":
					self.showConfig()
				elif opt == "Test":
					self.showTest()

	def showConfig(self):
		self.frameContent = Frame(self.ventana, bg='gray')
		self.frameContent.grid(row=1, column=0, sticky="WE", padx = 5, pady = 5)
		self.principalLabel = Label(self.frameContent, text="Ventana de configuración.").grid(row=0, column=0, padx = 5, pady = 5)

	def showPrincipal(self):
		self.frameContent = LabelFrame(self.ventana, text="Plan semanal",bg='#2F2F2F')
		self.frameContent.grid(row=1, column=0, sticky="WE", padx = 5, pady = 5)
		#principalLabel = Label(self.frameContent, text="Bienvenido a la ventana principal de Crayfe Utilities.").grid(row=0, column=0, padx = 5, pady = 5)
		week = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
		dayOfWeek = datetime.datetime.today().weekday()
		i=0
		for day in week:
			if i == dayOfWeek:
				frameaux = LabelFrame(self.frameContent, text=day+':', bg='#2F2F2F', fg='#10EED3')
			else:
				frameaux = LabelFrame(self.frameContent, text=day+':', bg='#2F2F2F')
			frameaux.grid(row=0, column=i,sticky="WE", padx = 5, pady = 5)

			auxTest = Label(frameaux, text="Nada").grid(row=0, column=0, padx = 5, pady = 5)
			i+=1

	def showCalendario(self):
		self.frameContent = Frame(self.ventana, bg='#2F2F2F')
		self.frameContent.grid(row=1, column=0, sticky="WE", padx = 5, pady = 5)	
		#BLOQUE SELECCION
		frameSelect = LabelFrame(self.frameContent, text="Selección:", bg='#2F2F2F')
		frameSelect.grid(row=0, column=0,sticky="WE", padx = 5, pady = 5)
		box = StringVar()
		selec = ttk.Combobox(frameSelect, state="readonly", values=["Todo", "Cumpleaños", "Tareas", "Eventos"], textvariable=box).grid(row=0, column=0, padx = 5, pady = 5)
		ver = Button(frameSelect, text="Ver selección", bg='#431D5A').grid(row=0, column=1, columnspan=3,padx = 5, pady = 5)
		#BLOQUE para añadir nuevos elementos
		frameAppend = LabelFrame(self.frameContent, text="Añadir nuevo evento:", bg='#2F2F2F')
		frameAppend.grid(row=1, column=0,sticky="WE", padx = 5, pady = 5)
		listLabel = Label(frameAppend, text="Lista:", bg='#2F2F2F').grid(row=0, column=0, padx = 5, pady = 5)
		etiquetaLabel = Label(frameAppend, text="Etiqueta:", bg='#2F2F2F').grid(row=0, column=1, padx = 5, pady = 5)
		fechaLabel = Label(frameAppend, text="Fecha:", bg='#2F2F2F').grid(row=0, column=2, padx = 5, pady = 5)
		lista = StringVar()
		etiqueta = StringVar()
		fecha = StringVar()
		check_value = IntVar()
		textoLista = Entry(frameAppend, textvariable=lista, width="12", justify="center", bg='#ACACAC').grid(row=1, column=0, padx = 5, pady = 5)
		textoEtiqueta = Entry(frameAppend, textvariable=etiqueta, width="18",justify="center", bg='#ACACAC').grid(row=1, column=1, padx = 5, pady = 5)
		textoFecha = Entry(frameAppend, textvariable=fecha, width="6",justify="center", bg='#ACACAC').grid(row=1, column=2, padx = 5, pady = 5)
		checkTarea = Checkbutton(frameAppend, text = "Tarea", variable = check_value, onvalue = 1, offvalue = 0, bg='#2F2F2F').grid(row=2, column=0, padx = 5, pady = 5)
		submitActivity = Button(frameAppend, text="Añadir evento", bg='#431D5A', command=lambda l=lista, e=etiqueta, f=fecha, c=check_value: self.loadFromNewEvent(l, e, f, c)).grid(row=2, column=1, columnspan=2,padx = 5, pady = 5)
		#BLOQUE LISTA 1
		frameListador = LabelFrame(self.frameContent, text="Listado obtenido:", bg='#2F2F2F')
		frameListador.grid(row=0, column=1,rowspan=6, padx = 5, pady = 5)
		self.generateList(frameListador, True)
		#BLOQUE LISTA 2
		frameListador2 = LabelFrame(self.frameContent, text="Eventos pasados:", bg='#2F2F2F')
		frameListador2.grid(row=2, column=0, padx = 5, pady = 5)
		self.generateList(frameListador2, False)

	def showTareas(self):
		self.frameContent = LabelFrame(self.ventana, text="Lista de tareas:",bg='#2F2F2F')
		self.frameContent.grid(row=1, column=0, sticky="WE", padx = 5, pady = 5)
		frameListador = LabelFrame(self.frameContent, text="Listado obtenido:", bg='#2F2F2F')
		frameListador.grid(row=0, column=0,rowspan=6, padx = 5, pady = 5)
		self.generateTasks(frameListador)

	def showTest(self):
		self.frameContent = Frame(self.ventana, bg='gray')
		self.frameContent.grid(row=1, column=0, sticky="WE", padx = 5, pady = 5)
		principalLabel = Label(self.frameContent, text="Ventana de pruebas.").grid(row=0, column=0, padx = 5, pady = 5)
	def generateTasks(self, frame):
		i = 0
		tasks = self.data.getListaTareas()
		for aux in tasks:
			print(aux)
			auxframe = Frame(frame,bg='#2F2F2F')
			auxframe.grid(row=i, column=0, columnspan=6, sticky=S+N+E+W, padx = 15, pady = 3)
			check_value = IntVar()
			aux0 = Checkbutton(auxframe,text=aux[1], variable = check_value, onvalue = 1, offvalue = 0, bg='#2F2F2F', selectcolor="green").grid(row=0,column=0)
			i+=1
	def generateList(self, frame, forward):
		i=0
		list = self.data.getListaEventos()
		rd = self.data.getCuentaAtras()
		for aux in list:
			if forward:
				if not rd[i] < 0:
					cadena1=""
					cadena2=""
					tema="#FFF"
					if aux[2] == 'cumpleaños':
						tema = '#FFCFFD'
						cadena1 = " días para el"
						cadena2 = "de"
					elif aux[2] == 'examen':
						tema='#F5B430'
						cadena1 = " días para el"
						cadena2 = "de"
					elif aux[2] == 'tarea':
						tema = '#73D351'
						cadena1 = " días para finalizar la"
						cadena2 = ": "
					auxframe = Frame(frame,bg='#2F2F2F')
					auxframe.grid(row=1+i, column=0, columnspan=6, sticky=S+N+E+W, padx = 15, pady = 3)
					aux0 = Label(auxframe,text=str(rd[i]), fg='#FFF2B2', bg='#2F2F2F').grid(row=0,column=0)
					aux1 = Label(auxframe,text=cadena1, bg='#2F2F2F').grid(row=0,column=1)
					aux2 = Label(auxframe,text=aux[2],fg=tema, bg='#2F2F2F').grid(row=0,column=2)
					aux3 = Label(auxframe,text=cadena2, bg='#2F2F2F').grid(row=0,column=3)
					aux4 = Label(auxframe,text=aux[1], bg='#2F2F2F').grid(row=0,column=4)
					aux5 = Label(auxframe,text=aux[0].strftime("%d/%m"), fg='#10EED3', bg='#2F2F2F').grid(row=0,column=5)
			else:
				if rd[i] < 0:
					auxframe = Frame(frame, bg='#2F2F2F')
					auxframe.grid(row=1+i, column=0, columnspan=5, sticky=S+N+E+W, padx = 1, pady = 1)
					aux0 = Label(auxframe,text=aux[2]+" de", bg='#2F2F2F').grid(row=0,column=1, padx = 1, pady = 1)
					aux1 = Label(auxframe,text=aux[1], bg='#2F2F2F').grid(row=0,column=2, padx = 1, pady = 1)
					aux2 = Label(auxframe,text=aux[0].strftime("%d/%m"), bg='#2F2F2F').grid(row=0,column=3, padx = 1, pady = 1)
					aux3 = Label(auxframe,text="Hace "+str(-rd[i])+" días fue el", bg='#2F2F2F').grid(row=0,column=0, padx = 1, pady = 1)
			i+=1

	def loadFromNewEvent(self, lista, etiqueta, fecha, tarea):
		print(tarea.get())
		with open(lista.get(), 'a') as archivo:
			if tarea.get() ==0:
				archivo.write(etiqueta.get()+"		"+fecha.get()+"\n")
				mb.showinfo(title="Hecho", message="Se ha añadido con éxito el evento \""+etiqueta.get()+"\" con fecha: "+fecha.get()+" dentro de la lista \""+lista.get()+"\".")
			else:
				if fecha.get() is None:
					archivo.write('[ ] '+etiqueta.get()+"\n")
					mb.showinfo(title="Hecho", message="Se ha añadido con éxito la tarea \""+etiqueta.get()+"\" dentro de la lista \""+lista.get()+"\".")
				else:
					archivo.write('[ ] '+etiqueta.get()+"		"+fecha.get()+"\n")
					mb.showinfo(title="Hecho", message="Se ha añadido con éxito la tarea \""+etiqueta.get()+"\" dentro de la lista \""+lista.get()+"\".")
		archivo.close()
		