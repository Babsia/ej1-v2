from clasemail import email
from manejadormails import manejamail
import csv

if __name__ == '__main__':
    conta = 0
    x = input("ingrese el id: ")
    y = input("ingrese el dominio: ")
    z = input("ingrese el tipo de dominio: ")
    contra = input("ingrese la contraseña: ")
    nom = input("ingrese el nombre: ")
    mail = email(x, y, z, contra)
    print("estimado {} le enviaremos un mensaje a la direccion: ".format(nom), mail.retornamail())
    contra = input("ingrese la contraseña actual: ")
    if contra == mail.retornacontra():
        newpass = input("ingrese su nueva contraseña: ")
        mail.setpass(newpass)



    else:
        print("contraseña incorrecta")
obj2 = input("ingrese una mail: ")
pass2 = input("ingrese una contraseña")
mail2 = email()
mail2.crearCuenta(obj2, pass2)
dom = input("ingrese un dominio: ")
l=manejamail()
l.crearlista()
x=l.dominio(dom)
print("la cantidad de mails con ese dominio es de : {}".format(x))
