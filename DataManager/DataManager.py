import re
from datetime import datetime, date

#función auxiliar para ordenar lista_eventos
def sortByDate(i):
    return (i[0].date()-date.today()).days

class DataManager:
    patron_tipo = '__+[A-ZÀ-ÿ]+__'
    patron_fecha = '[0-9]+/[0-9]+'
    patron_etiqueta = '[a-zA-ZÀ-ÿ\u00f1\u00d1]+'
    patron_tarea = '\[+[x]+\]|\[+[ ]+\]'
    fecha_actual = date.today()
    rd = []
    lista_eventos=[]
    lista_tareas=[]
    def __init__(self, l):
        
        for j in l:
            print("archivo abierto: ", j)
            contexto = j.lower()
            with open(j, 'r') as archivo:
                linea = archivo.readline()
                tipo = re.findall(self.patron_tipo, linea)
                print(tipo)
                if tipo is not None:
                    tipo = str(tipo).replace("__", "")
                    tipo = str(tipo).replace("['", "")
                    tipo = str(tipo).replace("']", "")
                    tipo = tipo.lower()
                    print(tipo)
                    while linea != '':
                        fecha = re.findall(self.patron_fecha, linea)
                        tarea = re.findall(self.patron_tarea, linea)
                        if len(fecha) == 1:
                            date_fecha = datetime.strptime(fecha[0]+'/'+str(self.fecha_actual.year), '%d/%m/%Y')
                            etiqueta = re.findall(self.patron_etiqueta, linea)
                            self.lista_eventos.append([date_fecha, etiqueta, tipo])
                        elif len(tarea) == 1:
                            etiqueta = re.findall(self.patron_etiqueta, linea)
                            if etiqueta[0] == 'x':
                                self.lista_tareas.append([True, etiqueta[1:], tipo])
                            else:
                                self.lista_tareas.append([False, etiqueta, tipo])
                        linea = archivo.readline()
            archivo.close()
        #Ordenamos la lista de eventos y calculamos la cuanta atrás en días
        self.lista_eventos.sort(key=sortByDate)
        i = 0
        for item in self.lista_eventos:
            self.rd.append(self.getRemainingDays(item[0]))
            i+=1

            
    def getListaEventos(self):
        return self.lista_eventos
    def getCuentaAtras(self):
        return self.rd
    def getListaEventosMasRd(self):
        return [self.lista_eventos, self.rd]

    def getListaTareas(self):
        return self.lista_tareas

    def printListaEventos(self):
        print("Lista de eventos:")
        for i in self.lista_tareas:
            print(i)

    def printListaTareas(self):
        print("Lista de tareas:")
        for i in self.lista_tareas:
        
            if i[0] == True:
                print("[x]"," ".join(i[1]))
            else:
                print("[ ]"," ".join(i[1]))

    def getRemainingDays(self, date):
        return int((date.date()-self.fecha_actual).days)

    
