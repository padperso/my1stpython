#!/usr/bin/python
# ----test factorielle --- 

import sys

# test du format de la ligne de commande
if len(sys.argv) != 2:
    print("usage : %s <n> " % sys.argv[0] )
    sys.exit(1)

#recuperation du parametre
nParam = int(sys.argv[1])

##################################
# calcul de factorielle de x 
##################################
def fact( x ):
   nRes = 1
   i=2
   #calcul de !nParam
   while (i <= nParam):
      nRes = nRes*i
      i    = i + 1
   return nRes

#affichage du resultat
nRes = fact( nParam )
print("factorielle(%d) = %d " % (nParam, nRes) )