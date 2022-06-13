## Coeficientes de Fresnel para la interfaz Aire-PMMA a 480 nm

import numpy as np
import matplotlib.pyplot as plt
 
# Indice de refraccion para el aire a 480 nm es:

n_aire=1.00027954;

#Indice de refraccion para el PMMA se calcula a partir de la Ecuacion de Cauchy.

longwave=480;

#Parametros son:

n_1=1.479;
n_2=0.00548;
n_3=0.000172;

n_PMMA_480=n_1+(n_1)/(longwave**2)+(n_2)/(longwave**4)

print('Indice de refraccion de PMMA a 480 nm es:')
print(n_PMMA_480)

#Calculo del indice de refraccion relativo

eta=n_PMMA_480/n_aire

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

gammaTE_PMMA_480=(np.cos(grados)-raiz)/(np.cos(grados)+raiz)

#Ecuacion del coeficiente de transmision del modo TE

tauTE_PMMA_480=(2*np.cos(grados))/(np.cos(grados)+raiz)

#Ecuacion del coeficiente de reflexion del modo TM

gammaTM_PMMA_480=(-(eta**2)*np.cos(grados)+raiz)/((eta**2)*np.cos(grados)+raiz)

#Ecuacion del coeficiente de transmision del modo TM

tauTM_PMMA_480=(2*(eta**2)*np.cos(grados))/(raiz+(eta**2)*np.cos(grados))

#Grafico varias
plt.plot(gammaTE_PMMA_480,color='b', label = "$\Gamma_{TE}$")
plt.plot(tauTE_PMMA_480,color='r', label = "$ τ_{TE}$")
plt.plot(gammaTM_PMMA_480,color='g', label = "$\Gamma_{TM}$")
plt.plot(tauTM_PMMA_480,color='y', label = "$τ_{TM}$")
plt.legend()
plt.xlabel('Ángulo de incidencia (°)')
plt.ylabel('$Coeficientes$')
plt.title('Comportamiento de los coeficientes de Fresnel a 480 nm.')
plt.xlim(0,90)
plt.ylim(-1,1)
plt.show()