#!/usr/bin/env python
# coding: utf-8

# In[3]:


Estimation_1 = input('Entrez un numéro entre 1 et 100 : ')# première proposition du chiffre compris entre 1 & 100
Estimation_en_entier = int(Estimation_1)#Conversion en entier 
import random #accès à toutes les fonctions du module random
Choix_aleatoire = random.randint(1, 100)#renvoi d'un nombre entier tiré aléatoirement entre 0 inclus et 100 inclus
if Choix_aleatoire == Estimation_en_entier:
 print('Félicitations ! Vous avez deviné le numéro correctement')
else:
 print("Votre choix est incorrect")
n = 1
while Choix_aleatoire != Estimation_en_entier and n <= 2:
   Estimation_2= input('Entrez encore une fois un numéro entre 1 et 100 : ')
   n = n+1
   Estimation_en_entier = int(Estimation_2)
if Choix_aleatoire == Estimation_en_entier:
 print('Félicitations ! Vous avez deviné le numéro correctement')


# In[24]:


Estimation_1 = input('Entrez un numéro entre 1 et 100 : ')# première proposition du chiffre compris entre 1 & 100
Estimation_en_entier = int(Estimation_1)#Conversion en entier 
import random #accès à toutes les fonctions du module random
Choix_aleatoire = random.randint(1, 100)#renvoi d'un nombre entier tiré aléatoirement entre 0 inclus et 100 inclus
if Choix_aleatoire == Estimation_en_entier:
 print('Félicitations ! Vous avez deviné le numéro correctement')
else:
 print("Votre choix est incorrect")
while Choix_aleatoire != Estimation_en_entier and n<=2:
   Estimation_2= input('Entrez encore une fois un numéro entre 1 et 100 : ')
   n = n+1
   Estimation_en_entier = int(Estimation_2)
if Choix_aleatoire == Estimation_en_entier:
 print('Félicitations ! Vous avez deviné le numéro correctement')










# ##### 34

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


55

