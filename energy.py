import rebound

def input(mass, x_coordinate, y_coordinate, z_coordinate, vx_coordinate, vy_coordinate, vz_coordinate):
	sim=rebound.Simulation()
	sim.units=['kg', 'm', 's']
	for (mass, xco, yco, zco, vxco, vyco, vzco) in zip(mass, x_coordinate, y_coordinate, z_coordinate,  vx_coordinate, vy_coordinate, vz_coordinate):
		sim.add(m=mass,x=xco, y=yco, z=zco, vx=vxco, vy=vyco, vz=vzco)
	energy=sim.calculate_energy()
	print('energy of the system is {0} Joules'.format(round(energy, 2)))

input(mass=[1,1], x_coordinate=[5,0],y_coordinate=[0,0], z_coordinate=[0,0], vx_coordinate=[2,0], vy_coordinate=[0,0], vz_coordinate=[0,0]) 
