fichier = raw_input('nom du fichier > ')

f = open(fichier, 'r')

a = f.readlines()
a.pop(0)
a.pop(-1)

longueur = 0

for i in a:
	longueur += len(i[:-1])
	

print longueur
