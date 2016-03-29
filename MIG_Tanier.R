rm(list=ls())
tab = read.table("mart_export.txt", h=T)

tab2 = cbind(tab[tab$Chromosome.Name.humain==1,1 ], tab[tab$Chromosome.Name.humain==1,5])

plot(tab2[,1], tab2[,2], cex=0.1, xlab='HS', ylab='PH')

tab3 = tab2[order(tab2[,1]),]




coeff = function (x, y){
  k = (x[2] - y[2]) / (x[1] - y[1])
  b = x[2] - x[1] * k
  return(cbind(b, k))
}

distance = function (x, b, k){
  return(abs(k*x[1]-x[2]+b)/sqrt(2))
}

bruit = function (x){
x_unique = unique(x[,1])
resultat = matrix(NA, nrow=length(x_unique), ncol=2)

coefficient = NULL
compteur = 0
for (i in 1:length(x_unique)){
  
  if (length(coefficient) == 0){
    
    a = x[ x[,1]==x_unique[i], ]; a = matrix(a, ncol=2)
    b = x[ x[,1]==x_unique[i+100], ]; b = matrix(b, ncol=2)
    
    for (e in 1:length(a[,1])){ for (f in 1:length(b[,1])){ d = coeff(a[e,], b[f,])
        if ( abs(d[2]-1)<0.1 ){
          coefficient = c(d[1], 1)
          break
        }
        if (abs(d[2]+1)<0.1 ){
          coefficient =c( d[1], -1)
          break
        }
    }}
    
  }
  
  else{
    a = x[ x[,1]==x_unique[i], ]; a = matrix(a, ncol=2)
    boucle = F
    for (e in 1:length(a[,1])){
    if (distance(a[e,], coefficient[1], coefficient[2])<=1){
      resultat[i, ] = a[e,]
      boucle = T
      compteur = 0
      break
    }}
    if (boucle == F){ compteur = compteur + 1 }
  }
  
  if (compteur == 10){ coefficient = NULL; i = i-10 } 
  
}


return(resultat)
}


bruit(tab3)



