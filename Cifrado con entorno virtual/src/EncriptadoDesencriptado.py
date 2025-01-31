from cryptography.fernet import Fernet


#Importamos la libreria cryptography.fernet importamos la clase fernet

texto = "x?1_P-1M.4!eM"

# Genera una clave en formato de secuencia de bytes:
key = Fernet.generate_key()
# Creamos un objeto cifrado
objeto_cifrado = Fernet(key)
# Creamos un texto cifrado = al objeto encriptado
#encode: codifica el objeto string que le estemos pasando 
texto_encriptado = objeto_cifrado.encrypt(str.encode(texto))
#imprime el texto encriptado
print(texto_encriptado)

#Texto desencriptado en Bytes 
texto_desencriptado_bytes = objeto_cifrado.decrypt(texto_encriptado)
# Inprimimos la variable
print(texto_desencriptado_bytes)
# podemos decodificar el valor anterior
texto_desencriptado = texto_desencriptado_bytes.decode()
print(texto_desencriptado)
# Con type podemos asegurar la variable que se asigno 
print(type(texto_desencriptado))

# Ejemplo tomado de
# https://cryptography.io/en/latest/fernet/