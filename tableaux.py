Procedure table ()

   entier n,m,i,t,y;
   entier tab[],tab1[],tab2[];

   ecrire ("saisir le nombre d'élément du premier tableau")
   lire(n)
   ecrire("saisir le nombre d'élément du second tableau")
   lire(m)

   pour i allant de 0 à n-1 && t allant de 0 à m-1    faire
           ecrire("donner l'élément du premier tableau")
           lire(tab[i])
           tab2[] = tab[i] 

           ecrire("donner l'élément du second tableau")
           lire(tab1[t])
           tab2[] = tab1[t]     
   fin pour
   
   pour t allant de 0 à m-1  faire
           pour y allant de 0 à (n+m)-1  faire
                       si tab2[t] < tab2[y] alors
                             tab1[t] = tab2[t]
                             tab2[t] = tab2[y]
                             tab2[y] = tab1[t]
                                   
                       fin si
            fin pour
   fin pour

fin table


Après analyse de l'agorithme précédent, nous dirons qu'il est 
de complexité quadratique ϴ(n^2) à cause de la boucle imbriquée