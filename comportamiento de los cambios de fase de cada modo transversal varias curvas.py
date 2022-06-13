import numpy as np
import matplotlib.pyplot as plt
 
#Indice de refraccion para el material se calcula a partir de la Ecuacion de Cauchy.

longwave=450;

#Coeficientes de Cauchy del BK7 son:
n_1=1.45800 ;
n_2=0.00354 ;
n_3=0;
#Coeficientes de Cauchy del SU8 son:
n_4=1.566;
n_5=0.00796;
n_6=0.00014;

n_2=n_1+(n_1)/(longwave**2)+(n_2)/(longwave**4)

n_3=n_4+(n_5)/(longwave**2)+(n_6)/(longwave**4)

n_aire= 1;   #Indice de refraccion del aire

n_r1=n_aire/n_2
n_r2=n_aire/n_3

#Para BK7

theta_p1 = np.arctan(n_r1)* 180/3.1415  #Angulo de polarizacion
theta_c1 = np.arcsin(n_r1)* 180/3.1415  #Angulo critico

theta_i_a1 = np.arange(0, theta_p1, 0.01)
theta_i_b1 = np.arange(theta_p1, theta_c1, 0.01)
theta_i_c1 = np.arange(theta_c1,90, 0.001)

phi_TE_a1 = 0*theta_i_a1
phi_TE_b1 = 0*theta_i_b1
phi_TE_c1 = -2*np.arctan((np.sqrt(np.sin(theta_i_c1*3.1415/180)**2-n_r1**2))/(np.cos(theta_i_c1*3.1415/180)))

phi_TM_a1 = 0*theta_i_a1
phi_TM_b1 = theta_i_b1/ theta_i_b1*3.1415
phi_TM_c1 = -2*np.arctan((np.sqrt(np.sin(theta_i_c1*3.1415/180)**2-n_r1**2))/(n_r1**2 *np.cos(theta_i_c1*3.1415/180)))+3.1415

#Para SU8

theta_p2 = np.arctan(n_r2)* 180/3.1415  #Angulo de polarizacion
theta_c2 = np.arcsin(n_r2)* 180/3.1415  #Angulo critico

theta_i_a2 = np.arange(0, theta_p2, 0.01)
theta_i_b2 = np.arange(theta_p2, theta_c2, 0.01)
theta_i_c2 = np.arange(theta_c2,90, 0.001)

phi_TE_a2 = 0*theta_i_a2
phi_TE_b2 = 0*theta_i_b2
phi_TE_c2 = -2*np.arctan((np.sqrt(np.sin(theta_i_c2*3.1415/180)**2-n_r2**2))/(np.cos(theta_i_c2*3.1415/180)))

phi_TM_a2 = 0*theta_i_a2
phi_TM_b2 = theta_i_b2/ theta_i_b2*3.1415
phi_TM_c2 = -2*np.arctan((np.sqrt(np.sin(theta_i_c2*3.1415/180)**2-n_r2**2))/(n_r2**2 *np.cos(theta_i_c2*3.1415/180)))+3.1415


#Graficos
plt.plot(theta_i_a1, phi_TE_a1, "-", color = 'g', lw = 3, label = '$\phi_{TE_{BK7}}$')
plt.plot(theta_i_b1, phi_TE_b1, "-", color = 'g', lw = 3)
plt.plot(theta_i_c1, phi_TE_c1, "-", color = 'g', lw = 3)

plt.plot(theta_i_a1, phi_TM_a1, "-", color = 'b', lw = 3, label = '$\phi_{TM_{BK7}}$')
plt.plot(theta_i_b1, phi_TM_b1, "-", color = 'b', lw = 3)
plt.plot(theta_i_c1, phi_TM_c1, "-", color = 'b', lw = 3)

linea1 = np.arange(0.0001, 3.14, 0.01)
linea2 = np.arange(-3.141592, -0.00001, 0.01)
x1 = theta_p1 * linea1 / linea1
plt.plot(x1, linea1, "--", color = 'g', lw=2)

x2 = theta_c1 * linea2 / linea2
plt.plot(x2, linea2, "--", color = 'b', lw=2)

plt.plot(theta_i_a2, phi_TE_a2, "-", color = 'y', lw = 4, label = '$\phi_{TE_{SU-8}}$')
plt.plot(theta_i_b2, phi_TE_b2, "-", color = 'y', lw = 4)
plt.plot(theta_i_c2, phi_TE_c2, "-", color = 'y', lw = 4)

plt.plot(theta_i_a2, phi_TM_a2, "-", color = 'r', lw = 3, label = '$\phi_{TM_{SU-8}}$')
plt.plot(theta_i_b2, phi_TM_b2, "-", color = 'r', lw = 3)
plt.plot(theta_i_c2, phi_TM_c2, "-", color = 'r', lw = 3)

x3 = theta_p2 * linea1 / linea1
plt.plot(x3, linea1, "--", color = 'y', lw=2)

x4 = theta_p2 * linea2 / linea2
plt.plot(x4, linea2, "--", color = 'r', lw=2)

plt.xlabel("$θ_i$")
plt.xlim(0,90)
plt.ylabel("$\Delta \phi$")
plt.rcParams["figure.figsize"]=(10,6)
plt.rcParams.update({'font.size':18})
plt.title("Comportamiento de los cambios de fase de cada modo transversal.", 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 12})
plt.legend()
