import rebound
from numpy import *
from matplotlib.pyplot import *

sim=rebound.Simulation()
sim.units=('kg','km','yr')
sim.add(particle="Sun")

plannet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune', 'Pluto']
for particles in plannet:
	if particles=='Jupiter':
		sim.add(m=1.898580250761156e29 ,a=778480939.193071 ,e=0.048650024931482155)
	else:
		sim.add(particle=particles)

year=arange(1,1000,1)
j=0
for t in year:
	j+=1
	sim.integrate(t)
	fig,ax_main=rebound.OrbitPlot(sim, xlim=(-10*10**9,10*10**9), ylim=(-5*10**9,40*10**9), unitlabel='km', color=['grey','pink',"blue","red",'orange','yellow','white','green','cyan'], orbit_type='solid', fancy='true')
	title('year={0}'.format(round(t,1)))
	fig.savefig('Solar System{0}.png'.format(j))
	print(t)
fig.show()

