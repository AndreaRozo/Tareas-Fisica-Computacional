#Tarea 2 - Física Computacional
#Andrea Rozo Méndez
#201015972

#Se revisan los argumentos del programa
import sys
if (len(sys.argv) ==2):
	#Se lee el archivo de entrada
	archivoEntrada = open('%s'% sys.argv[1], 'r')

	#Se carga todo el texto del archivo de entrada
	texto = archivoEntrada.read()

	#Verificación de la validez de los caracteres

	x=len(texto)
	caracteresValidos = []
	frecuencias = []
	invalidos = [" ",".",",",";",":","\n","\r","_","-","/","?","!","{","}","[","]","(",")","'",'"',"<",">","+","#","$","%","&","=","°","|","¬","*","@","~","^","`","¨","´","¿","¡"]
	
	for i in range (x):
		y = texto[i]
		valido = 1
		
		if(y in invalidos):
			valido = 0

		if (valido):
			agregar = True
			for j in range (len(caracteresValidos)):
				if(y == caracteresValidos[j]):
					agregar = False
			if (agregar == True):
				caracteresValidos.append(y)

	for i in range (len(caracteresValidos)):
		z = caracteresValidos[i]
		frecuencias.append(0)
		for j in range (x):
			y = texto[j]
			if (z == y):
				frecuencias[i] = frecuencias[i]+1


	for i in range (len(frecuencias)):
		for j in range (i,len(frecuencias)):
			primero = frecuencias[i]
			posicion = i
			if(primero < frecuencias[j]):
				primero = frecuencias[j]
				posicion = j
			temp1 = frecuencias[i]
			temp2 = caracteresValidos[i]
			frecuencias[i] = primero
			caracteresValidos[i] = caracteresValidos[posicion]
			frecuencias[posicion] = temp1
			caracteresValidos[posicion] = temp2
	
	total = sum(frecuencias)
	for i in range (len(frecuencias)):
		frecuencias[i] = float(frecuencias[i])/total*100

	archivoEntrada.close()
	
	#Generación del archivo de salida

	archivoSalida = open('frecuencias_%s'%sys.argv[1]+'.txt','w')
	for i in range (len(caracteresValidos)):
		archivoSalida.write('%s       %.6f  %s\n' % (caracteresValidos[i], frecuencias[i],chr(0x25)))

	archivoSalida.close()
else:
	print "Este programa necesita un parametro"