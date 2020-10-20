from Crypto.Util.number import *
from Crypto import Random
import Crypto
import libnum
import sys



bits=60
mensaje=input("Ingrese el mensaje: ")

#Definimos los numeros primos P y Q secretos
p = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Obtenemos nuestro primo P: ",p)
q = Crypto.Util.number.getPrime(bits, randfunc=Crypto.Random.get_random_bytes)
print("Obtenemos nuestro primo Q: ",q)
#Obtenemos el producto de los primos

n = p*q

PHI=(p-1)*(q-1)

#Definimos exponente verificador/llave publica
llave_publica=65537
print("Definimos nuestra llave publica: ",llave_publica)
#Obtenemos el exponente que firma / llave privada
llave_privada=(libnum.invmod(llave_publica, PHI))
print ("Obtenemos nuestra llave privada: ",llave_privada)

#Codigicamos el mensaje
Codificado=  bytes_to_long(mensaje.encode('utf-8'))
#Firmamos el mensaje
Mensaje_Firmado=pow(Codificado,llave_privada, n)
print ("Nuestro mensaje firmado :", Mensaje_Firmado)

#Se revisa la firma
revisado =pow(Mensaje_Firmado,llave_publica ,n)
print ("El resultado de la revision de la firma: ",long_to_bytes(revisado))

#Si res =  D entonces la firma es la misma.
if (revisado== Codificado):
    print("Los mensajes son iguales")
