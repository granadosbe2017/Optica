#Coeficientes de Fresnel en una incidencia perpendicular para la interfaz agua-BK7

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
eta_inv=1/eta
#Intervalo del angulo de incidencia

grados = np.arange(0, 90, 0.02) 

raiz=np.sqrt(1-((eta*np.sin(grados))**2))

#Ecuacion del coeficiente de reflexion incidencia paralela

gamma_per=(eta_inv*np.cos(grados)-raiz)/(eta_inv*np.cos(grados)+raiz)

#Ecuacion del coeficiente de transmision incidencia paralela

tau_per=(2*eta_inv*np.cos(grados))/(eta_inv*np.cos(grados)+raiz)

#Grafico varias
plt.plot(gamma_per,color='y', label = "$\Gamma_{\perp}$")
plt.plot(tau_per,color='c', label = "$ τ_{\perp}$")
plt.legend()
plt.xlabel('Ángulo de incidencia (°)')
plt.ylabel('$Coeficientes$')
plt.title('Coeficientes de Fresnel en una incidencia perpendicular para la interfaz agua-BK7')
plt.xlim(0,90)
plt.ylim(-4,2)
plt.show()
