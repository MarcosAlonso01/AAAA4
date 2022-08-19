"""with open("hola.txt", "r") as text:
    texto = text.read()
    print(texto)
    texto = text.readlines(5)
    print(texto)"""

from gettext import install
import numpy as np

#a = np.array([0, 1, 2, 3, 4])

#print(type(a))
#print(type(a.dtype))
#print(type(a.size))
#print(type(a.ndim))

#b =np.array([3.1, 11.02, 6.2, 213.2, 5.2])
#print(type(b))
#print(type(b.dtype))

#c =np.array([20, 1, 2, 3, 4])
#print(c)

#c[0]= 100
#print(c)

#c[4]= 0
#print(c)

#d = c[1:5]
#print(d)

#c[3:5] = 300, 400
#print(d)

#u=np.array([1, 0])
#v=np.array([0, 1])

#z= u+v

#print(z)

#for n, m in zip(u,v):
   
#    z.append(n+m)
#print(z)

#z = u-v

#print(z)

#Multiplicacion
#y =np.array([1,2])

#z = 2*y

#print(z)

#HADAMARD product

#u =np.array([1,2])
#v =np.array([3,2])

#z=u*v

#print(z)

#DOT product

#u = np.array([1, 2])
#v = np.array([3, 1])

#result= np.dot(u, v)

#print(result)

#Broadcasting
#u =np.array([1,2,3,-1])
#z= u+1
#print(z)

#Universal Function

#Average of the elements
#a =np.array([1,-1,1,-1])
#mean_a=a.mean()
#print(mean_a)

#Max Value
#b = np.array([1, 22, 3, 4, 5])
#max_b =b.max()
#print(max_b)

#map numpy arrays to new numpy array

#np.pi
#x =np.array([0, np.pi/2, np.pi])
#x= np.sin(x)
#print(x)

#a=np.linspace(-2, 2, num=9)
#print(a)

#b = np.dot(np.array([1,-1]),np.array([1,1]))
#print(b)

#Plotting a function

#x = np.linspace(0, 2*np.pi, 100)
#y= np.sin(x)

#import matplotlib.pyplot as plt

#print(plt.plot(x,y))

#print(np.__version__)



# 2 dimension arrays in Numpy

#a = [[11,12,13], [21,22,23], [31,32,33]]

#A= np.array(a)
#print(A)
#print(A.ndim)
#print(A.shape)
#print(A.size)

#user_number= int(input("Ingresa un numero del 0-2: "))
#user_number2= int(input("Ingresa un segundo numero del 0-2: "))
#print(A[user_number][user_number2])


#MINI API
"""
from nba_api.stats.static import teams
import pandas as pd
import numpy as np

nba_teams = teams.get_teams()


def one_dict(list_dict):
    keys= list_dict[0].keys()
    out_dict = {key:[] for key in keys}
    
    for dict_ in list_dict:
        for key, value in dict_.items():
            out_dict[key].append(value)
        return out_dict

dict_nba_team = one_dict(nba_teams)

df_teams = pd.DataFrame(dict_nba_team)
print(df_teams.head())

df_warriors = df_teams[df_teams['nickname']=='Warriors']
#print(df_warriors)

from nba_api.stats.endpoints import leaguegamefinder

gamefinder = leaguegamefinder.LeagueGameFinder(team_id_nullable=1610612737)

game =gamefinder.get_data_frames()[0]
print(game.head())
"""

a ={1,2,3,4,5,6}

print(a.append())