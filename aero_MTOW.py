'''
aero_MTOW.py: Runs takeoff simulation to determine MTOW








'''

from __future__ import print_function
from openmdao.api import Component, Group, Problem

# Imported from Python standard
import sys
import os
import time
import math
import numpy
from  AVL_py import AVL

runway_length = 200 	#[ft]
rho = 0.0765 			#[lbm/ft^3]
g = 9.81 * 3.28 		#[ft/s^2]
mu = 0.125

class aero_MTOW(Component):
	""" Makes the appropriate run file and outputs the computed numbers """
	def __init__(self):

		super(aero_MTOW, self).__init__()

		self.add_param('CL', val = 0.0);
		self.add_param('CD', val = 0.0);
		#self.add_param('friction-coeff', val = 0.0)
		self.add_param('Sref', val = 0.0)
		self.add_param('b', val = 0.0)
		#self.add_param('EW', val = 10.0); # lbs
		# self.add_param('T0', val = 0.0)
		# self.add_param('T1', val = 0.0)
		# self.add_param('T2', val = 0.0)
		# self.add_param('T3', val = 0.0)
		# self.add_param('T4', val = 0.0)

		self.add_output('MTOW', val = 0.0)
		self.add_output('TO_time', val = 0.0)
		self.add_output('TO_length', val = 0.0)
		self.add_output('TO_vel', val = 0.0)

		

	def solve_nonlinear(self, params, unknowns, resids):
		T0 = 12.756 
		T1 = -0.0941  
		T2 = 0.0023  
		T3 = -7e-05
		T4 = 4e-7 
		T_coeff = [T0, T1, T2, T3, T4] # All lbf

		#================================================
		# Function declarations
		#================================================
		def calc_total_force(v, CL, CD, Sref, mass, T_coeff, alpha):
			''' Calculates both the horizontal and vertical forces at specified conditions '''
			T0 = T_coeff[0]
			T1 = T_coeff[1]
			T2 = T_coeff[2]
			T3 = T_coeff[3]
			T4 = T_coeff[4]

			Ft = (T0 + T1 * v + T2 * v ** 2 + T3 * v ** 3 + T4 * v ** 4)
			if  Ft < 0:
				Ft = 0

			# Lift	
			Fl = 0.5 * rho * v ** 2 * Sref * CL

			# Drag 
			Fd = 0.5 * rho * v ** 2 * Sref * CD

			# Wheel Friction
			Fw = mu * ( mass * g - Fl - Ft *math.sin(math.radians(alpha)))
			if Fw < 0:
				Fw = 0


			F = []
			F.append(Ft *math.sin(math.radians(alpha)) - Fw - Fd)
			Fy = Fl - mass * g
			if Fy < 0:
				F.append(0)
			else:
				F.append(Fy)

			return F

		def calc_momentum_buildup(runway_length, mass, CL, CD, Sref, T_coef,T,  b):
			''' Calculates the runway length of the aircraft w/ specified properties '''
			 # Mass is independent variable
			 # Runway length is dependent variable
			 # ALL VARIABLES HAVE TO BE IMPERIAL UNITS
			 # Newton's method step varying mass and getting runway length

			position = [0, 0] 	#[ft] X, Y
			velocity = [0, 0] 	#[ft/s] X, Y
			force = [] 		#[lbf] X, Y
			time = 0 			#[s]
			dt = 0.001

			while position[0] < runway_length or position[1] > 0:

				position[0] = position[0] + velocity[0] * dt
			 	position[1] = position[1] + velocity[1] * dt

			 	force = calc_total_force(velocity[0], CL, CD,mass, Sref, T_coef, 0)

			 	velocity[0] = velocity[0] + force[0] * dt / mass
			 	velocity[1] = velocity[1] + force[1] * dt / mass

			 	time = time + dt

			set_all = {'time': time, 'length':position[0], 'vel_X':velocity[0]}
			return set_all

		# End of function declaring
		
		# Newton's Method
		empty_mass = 10.0 		# [lbs]
		starting_payload = 5.0 	# [lbs]

		total_mass = empty_mass + starting_payload
		starting_1 = calc_momentum_buildup(runway_length, total_mass, params['CL'], params['CD'], params['Sref'], T_coeff, T0, params['b'])
		total_mass = total_mass + 1
		starting_2 = calc_momentum_buildup(runway_length, total_mass, params['CL'], params['CD'], params['Sref'], T_coeff, T0, params['b'])
		
		tol_MTOW = starting_2['length'] - starting_1['length'] 
		deriv = starting_2['length'] - starting_1['length']
		prev_mass = total_mass
		previous = starting_2

		while tol_MTOW > 0.01:  
			
			next_mass = prev_mass - previous['length']/deriv
			next_total = calc_momentum_buildup(runway_length, next_mass, params['CL'], param['CD'], param['Sref'], T_coeff, T0, param['b'])

			deriv = (next_total['length'] - previous['length'])/(next_mass - prev_mass)
			tol_MTOW = (next_total['length'] - previous['length'])
			prev_mass = next_mass
			previous = next_total

		unknowns['MTOW'] = prev_mass
		unknowns['TO_time'] = previous['time']
		unknowns['TO_length'] = previous['length']
		unknowns['TO_vel'] = previous['vel_X']

		







			 	
