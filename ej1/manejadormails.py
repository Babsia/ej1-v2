import csv
from clasemail import email
class manejamail:
    __lista=[]
    def __init__(self):
        self.__lista=[]
    def crearlista(self):
        archivo = open('mails.csv')
        reader = csv.reader(archivo, delimiter=',')
        for fila in reader:
            mail3=email()
            mail3.crearCuenta(fila[0])
            self.__lista.append(mail3)
    def mostrar(self):
        print(self.__lista)
    def dominio(self,dom):
        cont=0
        for i in range (len(self.__lista)):
            if dom==self.__lista[i].getdom():
                cont+=1
        return cont
