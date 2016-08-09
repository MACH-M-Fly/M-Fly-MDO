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

density = 1.5/28#FILL IN

class struct_weight(Component):
	""" Calculates the empty weight of the aircraft """
	def __init__(self):

		super(struct_weight, self).__init__()

		self.add_param('taper', val=0.0)
		self.add_param('b_w', val=1.0)
		self.add_param('chord_w', val=1.6)

		self.add_output('EW', val = 0.0)
		
		

	def solve_nonlinear(self, params, unknowns, resids):

		#====================================
		# Trapezoidal shape approximation
		#====================================

		top = params['chord_w']
		end = params['chord_w'] * params['taper']
		airfoil_CS = params['chord_w'] * (2.0/12.0)

		volume = (top + end) * (params['b_w'] / 2.0) * airfoil_CS
		mass = volume * density
		print('Mass: '+str(mass))
		unknowns['EW'] = mass
		




			 	
