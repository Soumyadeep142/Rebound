import rebound
from numpy import *
from matplotlib.pyplot import *

sim=rebound.Simulation()
sim.add(m=1.0)
sim.add(m=1e-6, a=1)
sim.move_to_com()
ps=sim.particles
c=0.01
#Adding an extra force F=m.c
def starkforce(reb_sim):
	ps[1].ax+=c
sim.additional_forces=starkforce

N=1000
es=[]
times=linspace(0,200*pi,N)
for i, time in enumerate(times):
	sim.integrate(time)
	es.append(sim.particles[1].e)
	print(i)
plot(times, es)
axvline(0, color='black',  lw=2)
axhline(0, color='black',  lw=2)
axhline(1, color='red', lw=0.5)
xlabel('time')
ylabel('eccentrecity')
savefig('time_vs_eccentrecity.png')
show()


