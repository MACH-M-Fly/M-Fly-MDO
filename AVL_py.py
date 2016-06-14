# AVL Python Wrapper
#
# Contains function calls for AVL as well as Geometry file writing functions
# Written by Beldon Lin
#
# NOTE: All arrays are strings, use float() or int() to convert to values
# 
# 
# geometry_config: Array containing information about geometry
# [ Name
#	#Mach
# 	#IYsym IZsym Zsym
#	#Sref Cref Bref
#	#Xref Yref Zref
# 	#Number-of-surface ]
#	#S1 Name
#	#!Nchordwse Cspace Nspanwise Sspace
#	#Component
#	#YDuplicate
#	#ANGLE
#	#SCALE
# 	#TRANSLATE
#	Number-of-sections
#	#S2 Name
#	#!Nchordwise Cspace Nspanwise Sspace
#	#Component
#	#YDuplicate
#	#ANGLE
#	#SCALE
# 	#TRANSLATE
#	Number-of-sections ......
#	....
#	#Sn Name
#	#!Nchordwse Cspace Nspanwise Sspace
#	#Component
#	#YDuplicate
#	#ANGLE
#	#SCALE
# 	#TRANSLATE
#	Number-of-sections ] 
# 	Note: Keep in this order, the resulting array should be n x 4 where n is any integer
#	
#	geometry: Contains array of information about section information (In the same order as geometry config array lists)
# 	[Xle Yle Zle Chord Ainc AFILE CLaf(not yet)...
#													]
#														
# 	run_parameters: Contains the run parameters for the run file (dictionary)
#	[name, Xcg,  alpha, beta, pb/2V ,qc/2V, rb/2V, camber, aileron, elevator, rudder, alpha (labeled +2), beta, pb/2V, qc/2V, rb/2V, CL, CDo, bank, elevation, heading, Mach, velocity, density, grav.acc., turn_rad.                              
# 	load_fac., X_cg, Y_cg, Z_cg, mass, Ixx, Iyy, Izz, Ixy, Iyz, Izx, visc CL_a, visc CL_u, visc CM_a, visc CM_u 	....]
#
#
#
#


class AVL():
	""" Main AVL running class """

	def __init__(self, name, geometry_config, geometry, run_parameters):
		self.name = name
		self.geometry_config = geometry_config
		self.geometry = geometry
		self.run_parameters = run_parameters

	def run_avl():
		# Need to change to a command file
		with open('avl_commands.run', 'w') as w:
			
		# LOAD avl geometry file
		w.write('LOAD '+str(self.name) + '\n');

		#Enter OPER
		os.system('OPER')
		os.system('X')	#Runs analysis the file




		os.system('./avl < avl_commands.run > avl_output.txt' )
	# All Geometry file related 
	def create_geometry_file():
		self.geometry



