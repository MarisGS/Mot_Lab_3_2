# -*- coding: utf-8 -*-
"""
Created on Thu Apr 30 01:28:32 2020

@author: Lietotajs
"""
def BMEP (Tb):
    import numpy as np
    from fc_volume_4F import volume #call function to calculate volume
    Vd, Vc, Vth, dVth, cad =volume ()
    
    Tb_mean=np.mean(Tb)/4
    BMEP=(Tb_mean*2*np.pi*2*10**(-5))/Vd
    
    return BMEP    
