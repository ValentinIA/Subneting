import os
# Esta funcion toma un numero y lo convierte a binario

def binario(num):

    # Calcula el binario por metodo de sacar modulos de 2

    num = int(num)
    binario = []

    while (num>0):
        resto = num%2
        binario.insert(0,resto)
        num = num // 2

    # Corrige la longitud del binario y que debe de tener 8 caracteres estrictos añadiendo 0s al principio

    lon = 8-int(len(binario))

    for i in range(lon):
        binario.insert(0,0)

    return binario

# Esta funcion pasa el numero en binario a decimal

def decimal(bin):
    
    l=8
    mi_ip = ""
    cont= 0

    # Divide la ip en octetos

    for i in range(0, len(bin), l):
        output= bin[i:i + l] 

        # Calcula el numero decimal sumando las portencias de 2 correspondientes

        a= 128
        for i in output:
            
            if i==0:
                pass
            else:
                cont= cont + a
            a = a/2

        cont= int(cont)
        mi_ip= mi_ip + str(cont) + "."
        cont = 0

    print(mi_ip[:-1])
    
    return mi_ip[:-1]

# Esta funcion pasa la Ip a binario 

def ip_bin(ip):

    nume = ""
    ipenbin=[]

    # Saca los numeros de la Ip separada por .

    for i in ip:

        if i!= ".":

            nume = nume + i 

        else:

            ipenbin+= binario(nume)
            nume = ""
    
    # Utiliza la funcion binarioo para convertir el numero

    ipenbin+= binario(nume)

    print("IP en binario :" + str(ipenbin))

    # En esta variable global se alamacena una lista con el binario de la Ip la acual se utilizara mas adelante

    global y
    y= ipenbin

    return ipenbin

 # Esta funcion clacula la mascara en decimal y binario

def masc(masc):

    masc = masc-1
    l_masc= []

    # Saca la Ip en binario

    for i in range(32):

        if i<=masc:
            l_masc.append(1)
        else:
            l_masc.append(0)
        
    print("Mascar :" + str(l_masc))

    # Saca la Ip en decimal con la funcion

    print("Ip Mascara :")
    decimal(l_masc)

    # En esta variable global se alamacena una lista con el binario de la mmascara la acual se utilizara mas adelante

    global x
    x= l_masc

# Esta funcion calcula la Ip de Red y la Primera de Host

def IpRed(m):

    # Este bucle hace el cambio necesario a la Ip para obtener la de Red con el binario donde x el la mascara e y es la Ip 

    for i in range(32):
        if x[i]==0:
            y[i]=0

    print("Ip Binario de Ip de Red :"+ str(y))
    print("Ip de red :")
    decimal(y)
    print("/"+str(m))
    

    # Esto  hacen el cambio necesario para obtener la Primera Ip de Host

    y[31]=1

    print(" ")
    print("Ip Binario de Primer Host :" + str(y))
    print("Ip de PrimerHost :")
    decimal(y)

# Esta funcion calcula la Ip de Broodcas y la Ultima de Host

def IpBroodcas():

    # Este bucle hace el cambio necesario a la Ip para obtener la de Broodcast con el binario donde x el la mascara e y es la Ip 

    for i in range(32):
        if x[i]==0:
            y[i]=1

    print("Binario de Ip de Broodcast :"+ str(y))
    print("Ip de broodcast :")
    decimal(y)

    # Este cambio es el necesario para obtener el Ultimo Host

    y[31]=0

    print(" ")
    print("Ip binario de Ultimo Host :" + str(y))
    print("Ip de Ultimo Host :")
    decimal(y)

# Esta funcion clacula el numero de host

def numhost(masc):

    cont=0

    for i in masc:
        if i==0:
            cont = cont + 1
    cont= 2**cont -2

    print("Numero de hosts :")
    print(cont)
    return cont

# Esta funcion invoca al resto para imprimir los resultados deseados

def interfaz(NumIp,Mascara):

    Mascara = int(Mascara)

    ip_bin(NumIp)
    print(" ")
    masc(Mascara)
    print(" ")
    IpRed(Mascara)
    print(" ")
    IpBroodcas()
    print(" ")
    numhost(x)

# Este bucle pide las variables al usuario y mantiene en bucle el programa

while True:
    try:
        print("Introduce la Ip :")

        NumIp = input()

        print(" ")

        print("Introduce numero de la mascara :")

        Mascara = input()

        print(" ")

        interfaz(NumIp,Mascara)

        print(" ")

        print("Si desea continuar escriba s y n para finalizar ejecucion")

        continuar= input()

        if continuar== "s":
            print("-------------------------------------------------------------------------------------------------------------------------------")
            pass
        else:
            break
    except:
        os.system ("cls") 
        print("Error en los datos")