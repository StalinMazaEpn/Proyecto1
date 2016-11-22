print('\t\t ESCUELA POLITECNCA NACIONAL')
print('INTEGRANTES:')
print('\t\t Edison Osorio')
print('\t\t Micha Cardenas')
print("\t\t Stalin Maza")
import sys
import math
                    #FUNCIONES DE LAS FIGURAS
def triangulo():
    print('\tTRIANGULO')
    lado=int(input('Ingrese la longitud del lado (base):\n'))
    altura=int(input('Ingrese la altura:\n'))
    area=(lado*altura)/2
    perimetro=lado*3
    print('El area del triangulo es: ',area)
    print('El perímetro del triángulo es: ',perimetro)

def cuadrado():
    print('\tCUADRADO')
    lado=int(input('Ingrese la longitud del lado: \n'))
    area=lado*lado
    perimetro=lado*4 
    print('El area del cuadrado es: ',area)
    print('El perímetro del cuadrado es: ',perimetro)

def pentagonoR():
    print("\tPENTAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))
    temp = perimetroF(5,lado,"Pentagono")
    areaF(temp,apotemaF(lado,5),"Pentagono")#calcula el area 
    
def hexagonoR():
    print("\tHEXAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))    
    temp = perimetroF(6,lado,"Hexagono")
    areaF(temp,apotemaF(lado,6),"Hexagono")#calcula el area

def heptagonoR():
    print("\tHEPTAGONO REGULAR")
    lado = int(input('Ingrese la longitud del lado: \n'))   
    temp = perimetroF(7,lado,"Heptagono")
    areaF(temp,apotemaF(lado,7),"Heptagono")#calcula el area

def octagono():
    print("\t OCTAGONO REGULAR")
#se puede calcular mediante el ángulo centra lo cual no sirve para sacar el apotema
    angulo_central=360/8
#ingresamos el lado 
    lado=int(input ("Ingrese el lado del octagono regular"))
#calculo del perimetro n *l
    perimetro=8*lado
    apotem=lado/(2*math.tan(angulo_central/2))
    area=lado= 4*lado*apotem

    print("el perimetro del octagono regular es",perimetro)
    print (" el apotema es ",apotem)
    print("el area es ",area)

def eneagono():
    lado=int(input ("Ingrese el lado del eneagono regular"))
    perimetro=lado*9
#Formula sacar el area de una figura de 9 lados
    area=9*(lado*lado)/(4 * math.tan(180/2))
    print("el perimetro del eneagono regular es",perimetro)
    print("el area es ",area)
def decagono ():
    lado=int(input ("Ingrese el lado del decagono regular"))
    perimetro=lado*10
#Formula sacar el area del decagono
    area=10*(lado*lado)/(4 * math.tan(180/10))
    print("el perimetro del decagonno regular es",perimetro)
    print("el area es ",area)
    
                        #OPERACIONES MATEMATICAS   
def perimetroF(NumL,LongL,nombre):
    per = NumL * LongL #calcula el perimetro
    print("El perímetro del ",nombre," es: ",per)
    return per

def areaF(per,apotema,nombre):    
    areaT = (per*apotema)/2  #calcula el area
    print("El area del ",nombre," es: ",areaT)
    return areaT

def apotemaF(lado,n):
    conversion = math.radians(360/n)
    tangente = math.tan(conversion/2)
    apot = lado/(2*tangente)  
    return apot
                        #MENU Y SWITCH    
def switch(NumLados):    
    if NumLados=='3':
        triangulo()
        repetir()
    elif NumLados=='4':
        cuadrado()
        repetir()
    elif NumLados == '5':   #aqui realizamos las opciones del switch de acuerdo a lo que escoga
        pentagonoR()        #a lo que escoga el usuario.
        repetir()
    elif NumLados == '6':
        hexagonoR()
        repetir()
    elif NumLados == '7':
        heptagonoR()
        repetir()
    elif NumLados == '8':
        octagono()
        repetir()
    elif NumLados == '9' :
        eneagono()
        repetir()
    elif NumLados =='10':
        decagono()
        repetir()
    else:
        print("¡¡ERROR!!..NUMERO DE LADOS DEBE ESTAR EN RANGO DE 3 A 10")
        menu()
        
def menu():
    NumLados =input('INGRESE EL # DE LADOS\n')   
    switch(NumLados) #Este es el que recibe el numero de lados    
            
def repetir():
    escoger = input("Ingrese S si desea continuar o N si desea salir\n")
    while escoger == "S" or escoger == "s":
        menu()   #aqui damos la opcion al usuario de si desea continuar en el programa
    print ("Programa Terminado")
    sys.exit()
    
def main():
    menu()    #llamamos a la funcion del menu

main()
