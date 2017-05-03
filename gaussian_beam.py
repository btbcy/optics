from numpy import *
import pylab as plt

Lx    = 100E-3         # m (MKS)
Lz    = 1E-3           # m
N     = 101            # grid number in x and y
Nz    = 10000          # grid number in z
dx    = Lx / (N-1)     # grid size in x and y
dz    = Lz / Nz        # grid size in z
w0    = 7E-6           # m, beam width at minimum waist
lamda = 500E-9         # m, wavelength
k     = 2 * pi / lamda # wave vector
zo    = pi * w0**2 / lamda

#1, to set the amplitude at z = 0
u = zeros([N, N])
for i in range (N):
    for j in range (N):
