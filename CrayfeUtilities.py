from DataManager import DataManager as dm
from FrameManager.Frames import Ventana_Principal as win_main
from tkinter import *
import sys

if len(sys.argv) > 1:
	root = Tk()
	print(sys.path[0])
	img = PhotoImage(file=sys.path[0]+'/logo.png')
	root.tk.call('wm', 'iconphoto', root._w, img)
	#root.geometry("1200x750")
	#root.configure(background='black')
	dataCollection = dm.DataManager(sys.argv[1:len(sys.argv)])

	v = win_main(root, dataCollection )
	root.mainloop()

else:
	print("Error: no se ha introducido ninguna lista. Tienes que pasar alguna lista para que la ventana lo pueda mostrar.")
