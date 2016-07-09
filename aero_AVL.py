from __future__ import print_function
from openmdao.api import Component, Group, Problem

# Imported from Python standard
import sys
import os
import time
import math
import numpy
import AVL_py

class aero_AVL(Component):
	""" Makes the appropriate run file and outputs the computed numbers """
	def __init__(geometry, surface):

		super(aero_AVL, self).__init__(geometry, surface)

		self.add_param('taper', val=0.0) # taper ratio
		self.add_param('CL', val=0.0)


		# ==================================================================
		# Define starting geometry: (Change here depending on what you want)
		# ==================================================================
		# You can either parse a geometry file (future) or specify here
		# Array definition
		geometry_file_available = 0
		geometry = []
		sections = []
		if geometry_file_available == 0:
			geometry.append(0.0) # Mach
			geometry.append(0.0) # Iysm
			geometry.append(0.0) # IZsym
			geometry.append(0.0) # Zsym
			geometry.append( 14) # Sref (Planform Wing area)
			geometry.append(1.60) # Cref
			geometry.append(8.75) # Bref (wing span)
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
			geometry.append(0.0) # YDuplicate
			geometry.append(1.0) # XScale
			geometry.append(1.0) # YScale
			geometry.append(1.0) # Zscale
			geometry.append(4.0) # Number of sections in this surface

			## Surface Section (copy and paste and modify as many times as necessary)
			# Wing root
			sections.append(4) # Number of sections for this surface
			sections.append(0.0) # Xle
			sections.append(0.0) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('e420.dat') # AFILE
			# Aileron Start
			sections.append(4) # Number of sections for this surface
			sections.append(0.0) # Xle
			sections.append(2.62) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('e420.dat') # AFILE
			# Aileron End
			sections.append(4) # Number of sections for this surface
			sections.append(0.0) # Xle
			sections.append(4.37) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('e420.dat') # AFILE
			# Wing Tip
			sections.append(4) # Number of sections for this surface
			sections.append(0.0) # Xle
			sections.append(4.375) # Yle
			sections.append(0.0) # Zle
			sections.append(1.6) # Chord
			sections.append(2) # Ainc
			sections.append('e420.dat') # AFILE

		else
			# geometry_and_sections = read_geo()


		
		# Initializes an AVL object
		aircraft = AVL(geometry, sections)

	def solve_nolinear(self, params, unknowns, resids):
		#=========================================
		# Modify starting geometry according to taper, twist, dihedral, etc.
		#=========================================

		#TODO
		print('Taper ratio: ')
		print(params['taper'])
		print('\n')

		aircraft.update_geometry_results(geometry, sections)
		#=========================================
		# Run AVL with specified AoA
		#=========================================
		aircraft.create_geometry_file()
		aircraft.run_avl_AoA(0)
		aircraft.read_aero_file()

		unknowns['CL'] = aircraft.coeff['Cltot']

		
