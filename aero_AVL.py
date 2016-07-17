'''
aero_AVL: Modifies the aircraft geometry and runs AVL to determine aerodynamic properties

0.2 Produces CL, CD, Sref








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

class aero_AVL(Component):
	""" Makes the appropriate run file and outputs the computed numbers """
	def __init__(self):

		super(aero_AVL, self).__init__()

		self.add_param('taper', val=0.0) # taper ratio

		self.add_output('CL', val=0.0)
		self.add_output('CD', val=0.0)
		self.add_output('Sref', val = 0.0)
		self.add_output('oswald', val = 0.0)
		self.add_output('B_w', val = 0.0)


		

	def solve_nonlinear(self, params, unknowns, resids):

		#=========================================
		# Initialize AVL Object
		#=========================================

		# ==================================================================
		# Define starting geometry: (Change here depending on what you want)
		# ==================================================================
		# You can either parse a geometry file (future) or specify here
		# Array definition
		root_chord = 1.6
		wing_span = 8.75
		Sref = (root_chord + (root_chord * params['taper'])) * (wing_span / 2) / 2
		geometry_file_available = 0
		geometry = []
		sections = []
		if geometry_file_available == 0:

			geometry.append('M-8_Wing')
			geometry.append(0.0) # Mach
			geometry.append(0) # Iysm
			geometry.append(0) # IZsym
			geometry.append(0) # Zsym
			geometry.append(Sref) # Sref (Planform Wing area)
			geometry.append(root_chord) # Cref
			geometry.append(wing_span) # Bref (wing span)
			geometry.append(0.296) #Xcg
			geometry.append(0) # Ycg
			geometry.append(0) #Zcy
			geometry.append(1) # Num sections

			### SURFACE (copy and paste and modift as many times as necessary)
			geometry.append('Wing') # Name of surface
			geometry.append(10) # Nchordwise 
			geometry.append(1.0) # Cspace
			geometry.append(30) # Nspanwise
			geometry.append(-2.0) # Sspace
			geometry.append(1) # COMPONENT
			geometry.append(0.0) # YDuplicate
			geometry.append(0.0) # Angle
			geometry.append(1.0) # XScale
			geometry.append(1.0) # YScale
			geometry.append(1.0) # Zscale
			geometry.append(0.0) # Translate X
			geometry.append(0.0) # Translate Y
			geometry.append(0.0) # Translate Z
			geometry.append(4) # Number of sections in this surface

			## Surface Section (copy and paste and modify as many times as necessary)
			# Wing root
			sections.append(0.0) # Xle
			sections.append(0.0) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('ht22.dat') # AFILE
			# Aileron Start
			sections.append(0.0) # Xle
			sections.append(2.62) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('ht22.dat') # AFILE
			# Aileron End
			sections.append(0.0) # Xle
			sections.append(4.37) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('ht22.dat') # AFILE
			# Wing Tip
			sections.append(0.0) # Xle
			sections.append(4.375) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('ht22.dat') # AFILE

	#	else:
			# geometry_and_sections = read_geo()


		
		# Initializes an AVL object
		aircraft = AVL(geometry, sections)

		#=========================================
		# Modify starting geometry according to taper, twist, dihedral, etc.
		#=========================================

		#TODO
		# print('Taper ratio: ')
		# print(params['taper'])
		# print('\n')

		# Modify taper
		section_num = aircraft.geometry_config['surface_0_section_num']
		
		wingspan = aircraft.geometry_config['surface_0_section_data']['section_'+str(section_num-1)+'_Yle']
		
		root_chord = aircraft.geometry_config['surface_0_section_data']['section_0_Chord']

		for num in range(section_num):
		
			section_location = aircraft.geometry_config['surface_0_section_data']['section_'+str(num)+'_Yle']
			aircraft.geometry_config['surface_0_section_data']['section_'+str(num)+'_Chord'] = root_chord * (params['taper']-1)/ wingspan * section_location + root_chord

		#=========================================
		# Rerun AVL with specified AoA
		#=========================================
		aircraft.create_geometry_file()
		
		aircraft.run_avl_AoA(0)
		
		aircraft.read_aero_file()

		#=========================================
		# Send aero parameters back
		#=========================================
		
		unknowns['CL'] = aircraft.coeffs['CLtot']
		unknowns['CD'] = aircraft.coeffs['CDtot']
		unknowns['Sref'] = aircraft.coeffs['Sref']
		unknowns['oswald'] = aircraft.coeffs['e']
		unknwons['B_w'] = aircraft.coeffs['Bref']

	
		#print(aircraft.coeffs['CLtot'])
		print('\n')
	
		
