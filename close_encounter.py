import rebound
from numpy import *
from matplotlib.pyplot import *

#Plotting the distances
sim=rebound.Simulation()
sim.add(m=1)
sim.add(m=1e-3, a=1)
sim.add(m=5e-3, a=1.25)
sim.move_to_com()
N=1000
times=linspace(0,100*2*pi,N)

sim.exit_min_distance=0.15
distances=zeros(N)
ps=sim.particles

try:
	for i, time in enumerate(times):
		sim.integrate(time)
		dp=(ps[1]-ps[2]) #Calculate difference between particles
		distances[i]=(sqrt((dp.x)*(dp.x)+(dp.y)*(dp.y)+(dp.z)*(dp.z)))		
except rebound.Encounter as error:
	print(error)
	
j=0
t=[]
d=[]
for (time,distance) in zip(times,distances):
	j+=1
	fig = figure(figsize=(10,5))
	ax = subplot(111)
	ax.set_xlabel("time [orbits]")
	ax.set_xlim([0,sim.t/(2.*pi)])
	ax.set_ylim([0,2.5])
	ax.set_ylabel("distance")
	t.append(time/(2*pi))
	d.append(distance)
	plot(t, d)
	axhline(0.15, color='black', lw=0.5)
	title('year={0}'.format(round(time/(2*pi),2)))
	savefig('{0}.png'.format(j))
	if distance==0:
		break
#Plotting the orbits
sim=rebound.Simulation()
sim.add(m=1)
sim.add(m=1e-3, a=1)
sim.add(m=5e-3, a=1.25)
sim.move_to_com()
N=1000
times=linspace(0,100*2*pi,N)

j=0

for i,time in enumerate(times):
	if i==47:
		break
	else:
		j+=1
		sim.integrate(time)
		fig,ax_main=rebound.OrbitPlot(sim, xlim=(-1.5, 1.5), ylim=(-1.5, 1.5), unitlabel='AU',  orbit_type='solid', fancy='true')
		title('year={0}'.format(round(time/(2*pi),2)))
		fig.savefig('System{0}.png'.format(j))
		print(time)
		
