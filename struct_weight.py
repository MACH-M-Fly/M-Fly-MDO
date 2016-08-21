'''
struct_weight.py: Currently only returns the weight of the wing based on past wing density








'''

from __future__ import print_function
from openmdao.api import Component, Group, Problem

# Imported from Python standard
import sys
import os
import time
import math
import numpy


density = 1.5/28#FILL IN

class struct_weight(Component):
	""" Calculates the empty weight of the aircraft """
	def __init__(self):

		super(struct_weight, self).__init__()

	
		self.add_output('EW', val = 0.0)
		
		

	def solve_nonlinear(self, params, unknowns, resids):

		#====================================
		# Trapezoidal shape approximation
		#====================================

		top = params['chord_w']
		end = params['chord_w'] * params['taper'][3]
		airfoil_CS = params['chord_w'] * (2.0/12.0)

		volume = (top + end) * (params['b_w'] / 2.0) * airfoil_CS
		mass = volume * density
		print('Mass: '+str(mass))
		unknowns['EW'] = mass
		




			 	
