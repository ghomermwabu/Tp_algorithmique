Structure Cercle
       Entier x
       Entier y
       Entier R
Fin Structure

Fonction cercleSecante (): entier

       Cercle c1,c2;

       ecrire("Saisir le point du centre du premier cercle")
       lire(c1.x,c1.y)
       ecrire("saisir son rayon")
       lire(c1.R)

       ecrire("saisir le point du centre du second cercle")
       lire(c2.x,c2.y)
       ecrire("saisir le rayon")
       lire(c2.R)

              si  SQRT(SQR(c2.x-c1.x) + SQR(c2.y-c1.y)) > 0 && SQRT(SQR(c2.x-c1.x) + SQR(c2.y-c1.y)) < c1.R+c2.R  alors
                             retourner 1
              sinon
                             retourner 0
              fin si
              
Fin cercleSecante


Nous dirons que la complexité de cet algorithme est constante ϴ(1)
car si nous additionnons toutes les opérations de lecture, de comparaison 
(dans la condition afin de calculer la distance entre les points de deux centres) 
d'affichage et de retour. Nous aurons une constante