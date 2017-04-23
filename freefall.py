from visual import *
g      = 9.8  # g        = 9.8 m/s^2
size   = 0.25 # ball radius = 0.25m
height = 15.0 # ball center initial height = 15m

# open a window
scene = display (width = 800, height = 800, center=(0,height/2.0), background=(0.5,0.5,0))
# the floor
floor = box (length = 30, height = 0.01, width = 10, color = color.blue)
# the ball
ball = sphere (radius = size, color = color.red)

ball.pos = vector (0, height, 0) # ball center initial position
ball.v = vector (0, 0, 0)        # ball initial velocity

dt = 0.001               # time step
while ball.pos.y >=size: # until the ball hit the ground
    rate (1000)          # runn 10000 times per real second
    ball.pos += ball.v * dt
    ball.v.y += -g *dt

print 'end'
