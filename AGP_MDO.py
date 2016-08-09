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
from openmdao.api import ExecComp, Component, Group, Problem, IndepVarComp, ScipyOptimizer, ScipyGMRES
from openmdao.recorders.csv_recorder import CsvRecorder
from openmdao.drivers.pyoptsparse_driver import pyOptSparseDriver
# Imported from Python standard
import sys
import os
import time
import math
import numpy

# Modules
from aero_AVL import aero_AVL
from aero_MTOW import aero_MTOW
from struct_weight import struct_weight

class AGP_MDO(Group):

	def __init__(self):
		# add parameter
		super(AGP_MDO,self).__init__()

		
		# Design variables
		self.add('b_w', IndepVarComp('b_w', 5.0), promotes=['*']) # Wing Span 
		self.add('chord_w', IndepVarComp('chord_w',2.0), promotes=['*'])
		self.add('taper', IndepVarComp('taper', 0.35), promotes=['*']) # taper ratio
		
		# Add components
		self.add('aero_AVL', aero_AVL())
		self.add('aero_MTOW', aero_MTOW(), promotes = ['PAYLOAD'])
		# self.add('aero_CFD', aero_CFD());
		# self.add('struct_FEA', struct_FEA());
		# self.add('struct_LF', struct_LF());
		# self.add('geometry', geometry());
		# self.add('stability', stability());
		# self.add('sim_score', sim_score());
		# self.add('propulsion', propulsion());
		self.add('struct_weight', struct_weight())

		#=========================
		# Add Connections
		#=========================
		# (unknown, parameter)

		#Design variables
		self.connect('taper', ['aero_AVL.taper', 'struct_weight.taper'])
		self.connect('b_w', ['aero_AVL.b_w', 'struct_weight.b_w'])
		self.connect('chord_w', ['aero_AVL.chord_w', 'struct_weight.chord_w'])


		# aero_AVL
		self.connect('aero_AVL.CL', 'aero_MTOW.CL')
		self.connect('aero_AVL.CD', 'aero_MTOW.CD')
		self.connect('aero_AVL.Sref', 'aero_MTOW.Sref')

		# aero_MTOW
		self.connect('struct_weight.EW', 'aero_MTOW.EW')

		

		# Add Objective
		self.add('obj_comp', ExecComp('obj = PAYLOAD'), promotes=['*'] )
		# self.nl_solver = Newton()
		# self.nl_solver.options['alpha'] = 10000000.0
		# self.nl_solver.iprint = 1

		self.ln_solver = ScipyGMRES()

		# Add constraints
		#self.add('1', ExecComp('taper < 1'))

# Main routine
if __name__ == "__main__":

	# Initialize the problem
	top = Problem()
	
	top.root = AGP_MDO()
	top.driver = pyOptSparseDriver()
	top.driver.options['optimizer'] = 'ALPSO'
	#top.root.fd_options['force_fd'] = True	

	# Design variables
	top.driver.add_desvar('taper', lower=0.01, upper=1.0)
	top.driver.add_desvar('b_w', lower=2.0, upper=10.0 ) # Feet
	top.driver.add_desvar('chord_w', lower=0.5, upper=4.0)

	# Objective
	top.driver.add_objective('obj')

	# Add constraints

	# Add Recorder
	#recorder = CsvRecorder('AGP_CG')
	#recorder.options['record_params'] = True
	#recorder.options['record_metadata'] = False
	#top.driver.add_recorder(recorder)


	# Setup
	top.setup()
	time_start = time.time()

	# Initial values (either set default in each individual libraries or set them here)


	# Run 
	top.run()

	top.cleanup()

	print('\n')
	print("Optimization Time: " + str((time.time()-time_start)/3600) + "hours")
	print('\n')
	print('Wingspan: %f, Chord: %f, Taper: %f\n' % (top['b_w'], top['chord_w'], top['taper']))





