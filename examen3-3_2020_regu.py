# -*- coding: utf-8 -*-
"""
Created on Wed Jun 17 14:44:52 2020

@author: Hernandez Silverio Jenifer  15590696
         Mauricio Trejo Cecilia      16590106
"""
"""

 Fibonacci  <generadores>  30 pts

	Realice una generador que devuelva  de todos lo números de la
	serie fibonaci existentes de 0 hasta n-1 que 
	cumpla con el siguiente prototipo:
	
	def fibo(N):
		pass
	
	
	a = fibo(10)
	z = [e for e in a]
	print(z)
	# [0, 1 ,1 ,2 ]
"""
print ("\t**Fibonacci  <generadores>  30 pts** \n")
def fibo(N):
    a, b = 0,1
    while a < N:
        print(a, end=' ')
        a, b = b, a+b
		

a = fibo(3)
print()

print("----------------------------------------------------------------------------- \n")
"""
Patron332 <generadores> 20 pts
	
	Un montón de generos musicales usan el patron 3-3-2
	(Tango, Bachata, Bolero, Milonga, Salsa, Reegueton... )
	que es una manera de simplificar la secuencia de tonos 
	1,2,3,1,2,3,1,2.
	
	
	Explicación del patrón ritmico
	https://youtu.be/XU4P_65-OqU?t=186
	Complemento a la explicación
	https://youtu.be/htkI1ZDcOs0?t=58
	
	
	Defina un generador que reciba un numero entero positivo mayor a 0 N,
	dicho generador proporciona numero de 1 hasta N, correspondiente al patron
	con las siguientes condiciones:
	
	def p332(N):
		pass
		
	a = p332(10)
	z = [e for e in a]
	print(z)
	#[1,2,3,1,2,3,1,2,1,2]
"""
print ("\t**Patron332 <generadores> 20 pts** \n")
def p332(N):
    i = 1
    while i <= N:
        if i % 4 == 0 and i == 4 :
            yield 1 
        elif i % 5 == 0:
            yield 2
        elif i % 6 == 0:
            yield 3
        elif i % 7 == 0:
            yield 1
        elif i % 8 == 0:
            yield 2            
        elif i % 9 == 0:
           yield 1
        elif i % 10 == 0:
            yield 2
        else:
            yield i
        i = i + 1
		
a = p332(10)
z = [e for e in a]
print(z)

print("----------------------------------------------------------------------------- \n")

"""


Combinaciones <Comprensión de listas> 30pts

	Una exploradora y arqueologa quiere saber cuantas combinaciones de 
	herramientas de trabajo, supervivencia y comida puede realizar 
	a partir de un grupo de 5 herramientas trabajo (lupa; cepillo; 
	martillo y cincel; camara fotografica; o piqueta),      
	4 herramientas de supervivencia
	(lampara, pedernal, olla y cuchillo) y uno de 4 comidas
	posibles (Atun enlatado, frijoles enlatados, comida militar, carne seca)
	
	1) Obtenga una lista con todos los conjuntos posibles e imprimala en pantalla
	2) imprima un mensaje donde mencione la cantidad de conjuntos posibles
	
"""
print ("\t**Combinaciones <Comprension de listas> 30pts** \n")
A = ['lupa','cepillo','martillo','cincel','camara fotografica','piqueta']
B = ['lampara','pedernal','olla','cuchillo']
D = ['Atun enlatado','frijoles enlatados','comida militar','carne seca']

C = [[a,b,d] for a in A for b in B for d in D ]
print (C)
print("\nCantidad de Conjuntos posibles: ",len(C))

print("----------------------------------------------------------------------------- \n")
"""
    
¿Fedora?  <Comprensión de listas >  15 pts

	Del problema anterior imprima una lista que tenga todos las combinaciones
	que incluyen un atun enlatado y tambien despliegue su longitud
	
	
"""
print("\n**¿Fedora?  <Comprensión de listas >  15 pts** \n")
N = [ c for c in C if c[2]=='Atun enlatado']
print(N)
print("\nLongitud: ",len(N))

