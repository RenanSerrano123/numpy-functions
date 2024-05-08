F=input()
import numpy as np
A=float(input())
B=float(input())
C=float(input())
L=np.arange(A,B,C)
if F=="seno":
  seno=np.sin(L)
  print(*seno, sep=" ")
elif F=="cosseno":
  cosseno=np.cos(L)
  print(*cosseno, sep=" ")
elif F=="log10":
  log10=np.log10(L)
  print(*log10, sep=" ")
elif F=="log2":
  log2=np.log2(L)
  print(*log2, sep=" ")
else:
  print("funcao desconhecida")