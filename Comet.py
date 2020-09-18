import rebound
from numpy import *
from matplotlib.pyplot import *

sim=rebound.Simulation()
sim.units=('kg', 'AU', 'yr')
sim.add(particle="Sun")
sim.add(particle="Jupiter")
sim.add(particle="Saturn")
sim.add(particle="Uranus")
sim.add(particle="Neptune")
sim.add(m=2.2*10**14, a=17.834, e=0.96714,  inc=2.832, Omega= 1.012, M=0.67) #Halley's Comet
#sim.add(particle='Mercury')
#sim.status()
year=arange(1,1000,1)
j=0
for t in year:
	j+=1
	sim.integrate(t)
	fig,ax_main=rebound.OrbitPlot(sim, xlim=(-40,40), ylim=(-35,46), unitlabel='AU', color=['grey','pink',"blue","red",'orange','yellow','white','green','cyan'], orbit_type='solid', fancy='true')
	title('year={0}'.format(round(t,1)))
	fig.savefig('Halley{0}'.format(j))
	print(t)
fig.show()
