'''
aero_AVL: Modifies the aircraft geometry and runs AVL to determine aerodynamic properties

0.2 Produces CL, CD, Sref, oswald








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


import settings

class aero_AVL(Component):
	""" Makes the appropriate run file and outputs the computed numbers """
	def __init__(self):

		super(aero_AVL, self).__init__()

		# self.add_param('taper', val=[1.0, 1.0, 1.0]) # taper ratio
		# self.add_param('b_w', val = 1.0) # Wingspan
		# self.add_param('chord_w', val = 1.6)

		# ----Wing Design Variables-----------
		for i in range(settings.WING):
			if settings.W['W'+str(i+1)][6]:
				key_start = 'wing_' + str(i+1) + '_'
				self.add_param(key_start+'chord', val = settings.W['W' + str(i+1)][2])
				self.add_param(key_start+'b', val = settings.W['W' + str(i+1)][3])
				for j in range(settings.W['W' + str(i+1)][4]):
					self.add_param(key_start+'taper_'+str(j+1), val = 1.0)
					self.add_param(key_start+'angle_'+str(j+1), val = 0.0)
					self.add_param(key_start+'dihedral_'+str(j+1), val = 0.0)
					self.add_param(key_start+'x_offset_'+str(j+1), val = 0.0)

		# ----H tail Design Variables---------
		for i in range(settings.H_TAIL):
			if settings.H['H'+str(i+1)][6]:
				key_start = 'h_tail_' + str(i+1) + '_'
				self.add_param(key_start+'chord', val =  settings.H['H' + str(i+1)][2])
				self.add_param(key_start+'b', val = settings.H['H' + str(i+1)][3])
				for j in range(settings.H['H' + str(i+1)][4]):
					self.add_param(key_start+'taper_'+str(j+1), val = 1.0)
					self.add_param(key_start+'angle_'+str(j+1), val = 0.0)
					self.add_param(key_start+'dihedral_'+str(j+1), val = 0.0)
					self.add_param(key_start+'x_offset_'+str(j+1), val = 0.0)

		# ----V tail Design Variables---------
		for i in range(settings.V_TAIL):
			if settings.V['V'+str(i+1)][7]:
				key_start = 'v_tail_' + str(i+1) + '_'
				self.add_param(key_start+'chord', val = settings.V['V' + str(i+1)][2])
				self.add_param(key_start+'b', val =  settings.V['V' + str(i+1)][3])
				for j in range(settings.V['V' + str(i+1)][4]):
					self.add_param(key_start+'taper_'+str(j+1), val = 1.0)
					self.add_param(key_start+'angle_'+str(j+1), val = 0.0)
					self.add_param(key_start+'dihedral_'+str(j+1), val = 0.0)
					self.add_param(key_start+'x_offset_'+str(j+1), val = 0.0)
					self.add_param(key_start+'y_offset_'+str(j+1), val = 0.0)

		# ---- Boom Design variables----------
		for i in range(settings.BOOM):
			key_start = 'boom_'+str(i+1) + '_'
			self.add_param(key_start+'length', val = settings.B['B'+str(i+1)])	


		self.add_output('CL', val=0.0)
		self.add_output('CD', val=0.0)
		self.add_output('Sref', val = 0.0)
		self.add_output('oswald', val = 0.0)
		self.add_output('boom_length', val = 0.0)



		

	def solve_nonlinear(self, params, unknowns, resids):
		AC_0 = settings.AC_0		
		current_AC_AVL = AVL(AC_0.name)
		print(AC_0.h_tail)
		print(AC_0.v_tail)
		#------Modify AC geometry----------------

		# Wing
		for i in range(AC_0.wing['Num']):
			if settings.W['W'+str(i+1)][6]:
				key_start = 'wing_' + str(i+1) 
				key_start2 = 'wing_' + str(i+1) + '_'
				AC_0.wing[key_start]['root_chord'] = params[key_start2 +'chord']
				AC_0.wing[key_start]['wingspan'] = params[key_start2 +'b']

				#-----collect taper, dihedral, x_offset, and angle into one array-------
				taper_w = []
				dihedral_w = []
				x_offset_w = []
				angle_w = []
				for j in range(AC_0.wing[key_start]['num_sections']):
					taper_w.append(params[key_start2+'taper_'+str(j+1)])
					dihedral_w.append(params[key_start2+'dihedral_'+str(j+1)])
					x_offset_w.append(params[key_start2+'x_offset_'+str(j+1)])
					angle_w.append(params[key_start2+'angle_'+str(j+1)])

				AC_0.wing[key_start]['taper'] = taper_w
				AC_0.wing[key_start]['angle'] = angle_w
				AC_0.wing[key_start]['X_offset'] = x_offset_w
				AC_0.wing[key_start]['dihedral'] = dihedral_w

		# H_tail
		for i in range(AC_0.h_tail['Num']):
			if settings.H['H'+str(i+1)][6]:
				key_start = 'h_tail_' + str(i+1) 
				key_start2 = 'h_tail_' + str(i+1) + '_'
				AC_0.h_tail[key_start]['root_chord'] = params[key_start2 +'chord']
				AC_0.h_tail[key_start]['wingspan'] = params[key_start2 +'b']

				#-----collect taper, dihedral, x_offset, and angle into one array-------
				taper_w = []
				dihedral_w = []
				x_offset_w = []
				angle_w = []
				for j in range(AC_0.h_tail[key_start]['num_sections']):
					taper_w.append(params[key_start2+'taper_'+str(j+1)])
					dihedral_w.append(params[key_start2+'dihedral_'+str(j+1)])
					x_offset_w.append(params[key_start2+'x_offset_'+str(j+1)])
					angle_w.append(params[key_start2+'angle_'+str(j+1)])

				AC_0.h_tail[key_start]['taper'] = taper_w
				AC_0.h_tail[key_start]['angle'] = angle_w
				AC_0.h_tail[key_start]['X_offset'] = x_offset_w
				AC_0.h_tail[key_start]['dihedral'] = dihedral_w

		# V_tail
		for i in range(AC_0.v_tail['Num']):
			if settings.V['V'+str(i+1)][7]:
				key_start = 'v_tail_' + str(i+1) 
				key_start2 = 'v_tail_' + str(i+1) + '_'
				AC_0.v_tail[key_start]['root_chord'] = params[key_start2 +'chord']
				AC_0.v_tail[key_start]['wingspan'] = params[key_start2 +'b']

				#-----collect taper, dihedral, x_offset, and angle into one array-------
				taper_w = []
				dihedral_w = []
				x_offset_w = []
				y_offset_w = []
				angle_w = []
				for j in range(AC_0.v_tail[key_start]['num_sections']):
					taper_w.append(params[key_start2+'taper_'+str(j+1)])
					dihedral_w.append(params[key_start2+'dihedral_'+str(j+1)])
					x_offset_w.append(params[key_start2+'x_offset_'+str(j+1)])
					y_offset_w.append(params[key_start2+'y_offset_'+str(j+1)])
					angle_w.append(params[key_start2+'angle_'+str(j+1)])

				AC_0.v_tail[key_start]['taper'] = taper_w
				AC_0.v_tail[key_start]['angle'] = angle_w
				AC_0.v_tail[key_start]['X_offset'] = x_offset_w
				AC_0.v_tail[key_start]['Y_offset'] = y_offset_w
				AC_0.v_tail[key_start]['dihedral'] = dihedral_w


		#-------Update Geometry file and run-----------
		AC_0.update_prop()
		AC_0.create_AVL_geometry()

		current_AC_AVL.run_avl_AoA(0)
		current_AC_AVL.read_aero_file()


	

		unknowns['CL'] = current_AC_AVL.coeffs['CLtot']
		unknowns['CD'] = current_AC_AVL.coeffs['CDtot']
		unknowns['Sref'] = current_AC_AVL.coeffs['Sref']
		unknowns['oswald'] = current_AC_AVL.coeffs['e']
		

	
		#print(aircraft.coeffs['CLtot'])
		# print('\n')
	
		
