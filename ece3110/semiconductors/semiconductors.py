import scipy.optimize as optimize
import math
import numpy as np
####Constants####


q=1.6e-19
B_si= 1.08e31
Eg_si= 1.12
k=8.62e-5
kc=8.99e9


####Useful Equations####
def ni_equation(T):
    equation=np.sqrt(B_si*T**3*np.exp(-Eg_si/(k*T)))
    return equation

def res(T, w, h, l, Na, Nd,v):
   # mu_n=find_mu_n(Na,Nd)
    #mu_p=find_mu_p(Na,Nd)
    Nt=Nd+Na
    mu_n=52.2+(1365/(1+(Nt/9.68e16)**.68))
    mu_p=44.9+(426/(1+(Nt/2.23e16)**.72))

    ni=ni_equation(T)
    E= E_field(v,l)
    if((Na==0) and (Nd==0)):
        n=ni
        p=ni
    elif(Na<Nd):
        n=((Nd-Na)+np.sqrt((Nd-Na)**2+4*(ni**2)))/2
        p=(ni**2)/n
    else:
        p=((Na-Nd)+np.sqrt((Na-Nd)**2+4*(ni**2)))/2
        n=(ni**2)/p
    
    sigma = q*(mu_n*n+mu_p*p)
    rho =  solve_rho(sigma)
    Overall_resistance=rho*l/(h*w)
    jdrift=sigma*E

    print("sigma={:0.2e} rho={:0.2e}".format(sigma,rho))
    print("OVERALL RESISTANCE={:0.2e}".format(Overall_resistance))
    #print("E={:0.2e}".format(E))
    print("Curren Density={:0.2e}".format(jdrift))
    print("n={:0.2e} p={:0.2e}".format(n,p))
    print("mu_n={:0.2e} mu_p={:0.2e}".format(mu_n,mu_p))
    #jdiff=q*(Dn*()-Dp())
    #jtotal=jdrift+jdiff
    return Overall_resistance

def E_field(v,l):
    #print("Checking Length converted right {:0.2e}".format(l))
    E=v/l
    #print("Checking E is the same {:0.2e}".format(E))
    return E

def find_E(v,l):
    E=v/l
    return E

#def solve_sigma(mu_n, mu_p, n, p):
 #   s=q*(mu_n*n+mu_p*p)
    #return s

def solve_rho(sigma):
    return 1/sigma

def find_mu_n(Na, Nd):
    Nt=Nd+Na
    mu_n=52.2+(1365/(1+(Nt/9.68e16)**.68))
    return mu_n

def find_mu_p(Na, Nd):
    Nt=Nd+Na
    mu_p=44.9+(426/(1+(Nt/2.23e16)**.72))

def f(T, ni):
    return np.sqrt(B_si*T**3*np.exp(-Eg_si/(k*T)))-ni

def solve_for_T(ni):
    T=optimize.brentq(f, 300, 10500,args=(ni))
    print("T={:0.2e}".format(T))
    return T

def solving_for_ni(R,l,w,h,Na,Nd):
    rho= (R*(w*h))/l
    sigma = 1/rho
    Nt=Na+Nd
    mu_n=52.2+(1365/(1+(Nt/9.68e16)**.68))
    mu_p=44.9+(426/(1+(Nt/2.23e16)**.72))
    ni = sigma/(q*(mu_n+mu_p))
    print("ni = {:0.2e}".format(ni))
    return ni


#def find_Na_Eq(Nd, Na, ni, p):
 #   ni=ni_equation
  #  return (((Na-Nd)+np.sqrt((Na-Nd)**2+4*ni**2))/2)-p

#def find_Nd(n,p,Na,Nd,ni):
    #Nd=optimize.brentq(find_Nd_Eq(), 0, 1e30)
    #print("T={:0.2e}".format(Na))
    #return Nd

#def find_Nd_Eq(Nd, Na, ni, n, T):
    #ni=ni_equation(T)
    #return (((Nd-Na)+np.sqrt((Nd-Na)**2+4*ni**2))/2)-n

#def find_Na(n, p, Na, Nd, ni):
 #   Na=optimize.brentq(find_Na_Eq, 0, 1e30)
  #  print("T={:0.2e}".format(Na))
   # return Na