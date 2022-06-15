#!/usr/bin/env python
# coding: utf-8

# #### Comportamiento de los cambios de fase en la Reflexión Interna Total

# In[2]:


#Cargamos las librerias que se van a utilizr
import numpy as np
import matplotlib.pyplot as plt


# ##### Ecuación de Cauchy para el calculo del indice de refraccion del medio
#  $$\eta = n_{1} + \frac{n_{2}}{\lambda^2} + \frac{n_{3}}{\lambda^4}$$

# In[15]:


#Indice de refraccion para el material se calcula a partir de la Ecuacion de Cauchy.

longwave=450;

#Coeficientes de Cauchy del medio son:

n_1=1.566;
n_2=0.00796;
n_3=0.00014;

#Ecuacion

n_2=n_1+(n_2)/(longwave**2)+(n_3)/(longwave**4)

print('_____________________________________')
print('Indice de refraccion del material es: \n')
print("{:.4f}".format(n_2))
print('_____________________________________')


# ### El indice de refraccion relativo se obtiene a partir de la siguiente expresion:
# $$\eta_{r} = \frac{\eta_{1}}{\eta_{2}}$$
# ### que en nuestro caso sería:
#  $$\eta_{r}=\frac{\eta_{aire}}{\eta_{2}}$$
#  

# In[4]:


#Calculo del indice de refraccion relativo 
n_aire= 1;   #Indice de refraccion del aire

#Indice de refraccion relativo

n_r=n_aire/n_2

print('_________________________________')
print('Indice de refraccion relativo es: \n')
print("{:.4f}".format(n_r))
print('_________________________________')


# ### Angulos de polarizacion y critico
# ##### El ángulo de polarización se obtiene a partir de
# $$\theta_{p}=tan^{-1}\eta_{r}$$ $$(rad)$$ 
# ##### El ángulo crítico estara dado por 
# $$\theta_{c}=sen^{-1}\eta_{r}$$ $$(rad)$$
# 

# In[5]:


#Angulos de polarizacion y critico

theta_p = np.arctan(n_r)* 180/3.1415  #Ecuacion para Angulo de polarizacion

theta_c = np.arcsin(n_r)* 180/3.1415  #Ecuacion para Angulo critico

print('_________________________________')
print('Angulo de polarizacion es: \n')
print("{:.4f}".format(theta_p))
print('_________________________________')
print('Angulo critico es: \n')
print("{:.4f}".format(theta_c))
print('_________________________________')


# ### Intervalos de los cambios de fase de cada modo transversal
# 
# ##### Para el modo transversal eléctrico TE: 
# $$\theta < \theta_{c}$$
# $$\theta > \theta_{c}$$ 
# ##### Para el modo transversal magnético TM:
# $$\theta < \theta_{p}$$
# $$\theta_{p}<\theta < \theta_{c}$$
# $$\theta > \theta_{c}$$

# In[6]:


# Con la función arange definimos los intervalos 

theta_i_a = np.arange(0, theta_p, 0.01)     #intervalo 0 a angulo de polarizacion
theta_i_b = np.arange(theta_p, theta_c, 0.01)    #intervalo entre angulo de polarizacion y critico
theta_i_c = np.arange(theta_c,90, 0.001)    #intervalo cuando el angulo es mayor al critico


# ##### Ecuaciones del comportamiento de cambio de fase de los modos transversales en reflexión interna total
# ##### Para el modo TE:
# ###### Cuando $$\theta < \theta_{c}$$ el $$\phi_{TE}=0$$ y cuando $$\theta>\theta_{c}$$ entonces el $$\phi_{TE}=-2 tan^{-1}\left(\frac{\sqrt{sen^2\theta -\eta_{r}^2}}{cos\theta}\right)$$
# ##### Para el modo TM:
# ###### Ahora, cuando $$\theta < \theta_{p}$$ el $$\phi_{TM}=0$$ cuando $$\theta_{p}<\theta<\theta_{c}$$ el $$\phi_{TM}= \pi$$ y finalmente cuando $$\theta>\theta_{c}$$ $$\phi_{TM}=-2 tan^{-1}\left(\frac{\sqrt{sen^2\theta -\eta_{r}^2}}{\eta_{r}^2 cos\theta}\right) + \pi$$

# #### Edicion del grafico de los cambios de fase 
# 

# In[18]:


#ecuaciones de las cambios de fase

#Modo TE
phi_TE_a = 0*theta_i_a
phi_TE_b = 0*theta_i_b
phi_TE_c = -2*np.arctan((np.sqrt(np.sin(theta_i_c*3.1415/180)**2-n_r**2))/(np.cos(theta_i_c*3.1415/180)))
#Modo TM
phi_TM_a = 0*theta_i_a
phi_TM_b = theta_i_b/ theta_i_b*3.1415
phi_TM_c = -2*np.arctan((np.sqrt(np.sin(theta_i_c*3.1415/180)**2-n_r**2))/(n_r**2 *np.cos(theta_i_c*3.1415/180)))+3.1415


# In[19]:


# Para realizar la curva del comportamiento del cambio de fase del modo TE en la RTI

plt.plot(theta_i_a, phi_TE_a, "-", color = 'g', lw = 4, label = '$\phi_{TE}$')
plt.plot(theta_i_b, phi_TE_b, "-", color = 'g', lw = 4)
plt.plot(theta_i_c, phi_TE_c, "-", color = 'g', lw = 4)

# Para realizar la curva del comportamiento del cambio de fase del modo TM en la RTI

plt.plot(theta_i_a, phi_TM_a, "-", color = 'b', lw = 4, label = '$\phi_{TM}$')
plt.plot(theta_i_b, phi_TM_b, "-", color = 'b', lw = 4)
plt.plot(theta_i_c, phi_TM_c, "-", color = 'b', lw = 4)

#linea del angulo polarizacion

linea1 = np.arange(0.0001, 3.14, 0.01)
x1 = theta_p * linea1 / linea1
plt.plot(x1, linea1, "--", color = 'b', lw=2)  #linea del angulo polarizacion

#linea del angulo critico

linea2 = np.arange(-3.141592, -0.00001, 0.01)
x2 = theta_c * linea2 / linea2
plt.plot(x2, linea2, "--", color = 'g', lw=2) 

plt.xlim(0,90)

plt.ylabel("$\Delta \phi$")
plt.xlabel("$(°)$")

plt.rcParams["figure.figsize"]=(10,6)    #tamaño de la fuente del texto de las leyenas
plt.rcParams.update({'font.size':18})

#Estilo del titulo del grafico

plt.title("Comportamiento de los cambios de fase de cada modo transversal para SU-8.", 
          fontdict={'family': 'serif', 
                    'color' : 'darkblue',
                    'weight': 'bold',
                    'size': 12})  

#Etiquetas

plt.text(32, -0.5, "$θ_p$", fontsize=19, rotation = 0)
plt.text(38.1, -3.3, "$θ_c$", fontsize=19, rotation = 0)
plt.legend()


# #### Comportamiento del cambio de fase en RTI de varios materiales

# In[14]:


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
plt.xlabel("$(°)$")
plt.xlim(0,90)
plt.ylabel("$\Delta \phi$")
plt.rcParams["figure.figsize"]=(10,6)
plt.rcParams.update({'font.size':18})
plt.title("Comportamiento de los cambios de fase de cada modo transversal.", 
          fontdict={'family': 'serif', 
                    'color' : 'black',
                    'weight': 'bold',
                    'size': 12})
plt.legend()


# In[ ]:




