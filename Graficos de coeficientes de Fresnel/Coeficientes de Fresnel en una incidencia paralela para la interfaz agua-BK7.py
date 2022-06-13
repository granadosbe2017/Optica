#Coeficientes de Fresnel en una incidencia paralela para la interfaz agua-BK7

import numpy as np
import matplotlib.pyplot as plt

#Indice de refraccion se calcula a partir de la Ecuacion de Cauchy.

longwave=480;

#Parametros son:

n_1=1.45800;
n_2=0.00354;
n_3=0;

n_BK7=n_1+(n_1)/(longwave**2)+(n_2)/(longwave**4)

print('Indice de refraccion del medio es:')
print(n_BK7)

#Indice de refracción del agua es:

n_agua=1.3358   #a la misma longwave 

eta=n_agua/n_BK7    #eta=n_medio1/n_medio2

#Intervalo del angulo de incidencia

grados = np.arange(0, 90, 0.02) 

raiz=np.sqrt(1-((eta*np.sin(grados))**2))

#Ecuacion del coeficiente de reflexion incidencia paralela

gamma_para=(raiz-eta*np.cos(grados))/(eta*np.cos(grados)+raiz)

#Ecuacion del coeficiente de transmision incidencia paralela

tau_para=(2*np.cos(grados))/(eta*np.cos(grados)+raiz)

#Grafico varias
plt.plot(gamma_para,color='k', label = "$\Gamma_{||}$")
plt.plot(tau_para,color='g', label = "$ τ_{||}$")
plt.legend()
plt.xlabel('Ángulo de incidencia (°)')
plt.ylabel('$Coeficientes$')
plt.title('Coeficientes de Fresnel en una incidencia paralela para la interfaz agua-BK7')
plt.xlim(0,90)
plt.ylim(-2,2)
plt.show()

