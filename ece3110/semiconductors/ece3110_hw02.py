import semiconductors as sc
import diodes as di
T=28+273
ln=1600e-7
lp=1900e-7
w= 1900e-7
h= 150e-7
Na= 3e18
Nd= 2e20
V=-14

Overall_Res=sc.res(T, w, h, ln, Na, Nd, V)
#ni= sc.solving_for_ni(.023, 180e-7,200e-7,20e-7,1.3e-17)
#Temp= sc.solve_for_T(9.85e14)

#print("Current = {:0.2e}".format(V/Overall_Res))
#print("Density = {:0.2e}".format())
#print("Energy = {:0.2e}".format(sc.find_E(V,le)))

#test= sc.E_field(V, l)