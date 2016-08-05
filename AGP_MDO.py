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
from openmdao.api import ExecComp, Component, Group, Problem, IndepVarComp, ScipyOptimizer
#from openmdao.drivers.pyoptsparse_driver import pyOptSparseDriver
# Imported from Python standard
import sys
import os
import time
import math
import numpy

# Modules
from aero_AVL import aero_AVL
from aero_MTOW import aero_MTOW

class AGP_MDO(Group):

	def __init__(self):
		# add parameter
		super(AGP_MDO,self).__init__()

		
		# Design variables
		#self.add('b_wing', IndepVarcomp('b_wing', 2.0)) # Wing Span 
		self.add('taper', IndepVarComp('taper', 0.25), promotes=['*']) # taper ratio
		
		# Add components
		self.add('aero_AVL', aero_AVL(), promotes=['*'])
		self.add('aero_MTOW', aero_MTOW(), promotes=['*'])
		# self.add('aero_CFD', aero_CFD());
		# self.add('struct_FEA', struct_FEA());
		# self.add('struct_LF', struct_LF());
		# self.add('geometry', geometry());
		# self.add('stability', stability());
		# self.add('sim_score', sim_score());
		# self.add('propulsion', propulsion());

		#=========================
		# Add Connections
		#=========================

		#Design variables
		self.connect('taper.taper', 'aero_AVL.taper')

		# aero_AVL
		#self.connect('aero_MTOW.CL', 'aero_AVL.CL')
		#self.connect('aero_AVL.CD', 'aero_MTOW.CD')
		#self.connect('aero_AVL.Sref', 'aero_MTOW.Sref')
		#self.connect('aero_AVL.B_w', 'aero_MTOW.b')


		# Add Objective
		self.add('obj_comp', ExecComp('obj = MTOW'), promotes=['*'] )
		# self.nl_solver = Newton()
		# self.nl_solver.options['alpha'] = 10000000.0
		# self.nl_solver.iprint = 1

		#self.ln_solver = ScipyGMRES()

		# Add constraints
		# self.add('1', ExecComp('taper <'))

# Main routine
if __name__ == "__main__":

	# Initialize the problem
	top = Problem()
	
	top.root = AGP_MDO()
	top.driver = ScipyOptimizer()
	top.driver.options['optimizer'] = 'SLSQP'
	top.root.fd_options['force_fd'] = True	

	# Design variables
	top.driver.add_desvar('taper', lower=0.01, upper=0.5)

	# Objective
	top.driver.add_objective('obj')

	# Add constraints

	# Add Recorder


	# Setup
	top.setup()
	time_start = time.time()

	# Initial values (either set default in each individual libraries or set them here)

	# Run 
	top.run()







