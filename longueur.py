fichier1 = "1348_European_Black_Death_main_chromosome_2012.fasta"
fichier2 = "Yersinia_pestis_CO92.fasta"

f1 = open(fichier1, 'r')
f2 = open(fichier2, 'r')

def lon(f):
	a = f.readlines()
	a.pop(0)
	a.pop(-1)
	
	longueur = 0
	
	for i in a:
		longueur += len(i[:-1])
		
	return(longueur)
		
		
l1, l2 = lon(f1), lon(f2)
print 'longueur du chromosome au moyen age : ', l1
print 'longueur du chromosome mainetenant : ', l2

print 'difference de longueur entre avant et maintenant : ', l1 - l2
