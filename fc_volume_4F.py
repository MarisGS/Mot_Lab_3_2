
#Created on Sun Apr 12 15:13:04 2020

#@author: MG

def volume ():


    import numpy as np

    cad = np.linspace(0.1, 720, 7200)



    B=0.081 #Bore ,m
    s=0.077 #Stroke, m
    r=s/2# klokja garums, m
    L=0.13 # klanja garums, m 
    A=np.pi*(B/2)**2 # virsmas laukums, m2
    Vd=A*s # darba tilpums, m3

  
    CR = 9.5

    Vc=Vd/(CR-1)


    scad=L+r-(r*np.cos(np.radians(cad))+(L**2-r**2*np.sin(np.radians(cad))**2)**(1/2))

    Vth=Vc+A*scad

    #Vthm=np.roll(Vth,1) #shift array
    #dVth=Vth - Vthm
    
    dVth =(r*(np.sin(np.radians(cad)))+(r**2*(np.sin(2*np.radians(cad))))/(2*(L**2-r**2*(np.sin(np.radians(cad))**2))**(1/2)))*((np.pi*B**2)/4)*(np.pi/180)*0.1
 
    
    return Vd, Vc, Vth, dVth, cad

