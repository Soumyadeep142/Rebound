import rebound
from numpy import *
from matplotlib.pyplot import *

sim=rebound.Simulation()
sim.add(m=1.0)
sim.add(m=1e-6, a=1)
sim.move_to_com()
ps=sim.particles
tau=1000
#Force is velocity dependent
def migration_force(reb_sim):
	ps[1].ax-=ps[1].vx/tau
	ps[1].ay-=ps[1].vy/tau
	ps[1].az-=ps[1].vz/tau
sim.additional_forces=migration_force

N=1000
a=[]
times=linspace(0,200*pi,N)
for i, time in enumerate(times):
	sim.integrate(time)
	a.append(sim.particles[1].a)
	print(i)
plot(times, a)
axvline(0, color='black',  lw=2)
axhline(0, color='black',  lw=2)
axhline(1, color='red', lw=0.5)
xlabel('time')
ylabel('semi-major axis')
savefig('time_vs_semi-major_axis.png')
show()


