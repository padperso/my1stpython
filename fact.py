#!/usr/bin/python
# ----test factorielle --- 

import sys


#print("NB arg : %d " % len(sys.argv)) 
if len(sys.argv) != 2:
    print("usage : %s <n> " % sys.argv[0] )
    sys.exit(1)

#recuperation du parametre
nParam = int(sys.argv[1])
nRes = 1
i=2
#calcul de !nParam
while (i <= nParam):
    nRes = nRes*i
    i    = i + 1

#affichage du resultat
print("factorielle(%d) = %d " % (nParam, nRes) )