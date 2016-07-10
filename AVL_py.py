
''' AVL Python Wrapper

 AVL Interface Python library

 Written for M-Fly MDO/scripting/analysis purposes only 
------------------------------------------------------------------
	DEVELOPED BY
------------------------------------------------------------------

Beldon Lin

 
------------------------------------------------------------------
	INPUTS
------------------------------------------------------------------
NOTE: All arrays are strings, use float() or int() to convert to values

 
 geometry_config: Array containing information about geometry
 [ Name
	#Mach
 	#IYsym IZsym Zsym
	#Sref Cref Bref
	#Xref Yref Zref
 	#Number-of-surface 
	#S1 Name
	#!Nchordwse Cspace Nspanwise Sspace
	#Component
	#YDuplicate
	#ANGLE
	#SCALE
 	#TRANSLATE
	Number-of-sections
	#S2 Name
	#!Nchordwise Cspace Nspanwise Sspace
	#Component
	#YDuplicate
	#ANGLE
	#SCALEX
	#SCALEY
	#SCALEZ
 	#TRANSLATEX
 	#TRANSLATEY
	#TRANSLATEZ
	Number-of-sections ......
	....
	#Sn Name
	#!Nchordwse Cspace Nspanwise Sspace
	#Component
	#YDuplicate
	#ANGLE
	#SCALE
 	#TRANSLATE
	Number-of-sections ] 
 	Note: Keep in this order, the resulting array should be n x 4 where n is any integer
	
	geometry: Contains array of information about section information (In the same order as geometry config array lists), 
	NOTE: all strings
 	[Xle Yle Zle Chord Ainc AFILE CLaf(not yet)...
													]
														
 	run_parameters: Contains the run parameters for the run file (dictionary)
	[name, Xcg,  alpha, beta, pb/2V ,qc/2V, rb/2V, camber, aileron, elevator, rudder, alpha (labeled +2), beta, pb/2V, qc/2V, rb/2V, CL, CDo, bank, elevation, heading, Mach, velocity, density, grav.acc., turn_rad.                              
 	load_fac., X_cg, Y_cg, Z_cg, mass, Ixx, Iyy, Izz, Ixy, Iyz, Izx, visc CL_a, visc CL_u, visc CM_a, visc CM_u 	....]

'''

import os
import sys

