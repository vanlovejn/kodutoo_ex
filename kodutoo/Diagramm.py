import numpy as np
import matplotlib.pyplot as plt

file=open("Kodutöö/data.txt","r")
mas1=[]
mas2=[]
for line in file:
    n=line.find(",")
    mas1.append(line[0:n].strip())
    mas2.append(line[n+1:len(line)].strip())
file.close()
title = "IKT turvameetodite kasutamise osatähtsus ettevõttes, 2018"

fig, ax = plt.subplots(ncols=1)
fig.canvas.set_window_title(title)
fig.suptitle(title +
             "https://vana.stat.ee/pressiteade-2019-111")

ax.set_xlabel("%")
ax.set_ylabel("Nimi")

plt.barh(mas1, mas2, 0.7, color="#b32b0e")

plt.show()
