import socket

#Importamos la libreria socket ya que es un medio de comunicación entre nodos de una red

#inicialmente le preguntaremos la dirreccion ip a escanear al usuario
ip = input ("ingrese la direccion IP a escanear: ")

#Creamos un bucle for con la cantidad de puertos a escanear, lo haremos con todos (65535)
for puerto in range(1,65535):

#Creamos un socket como medio de comunicacion al puerto
#Al usar AF_INET especifica que estamos usando una dirreccion de red IPV4 
#Al usar SOCK_STREAM especifica que estamos utilizando el protocolo DHCP
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(5) #Establece un temporizador que ejecuta una función de 5 seg 

#Mediante el socket verificaremos que el puerto esta abierto o no, tratara de conectarse tanto a la IP como el Puerto que le especifiquemos
    result = soc.connect_ex((ip, puerto))

#Con la condicional IF si el resultado es 0 sera el puerto que este abierto de lo contrario estara cerrado10
    if result == 0:
        print("Puerto Abierto: " + str(puerto))
        soc.close()
    else:
        print("Puerto Cerrado: " + str(puerto))