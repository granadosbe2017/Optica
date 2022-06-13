## Coeficientes de Fresnel para la interfaz Aire-BK7  a 532 nm

import numpy as np
import matplotlib.pyplot as plt

# Indice de refraccion para el aire a 532 nm es:

n_aire=1.00027954;

#Indice de refraccion para el BK7 se calcula a partir de la Ecuacion de Cauchy.

longwave=532;

#Parametros son:

n_1=1.45800;
n_2=0.00354;
n_3=0;

n_BK7_532=n_1+(n_1)/(longwave**2)+(n_2)/(longwave**4)

print('Indice de refraccion de BK7 a 532 nm es:')
print(n_BK7_532)

#Calculo del indice de refraccion relativo

eta=n_BK7_532/n_aire

print('Indice de refraccion relativo es:')
print(eta)

theta_pol =np.arctan(eta)*(180/np.pi)
print('Angulo de polarización es:')
print(theta_pol)

#Intervalo del angulo de incidencia
grados = np.arange(0, 90, 0.02) 
#Angulo de transmision en terminos del angulo de incidencia 

raiz=np.sqrt(eta**2-(np.sin(grados))**2)

#Ecuacion del coeficiente de reflexion del modo TE

gammaTE_BK7_532=(np.cos(grados)-raiz)/(np.cos(grados)+raiz)

#Ecuacion del coeficiente de transmision del modo TE

tauTE_BK7_532=(2*np.cos(grados))/(np.cos(grados)+raiz)

#Ecuacion del coeficiente de reflexion del modo TM

gammaTM_BK7_532=(-(eta**2)*np.cos(grados)+raiz)/((eta**2)*np.cos(grados)+raiz)

#Ecuacion del coeficiente de transmision del modo TM

tauTM_BK7_532=(2*(eta**2)*np.cos(grados))/(raiz+(eta**2)*np.cos(grados))


#Grafico varias
plt.plot(gammaTE_BK7_532,color='c', label = "$\Gamma_{TE}$")
plt.plot(tauTE_BK7_532,color='m', label = "$ τ_{TE}$")
plt.plot(gammaTM_BK7_532,color='b', label = "$\Gamma_{TM}$")
plt.plot(tauTM_BK7_532,color='g', label = "$τ_{TM}$")
plt.legend()
plt.xlabel('Ángulo de incidencia (°)')
plt.ylabel('$Coeficientes$')
plt.xlim(0,90)
plt.ylim(-1,1)
plt.title('Comportamiento de los coeficientes de Fresnel a 532 nm.')
plt.show()