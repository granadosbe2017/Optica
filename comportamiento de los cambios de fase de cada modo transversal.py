import numpy as np
import matplotlib.pyplot as plt
 
#Indice de refraccion para el material se calcula a partir de la Ecuacion de Cauchy.

longwave=450;

#Coeficientes de Cauchy son:
n_1=1.566;
n_2=0.00796;
n_3=0.00014;

n_2=n_1+(n_1)/(longwave**2)+(n_2)/(longwave**4)

print('_________________________________')
print('Indice de refraccion del material es: \n')
print("{:.4f}".format(n_2))
print('_________________________________')

n_aire= 1;   #Indice de refraccion del aire

#Indice de refraccion relativo
n_r=n_aire/n_2
print('Indice de refraccion relativo es: \n')
print("{:.4f}".format(n_r))
print('_________________________________')

theta_p = np.arctan(n_r)* 180/3.1415  #Angulo de polarizacion
theta_c = np.arcsin(n_r)* 180/3.1415  #Angulo critico

print('Angulo de polarizacion es: \n')
print("{:.4f}".format(theta_p))
print('_________________________________')
print('Angulo critico es: \n')
print("{:.4f}".format(theta_c))
print('_________________________________')

#Intervalos de los angulos

theta_i_a = np.arange(0, theta_p, 0.01)
theta_i_b = np.arange(theta_p, theta_c, 0.01)
theta_i_c = np.arange(theta_c,90, 0.001)

#Iniciadores de las fases

phi_TE_a = 0*theta_i_a
phi_TE_b = 0*theta_i_b
phi_TE_c = -2*np.arctan((np.sqrt(np.sin(theta_i_c*3.1415/180)**2-n_r**2))/(np.cos(theta_i_c*3.1415/180)))


phi_TM_a = 0*theta_i_a
phi_TM_b = theta_i_b/ theta_i_b*3.1415
phi_TM_c = -2*np.arctan((np.sqrt(np.sin(theta_i_c*3.1415/180)**2-n_r**2))/(n_r**2 *np.cos(theta_i_c*3.1415/180)))+3.1415

#Graficos
plt.plot(theta_i_a, phi_TE_a, "-", color = 'green', lw = 4, label = '$\phi_{TE}$')
plt.plot(theta_i_b, phi_TE_b, "-", color = 'green', lw = 4)
plt.plot(theta_i_c, phi_TE_c, "-", color = 'green', lw = 4)

plt.plot(theta_i_a, phi_TM_a, "-", color = 'blue', lw = 4, label = '$\phi_{TM}$')
plt.plot(theta_i_b, phi_TM_b, "-", color = 'blue', lw = 4)
plt.plot(theta_i_c, phi_TM_c, "-", color = 'blue', lw = 4)

linea1 = np.arange(0.0001, 3.14, 0.01)
linea2 = np.arange(-3.141592, -0.00001, 0.01)
x1 = theta_p * linea1 / linea1
plt.plot(x1, linea1, "--", color = 'blue', lw=2)

x2 = theta_c * linea2 / linea2
plt.plot(x2, linea2, "--", color = 'green', lw=2)

plt.xlabel("$θ_i$")
plt.xlim(0,90)
plt.ylabel("$\Delta \phi$")
plt.rcParams["figure.figsize"]=(10,6)
plt.rcParams.update({'font.size':18})
plt.title("Comportamiento de los cambios de fase de cada modo transversal para SU-8.", 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 12})
plt.text(32, -0.5, "$θ_p$", fontsize=19, rotation = 0)
plt.text(38.1, -3.3, "$θ_c$", fontsize=19, rotation = 0)
plt.legend()
