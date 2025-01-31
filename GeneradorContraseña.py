import string
import random

#"importamos dos librerias"
#"Libreria STRING permite crear y personalizar el comportamiento de cadena utilizando la misma implementación en el texto"
#"Libreria RANDOM Ofrece generadores de números pseudo-aleatorios para varias distribuciones"

#"Creamos variable con nombre (tamaño) preguntara el tamaño de la contraseña"
tamaño = int(input("Ingrese el tamaño de la contraseña: "))

#"Creamos variable con nombre (digitos) asignando parametros:"
#"(ascii_letters = Letras Mayus/Minus) (digits = Genero digitos 1-9) (punctuation = Genera signos de puntuacion)"
digitos = string.ascii_letters + string.digits + string.punctuation

#"Creamos variable con nombre (contraseña) usamos .join para concatenar los caracteres aleatoriamente con Random"
#"Usamos ciclo for para estimar un tamaño dependiendo de la especificacion del usuario"
contraseña = "" .join(random.choice(digitos) for i in range(tamaño))

#"Imprimimos el resultado cifrado"
print("la contraseña cifrada es: " + contraseña)
