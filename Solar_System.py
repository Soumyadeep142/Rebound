import rebound
from numpy import *


sim = rebound.Simulation()
sim.units=('kg','m','s')


sim.add(particle='Sun')
plannet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
for particles in plannet:
	sim.add(particle=particles)
sim.integrate(2*pi)

fig,ax_main=rebound.OrbitPlot(sim, xlim=(-6*10**12,6*10**12), ylim=(-5*10**12,5*10**12), unitlabel='km', color=['grey','pink',"blue","red",'orange','yellow','white','green'], orbit_type='solid', fancy='true')
fig.savefig('Solar System.pdf')
fig.show()


