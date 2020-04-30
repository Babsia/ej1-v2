import re
class email:
    __idcuenta=''
    __dominio=''
    __tipodom=''
    __pass=''
    def __init__(self,id="",dom="",tipdom="",cont=""):
        self.__idcuenta=id
        self.__dominio=dom
        self.__tipodom=tipdom
        self.__pass=cont
    def retornamail(self):
        cadenas = self.__idcuenta + '@' + self.__dominio + '.' + self.__tipodom
        return cadenas

    def getdom(self):
       return self.__dominio
    def retornacontra (self):
        return self.__pass
    def setpass (self,new):
        self.__pass=new
        print("{}".format(self.__pass))

    def crearCuenta(self, correo,pass2=''):
        grupo = re.search(r'([a-zA-Z0-9/-_]+)@([a-zA-Z0-9/-]+).([a-z]+)', correo)
        if (type(grupo)==re.Match):
            self.__idcuenta=grupo.group(1)
            self.__dominio=grupo.group(2)
            self.__tipodom=grupo.group(3)
            self.__pass=pass2
        else:
            print("usted ingreso un correo invalido")


