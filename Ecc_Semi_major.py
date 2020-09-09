import rebound
from numpy import *

sim=rebound.Simulation()
sim.units=['kg','m','s']

sim.add(particle='Sun')
plannet=['Mercury','Venus','Earth','Mars','Jupiter','Saturn','Uranus','Neptune']
for particles in plannet:
	sim.add(particle=particles)
orbits=sim.calculate_orbits()

f=open('Ecc_Semi_Major.txt','w+')
for (plannets,particles) in zip(orbits,plannet):
	f.write('Plannet={0}, eccentrecity={1}, semi-major axis={2}m \n'.format(particles, plannets.e, plannets.a))
f.close()
