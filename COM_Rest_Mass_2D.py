import rebound
from matplotlib.pyplot import *

def input(mass, x_coordinate, y_coordinate):
	sim=rebound.Simulation()
	sim.units=['kg','m','s']
	for (mass, xco, yco) in zip(mass, x_coordinate, y_coordinate):
		sim.add(m=mass,x=xco, y=yco)
		text(xco+0.01,yco+0.01,'{0} kg'.format(mass))
	com=sim.calculate_com()

	scatter(x_coordinate, y_coordinate, color='red', s=100)
	scatter(com.x,com.y,color='blue')
	grid()
	text(com.x+0.01, com.y+0.01, 'Center of mass({0}m,{1}m)'.format(com.x,com.y))
	axvline(0, color='black', lw=2)
	axhline(0, color='black', lw=2)
	title('Centre of mass')
	xlabel('x-axis(m)')
	ylabel('y-axis(m)')
	savefig('COM_2D.pdf')
	show()
	
	
input(mass=[1,2,3,4], x_coordinate=[0,1,1,0], y_coordinate=[0,0,1,1])


