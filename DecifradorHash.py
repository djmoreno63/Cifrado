import hashlib
#La biblioteca hash es una estructura de datos que permite realizar búsquedas rápidas en un conjunto de entradas
#Decifraremos un Hash con una lista de palabras

#Hash cifrado con Herramienta online
hash_file = "ecd2ec43c588ae012e3550fcc55d6009"

#Pediremos al usuario donde ingrese el diccionario
dic_file = input("Ingrese la direccion del archivo del diccionario")

#Le especificaremos cada palabra del diccionario con la variable del directorio
with open(dic_file, 'r') as file:

    #Hara la busqueda de la palabra y con el uso de ine.strip quita los espacion en blanco
    diccionario = [line.strip() for line in file]

    #Palabra a palabra calcularemos el hash de esa palabra
    for password in diccionario:

        #Como el hash esta cifrado en sha256 realizara el decifrado de esta manera
        hash_calculado == hashlib.sha256(password.encode()).hexdigest()
        
        if hash_calculado == hash_file:
            print("La contraseña original es: " + password)
            break
        else:
            print("La contraseña no se encuentra en el formulario")
