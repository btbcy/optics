import csv
from visual import*
from visual.graph import*

lamda_begin = 490.0
lamda_end   = 510.0
c           = 3E17
delta_end   = 5000000
delta_step  = 50

scene1 = gdisplay (x=0, y=0, width=1000, height=300,
        xtitle='lamda', ytitle='spectrum', xmin=lamda_begin, xmax=lamda_end, background=(0.2, 0.6, 0.2))
Is_plot = gcurve (color=color.blue, gdisplay=scene1)

# read data from output.csv
It = dict()

for key, val in csv.reader (open("output.csv")):
    It[int(key)] = float(val)

It0 = 0.5 * It[0]

# gamma function
def gamma_delta(d):
    return (It[d]-It0)/It0

lamda = lamda_begin
while lamda < lamda_end:
    rate(100)
    Is = 0
    delta = 0
    while delta < delta_end:
        Is += gamma_delta(delta)*cos(2*pi*delta/lamda)*delta_step
        delta += delta_step
    Is *= 4 * It0 / c
    Is_plot.plot(pos=(lamda, Is))
    lamda += 0.1
