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

rho = 
g = 9.81;

class aero_MTOW(Component):
	""" Makes the appropriate run file and outputs the computed numbers """
	def __init__(self):

		super(aero_MTOW, self).__init__()

		self.add_param('CL', val = 0.0);
		self.add_param('CD', val = 0.0);
		self.add_param('friction-coeff', val = 0.0)
		#self.add_param('EW', val = 10.0); # lbs
		# self.add_param('T0', val = 0.0)
		# self.add_param('T1', val = 0.0)
		# self.add_param('T2', val = 0.0)
		# self.add_param('T3', val = 0.0)
		# self.add_param('T4', val = 0.0)

		self.add_output('MTOW', val = 0.0)
		self.add_output('TO-time', val = 0.0)
		self.add_output('TO-length', val = 0.0)
		self.add_output('TO-vel', val = 0.0)

		

	def solve_nonlinear(self, params, unknowns, resids):
		T0 = 
		T1 = 
		T2 = 
		T3 = 
		T4 = 
		T_coeff = [T0, T1, T2, T3, T4]

		#================================================
		# Function declarations
		#================================================
		def calc_total_force(v, CL, CD, Sref, mass, T_coeff, T, alpha):
			''' Calculates both the horizontal and vertical forces at specified conditions '''
			T0 = T_coeff[0]
			T1 = T_coeff[1]
			T2 = T_coeff[2]
			T3 = T_coeff[3]
			T4 = T_coeff[4]

			Ft = (T/T0)*(T0 + T1 * v + T2 * v^2 + T3 * v^3 + T4 * v ^ 4)
			if  Ft < 0:
				Ft = 0

			# Lift	
			Fl = 0.5 * rho * v[0] ^ 2 * Sref * CL

			# Drag 
			Fd = 0.5 * rho * v[0] ^ 2 * Sref * CD

			# Wheel Friction
			Fw = params['friction-coeff'] * ( mass * 9.81 - Fl - Ft * sin(radians(alpha)))
			if Fw < 0:
				Fw = 0


			F = []
			F.append(Ft * sin(radians(alpha)) - Fw - Fd)
			Fy = Fl - mass * g
			if Fy < 0:
				F.append(0)
			else:
				F.append(Fy)

			return F

		def calc_momentum_buildup(runway_length, mass, CL, CD, Sref, T_coef, T, b):
			''' Calculates the runway length of the aircraft w/ specified properties '''
			 # Mass is independent variable
			 # Runway length is dependent variable
			 # Newton's method varying mass and getting runway length

			 position = [0, 0]
			 velocity = [0, 0]
			 force = []
			 time = 0
			 dt = 0.001

			 while position[0] < runway_length || position[1] > 0:

			 	position[0] = position[0] + velocity[0] * dt
			 	position[1] = position[1] + velocity[1] * dt

			 	force = calc_total_force(v, CL, CD, Sref, T_coef, T, 0)

			 	velocity[0] = velocity[0] + force[0] * dt / mass
			 	velocity[1] = velocity[1] + force[1] * dt / mass

			 	time = time + dt

			 return position[0]

		# End of function declaring
		
			 	
