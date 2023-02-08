# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 20:48:50 2020

@author: MG

"""
import numpy as np
import scipy.io as spio # to import matlab
import matplotlib.pyplot as plt
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter, AutoMinorLocator)


# Initial parameters
#Choose air/fuel ratio Lambda according to data: 0.9, 1 or 1.1

Lambda = 1.1

Speed=1500 # rpm

if Lambda==0.9:
    Data = spio.loadmat('Data_L09.mat')
elif Lambda==1:
    Data = spio.loadmat('Data_L1.mat')
elif Lambda==1.1:
    Data = spio.loadmat('Data_L11.mat')

# Cylinder Pressure Data
P_Test1 = Data ['P_Mot'] # import variable from mat file
P_Test2 = Data ['P_SA20']
P_Test3 = Data ['P_SA25']
P_Test4 = Data ['P_SA30']

# Engine Torque Data
T_Test1 = Data ['T_Mot'] # import variable from mat file
T_Test2 = Data ['T_SA20']
T_Test3 = Data ['T_SA25']
T_Test4 = Data ['T_SA30']

P_Test1=np.squeeze(P_Test1) #removes axes with length 1
P_Test2=np.squeeze(P_Test2)
P_Test3=np.squeeze(P_Test3)
P_Test4=np.squeeze(P_Test4)

T_Test1=np.squeeze(T_Test1) #removes axes with length 1
T_Test2=np.squeeze(T_Test2)
T_Test3=np.squeeze(T_Test3)
T_Test4=np.squeeze(T_Test4)

SA_Test1=0 # Spark Advance, CAD BTDC
SA_Test2=20
SA_Test3=25
SA_Test4=30

#labels for plots

label_Test1='Motoring'
label_Test2='SA 20'
label_Test3='SA 25'
label_Test4='SA 30'

#labels for bar plot
labels_line_all = [label_Test1, label_Test2, label_Test3, label_Test4]
labels_line_fired = [label_Test2, label_Test3, label_Test4]
label_L=', $\lambda$ = '+str(Lambda) #converts to string

#First Figure:
Ff=1;




from fc_volume_4F import volume #call function to calculate volume
Vd, Vc, Vth, dVth, cad =volume ()

#Create cylinder volume plot

fig, ax = plt.subplots()
ax.grid()
ax.set_ylabel('Volume, $cm^3$')
F=str(Ff)
ax.set_xlabel('CAD \n \n Fig. '+F+'. Cylinder Volume During Engine Cycle')
Ff=Ff+1
maxval=np.max(Vth*10**6)
ylim=maxval+50
ax.set_xlim(-360, 360)
ax.set_ylim(0, ylim)

ax.xaxis.set_major_locator(MultipleLocator(60)) # distribute major ticks on x axis

line, = ax.plot(cad-360, Vth*10**6, label=('Volume'))

plt.show()

# Create cylinder pressure plot
fig, ax = plt.subplots()
ax.grid()
ax.set_ylabel('Pressure, bar')

F=str(Ff)
ax.set_xlabel('CAD \n \n Fig. '+F+'. Pressure changes in cylinder'+label_L)
Ff=Ff+1
maxval=np.max([np.max(P_Test1), np.max(P_Test2), np.max(P_Test3), np.max(P_Test4)])
ylim=maxval+5
ax.set_xlim(-100, 100)
ax.set_ylim(0, ylim)
ax.xaxis.set_major_locator(MultipleLocator(20)) # distribute major ticks on x axis
line, = ax.plot(cad-360, P_Test1, label=label_Test1)
line, = ax.plot(cad-360, P_Test2, label=label_Test2)
line, = ax.plot(cad-360, P_Test3, label=label_Test3)
line, = ax.plot(cad-360, P_Test4, label=label_Test4)
#ax.legend()
plt.show()


# Create cylinder pressure/volume plot
fig, ax = plt.subplots()
ax.grid() #create grid
ax.set_ylabel('Pressure, bar')
F=str(Ff)
ax.set_xlabel('Volume, $cm^3$ \n \n Fig. '+F+'. Pressure/ volume diagram'+label_L)
Ff=Ff+1
maxval=np.max([np.max(P_Test1), np.max(P_Test2), np.max(P_Test3), np.max(P_Test4)])
ylim=maxval+5
ax.set_xlim(0, 500) #set axe limits
ax.set_ylim(0, ylim)
line, = ax.plot(Vth*10**6, P_Test1, label=label_Test1) #create multilple line plots
line, = ax.plot(Vth*10**6, P_Test2, label=label_Test2)
line, = ax.plot(Vth*10**6, P_Test3, label=label_Test3)
line, = ax.plot(Vth*10**6, P_Test4, label=label_Test4)
ax.legend()
plt.show()

# Create cylinder pressure/volume log plot
fig, ax = plt.subplots()
ax.grid() #create grid
ax.set_ylabel('Pressure, bar')
F=str(Ff)
ax.set_xlabel('Volume, $cm^3$ \n \n Fig. '+F+'. Pressure/ volume diagram in log scale'+label_L)
Ff=Ff+1
maxval=np.log(np.max([np.max(P_Test1), np.max(P_Test2), np.max(P_Test3), np.max(P_Test4)]))
ylim=maxval+5
#ax.set_xlim(0, 750) #set axe limits
#ax.set_ylim(0, ylim)
ax.set_xscale('log')
ax.set_yscale('log')
ax.xaxis.set_major_locator(MultipleLocator(30)) # distribute major ticks on x axis
ax.yaxis.set_major_locator(MultipleLocator(10)) # distribute major ticks on y axis
line, = ax.plot((Vth*10**6), (P_Test1), label=label_Test1) #create multilple line plots
line, = ax.plot(Vth*10**6, P_Test2, label=label_Test2)
line, = ax.plot(Vth*10**6, P_Test3, label=label_Test3)
line, = ax.plot(Vth*10**6, P_Test4, label=label_Test4)
ax.legend()
plt.show()



from fc_maxp import maxp #call function to find maximal pressure and angle
PMax_Test1, PMax_cad_Test1 =maxp (P_Test1, cad)
PMax_Test2, PMax_cad_Test2 =maxp (P_Test2, cad)
PMax_Test3, PMax_cad_Test3 =maxp (P_Test3, cad)
PMax_Test4, PMax_cad_Test4 =maxp (P_Test4, cad)


# Create bar plot for Pmax
Pmax = [PMax_Test1, PMax_Test2 ,PMax_Test3,PMax_Test4]

x = np.arange(np.size(Pmax)) # creates array for bar order
fig, ax = plt.subplots()
plt.bar(x, Pmax,width=0.3, color=['C0','C1', 'C2', 'C3'])

for index, value in enumerate(x):
    plt.text(value, (Pmax[index]+1.5), str(np.round(Pmax[index],1)),horizontalalignment='center')
    
ax.set_ylabel('Pressure, bar')
F=str(Ff)
ax.set_xlabel('Test Mode \n \n Fig. '+F+'. Maximal Pressure'+label_L)
Ff=Ff+1
ylim=np.round((np.max(Pmax)+5),2)
ax.set_ylim(0, ylim)
plt.xticks(x, labels_line_all)
plt.show()

# Create bar plot for Pmax cad
Pmax_cad = [PMax_cad_Test2,PMax_cad_Test3,PMax_cad_Test4]

x = np.arange(np.size(Pmax_cad)) # creates array for bar order
fig, ax = plt.subplots()
plt.bar(x, Pmax_cad,width=0.3, color=['C1', 'C2', 'C3'])

for index, value in enumerate(x):
    plt.text(value, (Pmax_cad[index]+0.5), str(np.round(Pmax_cad[index],1)),horizontalalignment='center')
    
ax.set_ylabel('CAD, ATDC')
F=str(Ff)
ax.set_xlabel('Test Mode  \n \n Fig. '+F+'. Maximal Pressure Angle'+label_L)
Ff=Ff+1
ylim=np.round((np.max(Pmax_cad)+2),2)
ax.set_ylim(0, ylim)
plt.xticks(x, labels_line_fired)
plt.show()

#Create brake torque plot

fig, ax = plt.subplots()
ax.grid()
ax.set_ylabel('Torque, $Nm$')
F=str(Ff)
ax.set_xlabel('CAD \n \n Fig. '+F+'. Pressure and Brake Torque During Engine Cycle, SA20'+label_L)
Ff=Ff+1
maxval=np.max(T_Test2)
minval=np.min(T_Test2)
ylim=maxval+2
ylim_min=minval-2
ax.set_xlim(-360, 360)
ax.set_ylim(ylim_min, ylim)

ax.xaxis.set_major_locator(MultipleLocator(60)) # distribute major ticks on x axis

ax2 = ax.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Pressure, bar')  

ax2.yaxis.set_major_locator(MultipleLocator(2)) # distribute major ticks on y axis
fig.tight_layout()  # otherwise the right y-label is slightly clipped

line, = ax.plot(cad-360, T_Test2)
line, = ax2.plot(cad-360, P_Test2, color = 'C1')

plt.show()

# starting 3.2

from fc_BMEP_4F import BMEP #call function to calculate BMEP of one cylinder

BMEP_Test2 = BMEP (T_Test2)
BMEP_Test3 = BMEP (T_Test3)
BMEP_Test4 = BMEP (T_Test4)


# Create bar plot for BMEP
BMEP = [BMEP_Test2 ,BMEP_Test3, BMEP_Test4]

x = np.arange(np.size(BMEP)) # creates array for bar order
fig, ax = plt.subplots()
plt.bar(x, BMEP,width=0.3, color=['C1', 'C2', 'C3'])

for index, value in enumerate(x):
    plt.text(value, (BMEP[index]+0.2), str(np.round(BMEP[index],1)),horizontalalignment='center')
    
ax.set_ylabel('Brake Mean Effective Pressure, bar')
F=str(Ff)
ax.set_xlabel('Test Mode  \n \n Fig. '+F+'. Brake Mean Effective Pressure'+label_L)
Ff=Ff+1


ylim=np.round((np.max(BMEP)+1),2)
ax.set_ylim(0, ylim)
plt.xticks(x, labels_line_fired)
plt.show()


from fc_imep import imep #call function to calculate IMEP

IMEP_net_Test1, IMEP_gross_Test1 =imep (P_Test1, dVth, Vd)
IMEP_net_Test2, IMEP_gross_Test2 =imep (P_Test2, dVth, Vd)
IMEP_net_Test3, IMEP_gross_Test3 =imep (P_Test3, dVth, Vd)
IMEP_net_Test4, IMEP_gross_Test4 =imep (P_Test4, dVth, Vd)


# Create bar plot for IMEP_net
IMEP = [IMEP_net_Test1, IMEP_net_Test2 ,IMEP_net_Test3, IMEP_net_Test4]
labels = ['Mot', 'Adv5', 'Adv11', 'Adv15']
x = np.arange(np.size(IMEP)) # creates array for bar order
fig, ax = plt.subplots()
plt.bar(x, IMEP,width=0.3,color=['C0','C1', 'C2', 'C3'])

for index, value in enumerate(x):
    plt.text(value, (IMEP[index]+0.2), str(np.round(IMEP[index],2)),horizontalalignment='center')
    
ax.set_ylabel('IMEP$_{net}$, bar')
F=str(Ff)
ax.set_xlabel('Test Mode  \n \n Fig. '+F+'. Indicated Mean Effective  Pressure, Net'+label_L)
Ff=Ff+1


ylim=np.round((np.max(IMEP)+1),2)
ax.set_ylim(-1, ylim)
plt.xticks(x, labels)
plt.show()

# Create bar plot for IMEP_gross
IMEP = [IMEP_gross_Test1, IMEP_gross_Test2 ,IMEP_gross_Test3, IMEP_gross_Test4]
labels = ['Mot', 'Adv5', 'Adv11', 'Adv15']
x = np.arange(np.size(IMEP)) # creates array for bar order
fig, ax = plt.subplots()
plt.bar(x, IMEP,width=0.3,color=['C0','C1', 'C2', 'C3'])

for index, value in enumerate(x):
    plt.text(value, (IMEP[index]+0.2), str(np.round(IMEP[index],2)),horizontalalignment='center')
    
ax.set_ylabel('IMEP$_{gross}$, bar')
F=str(Ff)
ax.set_xlabel('Test Mode  \n \n Fig. '+F+'. Indicated Mean Effective  Pressure, Gross'+label_L)
Ff=Ff+1

ylim=np.round((np.max(IMEP)+1),2)
ax.set_ylim(-1, ylim)
plt.xticks(x, labels)
plt.show()

# Pumping loss

PMEP_Test1=IMEP_gross_Test1-IMEP_net_Test1
PMEP_Test2=IMEP_gross_Test2-IMEP_net_Test2
PMEP_Test3=IMEP_gross_Test3-IMEP_net_Test3
PMEP_Test4=IMEP_gross_Test4-IMEP_net_Test4

# Create bar plot for pumping loss
PMEP = [PMEP_Test1, PMEP_Test2 ,PMEP_Test3, PMEP_Test4]
labels = ['Mot', 'Adv5', 'Adv11', 'Adv15']
x = np.arange(np.size(PMEP)) # creates array for bar order
fig, ax = plt.subplots()
plt.bar(x, PMEP,width=0.3,color=['C0','C1', 'C2', 'C3'])

for index, value in enumerate(x):
    plt.text(value, (PMEP[index]+0.2), str(np.round(PMEP[index],2)),horizontalalignment='center')
    
ax.set_ylabel('PMEP, bar')
F=str(Ff)
ax.set_xlabel('Test Mode  \n \n Fig. '+F+'. Pumping Loss'+label_L)
Ff=Ff+1

ylim=np.round((np.max(PMEP)+1),2)
ax.set_ylim(-1, ylim)
plt.xticks(x, labels)
plt.show()

# Friction loss


FMEP_Test2=IMEP_gross_Test2-BMEP_Test2
FMEP_Test3=IMEP_gross_Test3-BMEP_Test3
FMEP_Test4=IMEP_gross_Test4-BMEP_Test4

# Create bar plot for pumping loss
FMEP = [FMEP_Test2 ,FMEP_Test3, FMEP_Test4]
labels = [ 'Adv5', 'Adv11', 'Adv15']
x = np.arange(np.size(FMEP)) # creates array for bar order
fig, ax = plt.subplots()
plt.bar(x, FMEP,width=0.3,color=['C1', 'C2', 'C3'])

for index, value in enumerate(x):
    plt.text(value, (FMEP[index]+0.2), str(np.round(FMEP[index],2)),horizontalalignment='center')
    
ax.set_ylabel('FMEP, bar')
F=str(Ff)
ax.set_xlabel('Test Mode  \n \n Fig. '+F+'. Friction Loss'+label_L)
Ff=Ff+1

ylim=np.round((np.max(FMEP)+1),2)
ax.set_ylim(-1, ylim)
plt.xticks(x, labels)
plt.show()




