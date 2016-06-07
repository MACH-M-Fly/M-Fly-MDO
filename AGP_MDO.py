# Aircraft Geometry and Performance Optimzer (AGPO)
#
# Multi-disciplinary Optimization (MDO) program developed for M-Fly that does low-fidelity aerostructural, power systems, and thrust optimization
# as well as geometric shape optimization for wing
#
# written by Beldon Lin - Advanced Class Chief Engineer, M-Fly 2016-2017
# beldon@umich.edu
#
#	Version 0.1 
#		- Integrated AVL
#		- Optimized taper ratio for given airfoil
#
#
#
#

# Imported from OpenMDAO Library
from __future__ import print_function
from openmdao.api import Component, Group, Problem, IndepVarComp

# Imported from Python standard
import sys
import os
import time
import math
import numpy

class AGP_MDO(Group):

	def __init__(self):
		# add parameter
		super(AGP_MDO,self).__init__()
		# Initial guesses for parameters
		self.add('b_wing', IndepVarcomp('b_wing', 2.0)) # Wing Span 
		self.add('taper', IndepVarcomp('taper', 1.0)) # taper ratio

		# Add components
		self.add('aero_AVL', aero_AVL());
		# self.add('aero_CFD', aero_CFD());
		# self.add('struct_FEA', struct_FEA());
		# self.add('struct_LF', struct_LF());
		# self.add('geometry', geometry());
		# self.add('stability', stability());
		# self.add('sim_score', sim_score());
		# self.add('propulsion', propulsion());

		# self.add('')

# Main routine
if __name __ == "__main__":

