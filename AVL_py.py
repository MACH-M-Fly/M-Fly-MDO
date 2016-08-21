
''' AVL Python Wrapper

 AVL Interface Python library

 Written for M-Fly MDO/scripting/analysis purposes only 

'''

import os
import sys

class AVL():
	""" Main AVL running class """

	def __init__(self,  name):
		self.name = name
		# self.geometry_config = self.parse_geometry_config(geometry_config, geometry) #Dictionary of geometry config values
		# # self.geometry = parse_geoemtry_surfaces(geometry) # Dictionary of all surface properties
		# self.create_geometry_file()
		# # self.run_avl_AoA(0) # Initialy runs at an angle of attack of to give AoA = 0 properties
		self.coeffs = {}# self.read_aero_file()

	def run_avl_AoA(self, AoA):
		''' Runs AVL at a certain angle of attack and saves output into avl_output.txt'''
		# Need to change to a command file

		# Change directories into AVL folder

		# Remove previous system files
		#os.system('cd AVL')
		if os.path.exists(str(self.name)+'_total_forces.txt'):
			os.remove(str(self.name)+'_total_forces.txt')
		if os.path.exists(str(self.name)+'_force_elements.txt'):
			os.remove(str(self.name)+'_force_elements.txt')
		#os.system('cd ..')
		


		with open('avl_commands.run', 'w') as w:
			
			# LOAD avl geometry file
			w.write('LOAD '+str(self.name) + '.avl\r\n')
			# enter OPER mode
			w.write('OPER\r\n')
			# Modify run case
			w.write('A\r\n')
			w.write('A\r\n')
			w.write(str(AoA)+'\r\n')
			# Run run case
			w.write('X\r\n')
			# Produce Total Forces file
			w.write('FT\r\n')
			w.write(str(self.name)+'_total_forces.txt'+'\r\n')
			

			#Produce force element file
			w.write('FE\r\n')
			w.write(str(self.name)+'_force_elements.txt'+'\r\n')
			w.write('\r\n')

			#Exit
			w.write('\r\n')
			w.write('QUIT')

			w.close()



		# print('Running AVL\r\n')

		os.system('./avl < avl_commands.run > avl_output.txt' )


	def read_aero_file(self):
		# with open(str(name)++'_total_forces.txt') as read_force_file:
		# 	line = ''
		# 	while True:
		
		aero_init = open(str(self.name)+'_total_forces.txt').read().split()
		#print(aero_init)
		length_aero = len(aero_init)
		coeff_dict = dict()

		for i in range(length_aero):
			if aero_init[i] == '=':
				coeff_dict[aero_init[i-1]] = aero_init[i+1]
				# if aero_init[i-1] == 'CLtot':
				# 	print(aero_init[i+1])
				# 	print('\n')
		self.coeffs = coeff_dict
		return 

]

	# FUTURE FUNCTIONS	
#	def read_force_elements_results():
#	def read_stability_results():
#	def run_avl_stability():
#