print("----------------------------------------------------------------------------- \n")

"""
<Monads>   30 pts

--Lacrimosa - Durch Nacht und Flut --   

Die Suche endet jetzt und hier
Gestein kalt und nass
Granit in Deiner Brust
Der Stein der Dich zerdrückt
Der Fels der Dich umgibt
Aus dem gehauen Du doch bist

Despiertate te busco
Mi corazon abreté te libro
Elevate mi luz y prende mi llama
Si a ti, yo se, te encontrare

El fragmento anterior es un canción del duo lacrimosa

Usando Monads obtenga la letra 
que menos se repite por cada linea y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""
print("\n** Monads --Lacrimosa - Durch Nacht und Flut --  30 pts**")
from functools import reduce


lis = ["""Die Suche endet jetzt und hier
Gestein kalt und nass
Granit in Deiner Brust
Der Stein der Dich zerdrückt
Der Fels der Dich umgibt
Aus dem gehauen Du doch bist
Despiertate te busco
Mi corazon abreté te libro
Elevate mi luz y prende mi llama
Si a ti, yo se, te encontrare"""]


def contar(e, l):
    v = 0
    for i in l:
        if e == i:
            v += 1
    return v + 1

def unicos(l):
    co = []
    c = []
    n = []
    if not l:
        return []
    p = l[0]
    for i in p:
        if not i in c:
            if i != ' ':
                if i != '\n':
                    c.append(i)
        else:
            n.append(i)

    for a in c:
        co.append(contar(a, n))
    v = reduce(lambda a,b: a + b, co)
    print('Probabilidad: 1 /',v)
    letras = list(zip(c, co))
    print('Letra que menos se repite',letras)
  
    return letras

s = unicos(lis)
f = filter(lambda a: a[1] == 1, s)
d = list(f)
print('\nLetra(s) con menos aparicion en el texto')
print('\n',d)

print("----------------------------------------------------------------------------- \n")
"""
<Monads>

--Hole in my soul apocalyptica--  20 pts

There's a hole in my heart, in my life, in my way
And it's filled with regret and all I did, to push you away
If there's still a place in your life, in your heart for me
I would do anything, so don't ask me to leave

I've got a hole in my soul where you use to be
You're the thorn in my heart and you're killing me
I wish I could go back and do it all differently
I wish that I'd treated you differently
'Cause now there's a hole in my soul where you use to be

El fragmento anterior es un canción del grupo apocalyptica

Usando Monads obtenga la letra 
que menos se repite de todo el fragmento y obtenga la probabilidad de sacar dicha
letra.

Nota: Pueden ayudarse de funciones recursivas y compresiones de lista. 

"""
print("\n** Monads --Hole in my soul apocalytica-- 20 pts **")
from functools import reduce


lis = ["""There's a hole in my heart, in my life, in my
     way And it's filled with regret and all I did, to push you away
    If there's still a place in your life, in your heart for me
    I would do anything, so don't ask me to leave
    I've got a hole in my soul where you use to be
    You're the thorn in my heart and you're killing me
    I wish I could go back and do it all differently
    I wish that I'd treated you differently
    'Cause now there's a hole in my soul where you use to be"""]


def contar(e, l):
    v = 0
    for i in l:
        if e == i:
            v += 1
    return v + 1

def unicos(l):
    co = []
    c = []
    n = []
    if not l:
        return []
    p = l[0]
    for i in p:
        if not i in c:
            if i != ' ':
                if i != '\n':
                    c.append(i)
        else:
            n.append(i)

    for a in c:
        co.append(contar(a, n))
    v = reduce(lambda a,b: a + b, co)
    print("Probabilidad: 1/",v)
    letras = list(zip(c, co))
    """print('Lista de letras que existen y cuantas veces se repite\n',letras)"""
  
    return letras

s = unicos(lis)
f = filter(lambda a: a[1] == 1, s)
d = list(f)
print("Letra(s) que menos se repite en todo el Fragmento: \n", d)