class AVL():
	""" Main AVL running class """

	def __init__(self,  geometry_config, geometry):
		self.name = geometry_config[0]
		self.geometry = {}
		self.geometry_config = self.parse_geometry_config(geometry_config, geometry, self.geometry) #Dictionary of geometry config values
		# self.geometry = parse_geoemtry_surfaces(geometry) # Dictionary of all surface properties
		print(self.geometry)
		self.create_geometry_file()
		self.run_avl_AoA(0) # Initialy runs at an angle of attack of to give AoA = 0 properties
		self.coeffs = self.read_aero_file()

	def run_avl_AoA(self, AoA):
		''' Runs AVL at a certain angle of attack and saves output into avl_output.txt'''
		# Need to change to a command file

		# Change directories into AVL folder

		# Remove previous system files
		#os.system('cd AVL')
		#if os.path.exists(str(self.name)+'_total_forces.txt'):
		#	os.remove(str(self.name)+'_total_forces.txt')
		#if os.path.exists(str(self.name)+'_force_elements.txt'):
		#	os.remove(str(self.name)+'_force_elements.txt')
		#os.system('cd ..')
		


		with open('avl_commands.run', 'w') as w:
			
			# LOAD avl geometry file
			w.write('LOAD '+str(self.name) + '.avl\n')
			# enter OPER mode
			w.write('OPER\n')
			# Modify run case
			w.write('A\n')
			w.write('A\n')
			w.write(str(AoA)+'\n')
			# Run run case
			w.write('X\n')
			# Produce Total Forces file
			w.write('FT\n')
			w.write(str(self.name)+'_total_forces.txt'+'\n')
			w.write('\n')

			#Produce force element file
			w.write('FE\n')
			w.write(str(self.name)+'_force_elements.txt'+'\n')
			w.write('\n')

			#Exit
			w.write('\n')
			w.write('QUIT')



		

		os.system('./avl < avl_commands.run > avl_output.txt' )
	
	def parse_geometry_config(self, geometry_config, geometry, section_geometry):
		'''
		Reads AVL configuration array into a much more usable dictionary for processing purposes
		'''
		geo_config_dict = {'Name': geometry_config[0]}
		geo_config_dict['Mach'] = geometry_config[1]
		geo_config_dict['IYsym'] = geometry_config[2]
		geo_config_dict['IZsym'] = geometry_config[3]
		geo_config_dict['Zsym'] = geometry_config[4]
		geo_config_dict['Sref'] = geometry_config[5]
		geo_config_dict['Cref'] = geometry_config[6]
		geo_config_dict['Bref'] = geometry_config[7]
		geo_config_dict['Xref'] = geometry_config[8]
		geo_config_dict['Yref'] = geometry_config[9]
		geo_config_dict['Zref'] = geometry_config[10]
		geo_config_dict['Num_Surfaces'] =  geometry_config[11]

		section_num = 1;
		#Iterate through the number of surfaces present
		for i in range(geo_config_dict['Num_Surfaces']):
			surface_num = i 
			geo_config_dict['surface_'+str(surface_num)+'_name'] = geometry_config[12+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_Nchordwise'] = geometry_config[13+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_Cspace'] = geometry_config[14+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_Nspanwise'] = geometry_config[15+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_Sspace'] = geometry_config[16+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_Component'] = geometry_config[17+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_YDuplicate'] = geometry_config[18+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_Angle'] = geometry_config[19+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_ScaleX'] = geometry_config[20+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_ScaleY'] = geometry_config[21+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_ScaleZ'] = geometry_config[22+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_TranslateX'] = geometry_config[23+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_TranslateY'] = geometry_config[24+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_TranslateZ'] = geometry_config[25+(i-1)*16]
			geo_config_dict['surface_'+str(surface_num)+'_section_num'] = geometry_config[26+(i-1)*16]
			geo_section = dict()

			for j in range(geo_config_dict['surface_'+str(surface_num)+'_section_num']):
				geo_section['section_'+str(i)+'_Xle'] = geometry[0+(i-1)*6+(section_num-1)*6]
				geo_section['section_'+str(i)+'_Yle'] = geometry[1+(i-1)*6+(section_num-1)*6]
				geo_section['section_'+str(i)+'_Zle'] = geometry[2+(i-1)*6+(section_num-1)*6]
				geo_section['section_'+str(i)+'_Chord'] = geometry[3+(i-1)*6+(section_num-1)*6]
				geo_section['section_'+str(i)+'_Ainc'] = geometry[4+(i-1)*6+(section_num-1)*6]
				geo_section['section_'+str(i)+'_AFILE'] = geometry[5+(i-1)*6+(section_num-1)*6]


			geo_config_dict['surface_'+str(surface_num)+'_section_data'] = geo_section

			section_num = section_num + geometry_config[26+(i-1)*16]*6

		section_geometry = geo_section

		return geo_config_dict

	# All Geometry file related 
	
	def create_geometry_file(self):
		with open(str(self.name)+'.avl', 'w') as geo:

			# title
			geo.write(str(self.name))

			#Initial first 4 lines
			geo.write('\n#Mach\n')
			geo.write(str(self.geometry_config['Mach'])+'\n')
			geo.write('#IYsym\tIZsym\tZsym\n')
			geo.write(str(self.geometry_config['IYsym'])+'\t'+str(self.geometry_config['IZsym'])+'\t'+str(self.geometry_config['Zsym']) + '\n\n')
			geo.write('#Sref\tCref\tBref\n')
			geo.write(str(self.geometry_config['Sref'])+'\t'+str(self.geometry_config['Yref'])+'\t'+str(self.geometry_config['Bref']) + '\n\n')
			geo.write('#Xref\tYref\tZref\n')
			geo.write(str(self.geometry_config['Xref'])+'\t'+str(self.geometry_config['Yref'])+'\t'+str(self.geometry_config['Zref'])+'\n\n')
			geo.write('#---------------------------------------------------------\n')

			for i in range(self.geometry_config['Num_Surfaces']):
				surface_num = i
				geo.write('SURFACE\n')
				geo.write('')
				geo.write('!Nchordwise\tCspace\tNspanwise\tSspace\n')
				geo.write(str(self.geometry_config['surface_'+str(surface_num)+'_Nchordwise'])+'\t'+str(self.geometry_config['surface_'+str(surface_num)+'_Cspace'])+'\t'+str(self.geometry_config['surface_'+str(surface_num)+'_Nspanwise'])+'\t'+str(self.geometry_config['surface_'+str(surface_num)+'_Sspace'])+'\n')
				geo.write('COMPONENT\n')
				geo.write(str(self.geometry_config['surface_'+str(surface_num)+'_Component'])+'\n')
				geo.write('YDUPLICATE\n')
				geo.write(str(self.geometry_config['surface_'+str(surface_num)+'_YDuplicate'])+'\n')
				geo.write('ANGLE\n')
				geo.write(str(self.geometry_config['surface_'+str(surface_num)+'_Angle'])+'\n')
				geo.write('SCALE\n')
				geo.write(str(self.geometry_config['surface_'+str(surface_num)+'_ScaleX'])+'\t'+str(self.geometry_config['surface_'+str(surface_num)+'_ScaleY'])+'\t'+str(self.geometry_config['surface_'+str(surface_num)+'_ScaleZ'])+'\n')
				geo.write('TRANSLATE\n')
				geo.write(str(self.geometry_config['surface_'+str(surface_num)+'_TranslateX'])+'\t'+str(self.geometry_config['surface_'+str(surface_num)+'_TranslateY'])+'\t'+str(self.geometry_config['surface_'+str(surface_num)+'_TranslateZ'])+'\n')

				for j in range(self.geometry_config['surface_'+str(surface_num)+'_section_num']):
					geo.write('SECTION\n')
					geo.write('#Xle\tYle\tZle\tChord\tAinc\tNspanwise\tSspace\n')
					geo.write(str(self.geometry['section_'+str(j)+'_Xle'])+'\t'+str(self.geometry['section_'+str(j)+'_Yle'])+'\t'+str(self.geometry['section_'+str(j)+'_Zle'])+'\t'+str(self.geometry['section_'+str(j)+'Chord'])+'\t'+str(self.geometry['section_'+str(j)+'_Ainc'])+'\n')
					geo.write('AFILE\n')
					geo.write(str(self.geometry['section_'+str(j)+'_AFILE'])+'\n\n')

		return	


	def read_aero_file(self):
		# with open(str(name)++'_total_forces.txt') as read_force_file:
		# 	line = ''
		# 	while True:
		
		aero_init = open(str(self.name)+'_total_forces.txt').read().split()
		length_aero = len(aero_nit)
		coeff_dict = dict()

		for i in range(length_aero):
			if aero_init[i] == '=':
				coeff_dict[aero_init[i-1]] = coeff_dict[aero_init[i+1]]
		return coeff_dict

	def update_geometry_results(self, geometry_config, geometry):
		''' Updates all data with new geometry and aerdynamic results'''
		self.name = geometry_config[0]
		self.geometry_config = parse_geometry_config(geometry_config) #Dictionary of geometry config values
		self.geometry = parse_geoemtry_surfaces(geometry) # Dictionary of all surface properties
		self.run_avl_AoA(0) # Initialy runs at an angle of attack of to give AoA = 0 properties
		self.coeffs = read_aero_file()

	# FUTURE FUNCTIONS
#	def read_geometry_file(filename):
		
#	def read_force_elements_results():
#	def read_stability_results():
#	def run_avl_stability():
#	def add_section(surface, starting_section, ending_section):







