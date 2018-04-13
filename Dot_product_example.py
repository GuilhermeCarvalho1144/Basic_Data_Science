#==============================================================================
# O CODIGO IMPLEMENTA UM TESTE PARA DESMOSTAR A FACILIDADE DE SE TARBALHAR COM
# A BIBLIOTECA NUMPY PARA OPERAÇÕES VETORIAIS
# AUTOR : GUILHERME CARVALHO PEREIRA
# SOURCE: DEEP LEARNING PREREQUISITES: THE NUMPY STACK IN PYTHON...UDEMY COURSE
#==============================================================================
##INICIO
##IMPORTANDO AS BIBLIOTECAS
import numpy as np
from datetime import datetime 
#==============================================================================
#FUNÇÃO PARA CALCULAR O PRODUTO VETORIAL
def loop_form(x,y):
   ans = 0
   for a,b in zip(x,y):
      ans += a*b
   return ans
#==============================================================================
#DEFININDO AS VARIAVEIS
x = np.random.randn(100)
y = np.random.randn(100)
T = 100000
t_start = datetime.now()
#CALCULANDO O PRODUTO VETORIAL PELA FORMA DE LOOP
for t in xrange(T):
   loop_form(x,y)
dt1 = datetime.now() - t_start
#CALCULANDO O PRODUTO VETORIAL PELA BIBLIOTECA NUMPY
t_start = datetime.now()
for t in xrange(T):
   x.dot(y)
dt2 = datetime.now()- t_start
#MOSTRANDO O RESULTADO
print "dt1/dt2 ", dt1.total_seconds() / dt2.total_seconds()

