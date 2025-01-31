from werkzeug.security import generate_password_hash, check_password_hash

#De werkzeug traeremos su subpaquete werkzeug.security importando: 
# generate_password_hash -> metodo que genera la encriptacion 
# check_password_hash -> metodo para comprobar si un valor cifrado coincide con uno original, antes de ser encriptado

#texto ya encriptado necesario para ser cifrado
texto = "x?1_P-1M.4!eM"

#metodo del algoritmo de encriptado, estos contiene datos de entrada junto a una clave 
#la idea es calcular la clace correcta generando datos cifrados como forma de salida usando el metodo generate_password_hash
#Primer metodo encriptado es necesario una cadena string para ser cifrado
texto_encriptado1 = generate_password_hash(texto)

#segundo metodo de encriptacion con segundo nivel de seguridad con metodologia sha256 para encriptar el valor
#El algoritmo SHA-256 es un algoritmo criptográfico que se usa para generar una huella digital única de un archivo o mensaje. 
texto_encriptado2 = generate_password_hash(texto, 'sha256')

#tercer metodo de encriptado con tercer nivel se le agrega la cantidad de iteraciones que se repetira el algoritmo 
# para realizar el cifrado con un valor mayor de seguridad
texto_encriptado3 = generate_password_hash(texto, 'sha256', 30)

print(texto_encriptado1)
print(texto_encriptado2)
print(texto_encriptado3)

#usando el metodo check_password_hash vamos a validar quela contraseña fue cifrada de un valor texto

#hara la comparacion a partir del texto inicial dada y el valor encriptada con el metodo texto_encriptado1
print(check_password_hash(texto_encriptado1, texto))
print(check_password_hash(texto_encriptado2, texto))
print(check_password_hash(texto_encriptado3, texto))


#Ejemplos tomados de 
# https://werkzeug.palletsprojects.com/en/2.0.x/utils/
