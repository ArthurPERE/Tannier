import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt

n = 100
k = 50


def signe(i):
	if i < 0:
		return -1
	else:
		return 1


def tore(i):
	if i==0:
		return -1
	if i==n+1:
		return 0
	return i-1


debut = range(1,n+1)*np.random.choice([-1,1], size=n)
rand = np.random.randint(n, size=(2,k))

inverse = np.array(debut)
memoire = []
# Inversion du genome
for i in xrange(k):
	a = min(rand[0,i], rand[1,i])
	b = max(rand[0,i], rand[1,i])

	if a != b:
		for j in xrange(a,b):
			inter = inverse[a:b][::-1]*(-1)

		memoire.append(list(inter))
		inverse[a:b] = inter


print len(memoire)


# nombre d'adjacence commune
adjacent = 0
for i in xrange(-1,n-1):
	a, b = inverse[i], inverse[i+1]

	if abs(a) == 1 and abs(b) == n:
		if debut[1] == a and debut[-1] == b:
			adjacent += 1

	if abs(a)+1 == abs(b):
		if a == debut[abs(a)-1] and b == debut[abs(b)-1]:
			adjacent +=1 


print adjacent



graph = {}
for i in xrange(1,n+1):
	graph[i] = [[],[]]


for i in xrange(1,n+1):
	d = debut[i-1]
	j = inverse[i-1]

	graph[i][0] = [abs(debut[tore(abs( d-1 ))]), abs(debut[tore(abs( d+1 ))])]
	graph[abs(j)][1] = [ abs(inverse[tore(abs(i*signe(j)-1))]), abs(inverse[tore(abs(i*signe(j)+1))]) ]
	
	
r = range(1,n+1)

print graph

compteur_cycle = 0
while len(r) != 0:
	i=r[0]
	r.remove(i)

	z = graph[i][0][1]
	compteur = 0
	while z in r:
		compteur += 1
		r.remove(z)
		z = graph[z][compteur%2][0]

	compteur_cycle += 1




print compteur_cycle