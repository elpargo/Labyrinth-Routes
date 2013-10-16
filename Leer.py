def leerArchivo(archivo_path):

	config_file = open(archivo_path,'r')

	result = config_file.readlines()

	result = [ i.replace('\n','') for i in result]
	lis=[]
	maze=[]
	cont=0
	inicio=[]
	final=[]
	tmp=''
	for i in result:
		if cont == 0:
			tmp=''
			for char in i:
				if char==" ":
					print tmp
					tmp=int(tmp)
					inicio.append(tmp)
					tmp=''
				else:	
					tmp+=char
			inicio.append(int(tmp))

		if cont == 1:
			tmp=''
			for char in i:
				if char==" ":
					final.append(int(tmp))
					tmp=''
				else:	
					tmp+=char
			final.append(int(tmp))

		if cont>=2:
			for char in i:
				if char=="1":
					lis.append(1)
				elif char=="0":
					lis.append(0)
			maze.append(lis)
			lis=[]
		cont+=1
	#aze = [ [1 if space  == "1" else 0 for space in i] for i in result ]
	
	return inicio,final,maze

