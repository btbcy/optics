from visual import*
from visual.graph import *

A, lamda_a, lamda_ae = 1.0, 502.0, 0.4
B, lamda_b, gamma     = 0.1, 497.0, 0.6
C, lamda_c, lamda_ce = 0.1, 501.0, 0.2

lamda_begin = 495.0
lamda_end   = 505.0

R1      = [0.8, 0.99, 0.99]
m       = [20, 40, 20]
# t_begin = [m[idx] * lamda_begin for idx in range(3)]
# t_end   = [m[idx]*lamda_end for idx in range(3)]

def spectrum (lamda):
    specA = A * exp (-((lamda-lamda_a)/lamda_ae)**2)
    specB = B * (gamma/2) / ( (lamda-lamda_b)**2 + (gamma/2)**2 ) # lamda_a ??
    specC = C * exp (-((lamda-lamda_c)/lamda_ce)**2)
    return specA + specB + specC

def Tetalon (lamda, th, R):
    delta = 4*pi*1*th/lamda
    Te = (1-R)**2 / ( (1-R)**2 + 4*R*(sin(delta/2))**2)
    return Te

for idx in range (3):
    scene = gdisplay (x=0, y=300, width=1000, height=300,
            xtitle='lamda', ytitle='spectrum'+' R = '+str(R1[idx]), xmax=505, xmin=495, background=(0.2,0.6,0.2))
    pass_lamda = gcurve (color=color.blue, gdisplay=scene)
    t_begin = m[idx] * lamda_begin
    t_end   = m[idx] * lamda_end
    t = t_begin
    while t < t_end:
        rate(10000)
        pass_band = 0
        lamda_working = 495
        while lamda_working <= 505:
            pass_band += Tetalon(lamda_working,t,R1[idx]) * spectrum(lamda_working)
            lamda_working += 0.01
        pass_lamda.plot(pos = (t/m[idx], pass_band))
        t = t + 0.1

print 'end'
