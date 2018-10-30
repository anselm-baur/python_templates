#! /usr/bin/python3

#########################################################
#                                                       #
#   Vorlage fuer Plots                                  #
#   Anselm Baur                                         #
#   Oktober 2016                                        #
#                                                       #
#########################################################

import csv
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from scipy.optimize import curve_fit

#Messwerte eintragen und Fehler berechnen

N = np.array([39674,35656,32512,29436,27052,23805,21511,20335,18657,16621,15119,13358,12764,11604,10402,9646])
r = np.array(np.arange(0.14,0.22,0.005))
delta = np.abs(1/N*np.sqrt(N))+np.abs(2/r*0.0005)

x_raw = r
y_raw = np.log(N*r**2)
y_err = delta

print(y_err)
# Achsenausschnitt auf der x und y Achse
x_scal = np.array([0.1,0.3])
y_scal = np.array([6,7])

# FIGURE
fig = plt.figure(figsize=(10,10))
ax = fig.add_subplot(1,1,1)
ax.clear()

# FIT
def func(x, a, b):
    return(a*x+b)
popt_1, pcov_1 = curve_fit(func, x_raw, y_raw,sigma=y_err)
x_fit = np.arange(0.1,0.25,0.010)
y_fit = func(x_fit, popt_1[0], popt_1[1])
a_1 = round(popt_1[0], 4)
b_1 = round(popt_1[1], 4)
perr_1 = np.sqrt(np.diag(pcov_1))



###################################### Hier nur Style #################################
xmajor_ticks = np.arange(x_scal[0],x_scal[1]+0.01,(x_scal[1]-x_scal[0])/4)
xminor_ticks = np.arange(x_scal[0],x_scal[1],(x_scal[1]-x_scal[0])/20)

ymajor_ticks = np.arange(y_scal[0],y_scal[1]+0.1,(y_scal[1]-y_scal[0])/10)
yminor_ticks = np.arange(y_scal[0],y_scal[1],(y_scal[1]-y_scal[0])/100)

ax.set_xlim(x_scal[0],x_scal[1])
ax.set_ylim(y_scal[0], y_scal[1])
ax.axhline(linewidth=0.5, color="k")
ax.axvline(linewidth=0.5, color="k")
# Schriftgroesse der Achsenwerte
plt.setp(ax.get_xticklabels(), fontsize=18)
plt.setp(ax.get_yticklabels(), fontsize=18)

ax.set_xticks(xmajor_ticks)
ax.set_xticks(xminor_ticks, minor=True)
ax.set_yticks(ymajor_ticks)                                                       
ax.set_yticks(yminor_ticks, minor=True)
ax.tick_params("both", length=10, which="major")
ax.tick_params("both", length=5, which="minor")

ax.grid(which="major", alpha=0.5)
######################################################################################

ax.set_xlabel(r'Abstand $r$ in m', fontsize=18)
ax.set_ylabel(r'$\ln(N\cdot r^2)$', fontsize=18)



ax.errorbar(x_raw,y_raw, xerr=0, yerr=y_err, fmt='o', c='b', capsize=2, elinewidth=0.5,  label="ohne Cd") # Messdatenus
ax.plot(x_fit,y_fit, 'r')
ax.text(0.15, 6.8, r'$\ln(N\cdot r^2)$ = '+str(a_1)+r'$\pm$'+str(round(perr_1[0],3))+r'$\cdot r^{-1}}$ + '+ str(abs(b_1))+r'$\pm$'+str(round(perr_1[1],3)), fontsize=16)
ax.legend( loc="upper right",  prop={'size':16}).get_frame().set_linewidth(0.5)

plt.show()

# Save figure
fig.savefig('../fig/plot.eps')