import numpy as np
#GLOBAL VARIABLES

q=1.6e-19
B_si= 1.08e31
Eg_si= 1.12
k=8.62e-5
kc=8.99e9
es=11.7

def junction_potential(Nd,Na,Vt,ni):
    phi= Vt*np.log(Na*Nd/ni**2)
    return phi

def depletion_Wn(Wdo,Nd, Na):
    xn= Wdo/(1+(Nd/Na))
    return xn

def depletion_wp(wdo,Nd,Na):
    xp=wdo/(1+(Na/Nd))
    return xp

def depletion_width(Na, Nd, phi_j):
    wdo=np.sqrt((2*es/q)*((1/Na)+(1/Nd))*phi_j)
    return wdo

def dio_current(Is, Vd, n, Vt):
    Id= Is*np.exp(Vd/(n*Vt))-1
    return Id

def rev_dio_current(Id):
    Is= Id
    return -Is

def forward_dio_current(Is, n, Vt, Vd):
    Id= Is*np.exp(Vd/(n*Vt))
    return Id

def Max_e_field(Na, xp, Nd, xn):
    if(Na==0):
        Emax=q*Nd*xn/es
    elif(Nd==0):
        Emax=q*Na*xp/es
    return Emax

#def Diode_temp_coeff(dt):
 #   dvd=-1.82*dt
  #  return dvd

def depletion_wid_reverse_bias(wdo, vg, phi_j):
    wd=wdo*np.sqrt(1+(vg/phi_j))
    return wd

def reverse_bias_satur_curr(Is, Vg, phi_j):
    Isr= -Is*np.sqrt(1+(Vg/phi_j))
    return Isr

def charge_on_n_pn_junction(Nd,xn,a):
    Qn= q*Nd*xn*a
    return Qn

def charge_on_n_pn_junction_without_xn(wd,Nd,na,a):
    Qn= q*((na*Nd)/(na+Nd))*wd*a
    return Qn

def cap_of_pn_junc(a,wdo):
    Cjo=(es/wdo)*a
    return Cjo

def cap_of_pn_junc_unit_F(id,tT,Vt):
    Cd=(id*tT)/Vt
    return Cd

