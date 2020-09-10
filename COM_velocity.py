import rebound

def input(mass, x_coordinate, y_coordinate, z_coordinate, vx_coordinate, vy_coordinate, vz_coordinate,time):
	sim=rebound.Simulation()
	sim.units=['kg', 'm', 's']
	for (mass, xco, yco, zco, vxco, vyco, vzco) in zip(mass, x_coordinate, y_coordinate, z_coordinate,  vx_coordinate, vy_coordinate, vz_coordinate):
		sim.add(m=mass,x=xco, y=yco, z=zco, vx=vxco, vy=vyco, vz=vzco)
	sim.integrate(time)
	com=sim.calculate_com()
	print('After time {0} s, \nPosition of centre of mass in x-coordinate is {1}m,\nPosition of centre of mass in y-coordinate is {2}m,\nPosition of centre of mass in z-coordinate is {3}m,\nVelocity of centre of mass in x-coordinate is {4}m/s,\nVelocity of centre of mass in y-coordinate is {5}m/s,\nVelocity of centre of mass in z-coordinate is {6}m/s'.format(time, com.x, com.y, com.z, com.vx, com.vy, com.vz))
	
input(mass=[1,1], x_coordinate=[-5,5], y_coordinate=[0,5], z_coordinate=[0,0], vx_coordinate=[0,0], vy_coordinate=[2,0], vz_coordinate=[0,0],time=3)
