import rebound
from numpy import *


sim = rebound.Simulation()
sim.units=('kg','m','s')

#Searching Nasa Horizons
sim.add(particle="Sun") 
sim.add(particle="Mercury")
sim.add(particle="Venus")
sim.add(particle="Earth") 
sim.add(particle="Mars")
sim.add(particle="Jupiter")
sim.add(particle="Saturn")
sim.add(particle="Uranus")
sim.add(particle="Neptune")
sim.integrate(2*pi)

fig,ax_main=rebound.OrbitPlot(sim, xlim=(-6*10**12,6*10**12), ylim=(-5*10**12,5*10**12), unitlabel='km', color=['grey','brown',"blue","red",'orange','yellow','black','green'])
fig.savefig('Solar System.pdf')
fig.show()

