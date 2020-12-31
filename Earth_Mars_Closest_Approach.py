import rebound
from numpy import *


sim = rebound.Simulation()
sim.units=('kg','km','yr')
#Searching Nasa Horizons
date="2000-01-01 00:00"
sim.add(particle='Sun', date=date)
plannet=['Earth','Mars']
for particles in plannet:
	sim.add(particle=particles, date=date)


months_array=[]
dist=[]
ps=sim.particles
y=arange(0,100,1)
t=arange(1,13,1)
for i in y:
	for j in t:
		months=i*12+j
		months_array.append(months)
		year=i+j/12.0
		sim.integrate(year)
		dp=(ps[1]-ps[2]) #Calculate difference between particles
		distance=(sqrt((dp.x)*(dp.x)+(dp.y)*(dp.y)+(dp.z)*(dp.z)))
		dist.append(distance)

dist, months_array=zip(*sorted(zip(dist, months_array)))

months_stack=['January', 'February', 'March', "April", 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

for l in range(10):
	yr=2000+(months_array[l]//12)
	mon=months_stack[months_array[l]%12]
	dis=round(dist[l]/10**7,2)
	print('{0} {1} distance={2}*10^7km'.format(yr, mon, dis))
