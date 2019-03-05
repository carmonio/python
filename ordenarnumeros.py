#!/usr/bin/env   pyhton
# __*__   coding:utf-8  __*__
def main():

	print ("ORDENAR 3 NÚMEROS")
	lista = []

	lista.append( int(input("Intruduzca el primer número: ")) )
	lista.append( int(input("Intruduzca el primer número: ")) )
	lista.append( int(input("Intruduzca el primer número: ")) )

	lista.sort()

	print(lista)

if __name__ == "__main__":
    main()

