rm(list=ls())
tab = read.table("mart_export.txt", h=T)

tab2 = cbind(tab[tab$Chromosome.Name.humain==1,1 ], tab[tab$Chromosome.Name.humain==1,5])

plot(tab2[,1]/10^7, tab2[,2]/10^7, cex=0.1, xlab='HS', ylab='PH')

tab3 = tab2[order(tab2[,1]),]



tab3[ tab3[,1] == unique(tab3[,1])[1], 2]
tab_unique = unique(tab3[,1])

for (i in length(tab_unique)){
  
}