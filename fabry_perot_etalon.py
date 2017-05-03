from visual import*
from visual.graph import *

A, lamda_a, lamda_ae = 1.0, 502.0, 0.4
B, lamda_b, gamma    = 0.1, 497.0, 0.6
C, lamda_c, lamda_ce = 0.1, 501.0, 0.2

lamda_begin = 495.0
lamda_end   = 505.0

R         = [0.8, 0.99, 0.99]
m         = [20, 40, 20]
t_begin   = lamda_begin * 20
t_end     = lamda_end * 20
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

def integ (i):
    pass_band = 0.
    lamda = lamda_begin
    while lamda <= lamda_end:
        pass_band += Tetalon(lamda,t*m[i],R[i]) * spectrum(lamda)
        lamda += 0.01
    return pass_band

# source spec
scene = gdisplay (x=0, y=300, width=1000, height=300,
        xtitle='lamda', ytitle='spectrum', xmax=505, xmin=495, background=(0.2,0.6,0.2))
source = gcurve(color=color.blue, gdisplay=scene)

t = lamda_begin
while t < lamda_end:
    rate(10000)
    source.plot(pos=(t, spectrum(t)))
    t = t + 0.01

sleep(5)
raw_input('Press Enter to continue...')

# scan
scene = gdisplay (x=0, y=300, width=1000, height=300,
        xtitle='lamda', ytitle='E1 : blue\nE2 : red\nE3 : yellow',
        xmax=505, xmin=495, background=(0.2,0.6,0.2))
scan1 = gcurve(color=color.blue, gdisplay=scene)
scan2 = gcurve(color=color.red, gdisplay=scene)
scan3 = gcurve(color=color.yellow, gdisplay=scene)

t = lamda_begin
while t < lamda_end:
    rate(10000)
    scan1.plot(pos=(t, Tetalon(t, 497*m[0], R[0])))
    scan2.plot(pos=(t, Tetalon(t, 497*m[1], R[1])))
    scan3.plot(pos=(t, Tetalon(t, 497*m[2], R[2])))
    t = t + 0.01

sleep(5)
raw_input('Press Enter to continue...')

# pass spec
scene = gdisplay (x=0, y=300, width=1000, height=300,
        xtitle='lamda', ytitle='E1 : blue\nE2 : red\nE3 : yellow',
        xmax=505, xmin=495, background=(0.2,0.6,0.2))
etalon1 = gcurve(color=color.blue, gdisplay=scene)
etalon2 = gcurve(color=color.red, gdisplay=scene)
etalon3 = gcurve(color=color.yellow, gdisplay=scene)

t = lamda_begin
while t < lamda_end:
    rate(10000)
    etalon1.plot(pos=(t, integ(0)/57.8))
    etalon2.plot(pos=(t, integ(1)/3.1))
    etalon3.plot(pos=(t, integ(2)/6.0))
    t = t + 0.01

print 'end'
