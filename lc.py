#!/usr/bin/python

import sys

print('----bonjour monde --- ')

print("arg 0 : %s " % sys.argv[0])
print("arg 1 : %s " % sys.argv[1])

#recuperation du parametre
nParam = int(sys.argv[1])
nRes = 1
i=2
#calcul de !nParam
while (i <= nParam):
    nRes= nRes*i
    i = i + 1

print("fact(%d) = %d " % (nParam, nRes) )