import rebound
from numpy import *
from tabulate import tabulate

plannet=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
Pt=['Plannet']+plannet
Mercury=['Mercury']
Venus=['Venus']
Earth=['Earth']
Mars=['Mars']
Jupiter=['Jupiter']
Saturn=['Saturn']
Uranus=['Uranus']
Neptune=['Neptune']
Dummy=[Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune]

for first in range(len(plannet)):
	for second in range(len(plannet)):
		if second>first:
			plannets=[]
			sim = rebound.Simulation()
			sim.units=('kg','km','yr')
			date="2000-01-01 00:00"
			sim.add(particle='Sun', date=date)
			plannets.append(plannet[first])
			plannets.append(plannet[second])
			for particles in plannets:	
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

			yr=str(2000+(months_array[0]//12))
			mon=months_stack[months_array[0]%12]
			dis=dist[0]
			Dummy[first].append('{0} {1}'.format(yr,mon))
	#		print(yr)
		else:
			Dummy[first].append('X')

table=[[Pt[k], Mercury[k], Venus[k], Earth[k], Mars[k], Jupiter[k], Saturn[k], Uranus[k],Neptune[k]] for k in range(len(Pt))]
print(tabulate(table))
