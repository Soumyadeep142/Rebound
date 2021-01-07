import rebound
from numpy import *

plannet=['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
for first in range(len(plannet)):
	for second in range(first+1, len(plannet)):
		print(first, second)
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

		years=['Year']
		month=['Month']
		Distance=["Distance in km"]
		for l in range(10):
			yr=2000+(months_array[l]//12)
			mon=months_stack[months_array[l]%12]
			dis=dist[l]
			years.append(yr)
			month.append(mon)
			Distance.append(dis)
		data=column_stack((years, month, Distance))
		savetxt('Nearest Distances {0} and {1}.txt'.format(plannets[0],plannets[1]), data, fmt='%s')
