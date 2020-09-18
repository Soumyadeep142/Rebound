import rebound
from numpy import *
from matplotlib import *

sim = rebound.Simulation()
sim.units=('kg','km','yr')

#Searching Nasa Horizons

sim.add(particle='Sun')
plannet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune','Pluto']
for particles in plannet:
	sim.add(particle=particles)
year=linspace(1,200,1500)
j=0
for t in year:
	j+=1
	sim.integrate(t)
	fig,ax_main=rebound.OrbitPlot(sim, xlim=(-6*10**9,8*10**9), ylim=(-5*10**9,7*10**9), unitlabel='km', color=['grey','pink',"blue","red",'orange','yellow','white','green','grey'], orbit_type='solid', fancy='true')
	fig.savefig('Solar System{0}.png'.format(j))
	print(t)
fig.show()

