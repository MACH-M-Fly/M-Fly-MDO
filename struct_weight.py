'''
struct_weight.py: Currently only returns the weight of the aircraft based volume 








'''

from __future__ import print_function
from openmdao.api import Component, Group, Problem

# Imported from Python standard
import sys
import os
import time
import math
import numpy

import settings
density = 1.5/28.0#FILL IN

class struct_weight(Component):
	""" Calculates the empty weight of the aircraft """
	def __init__(self):

		super(struct_weight, self).__init__()

	
		self.add_output('EW', val = 0.0)
		
		

	def solve_nonlinear(self, params, unknowns, resids):

		#====================================
		# Trapezoidal shape approximation
		#====================================
		AC_0 = settings.AC_0
		print(AC_0.wing)
		AC_0.update_prop()
		Sref = AC_0.proper['Sref']
		volume = Sref * 1.0/12.0 
		mass = volume * density
		#print('Mass: '+str(mass))
		unknowns['EW'] = mass
		




			 	
