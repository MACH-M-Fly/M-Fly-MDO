# Main aircraft configuration File
# This file is where the aircraft configuration is interpreted and modified
# 
'''
Work that still needs to be done:

- Fueselage (slender body)
- Fueselage (collection of surfaces)
- Component surfaces
- Control surfaces
- Mass declaration










'''
from AC_Config import AC

def init(filename):

	#------Read configuration file----------------
	geo_init = open('/Input/' + str(filename)).read().split()
	length_aero = len(geo_init)
	coeff_dict = dict()
	for i in range(length_aero):
			if aero_init[i] == '=':
				coeff_dict[aero_init[i-1]] = aero_init[i+1]
	
	#-----------Configuration details--------------

	global AIRCRAFT_NAME
	AIRCRAFT_NAME = coeff_dict['AIRCRAFT_NAME']

	global WING
	WING = coeff_dict['WING']

	global H_TAIL
	H_TAIL = coeff_dict['H_TAIL']

	global V_TAIL
	V_TAIL = coeff_dict['V_TAIL']

	global BOOM
	BOOM = coeff_dict['BOOM']

	#-------- Wing ----------------------------
	global W
	for i in range(WING):
		key_start = 'WING'+str(i+1)
		W = {}

		#Initial starting points
		W_0 = []
		W_0.append(coeff_dict[key_start+'_Name'])
		W_0.append(coeff_dict['AIRFOIL_INIT_'+key_start])
		W_0.append(coeff_dict['ROOT_CHORD_INIT_'+key_start])
		W_0.append(coeff_dict['WINGSPAN_INIT_'+key_start])
		W_0.append(coeff_dict[key_start+'_Num_Sections'])
		W_0.append(coeff_dict['X_OFFSET_INIT'+key_start])
		W_0.append(coeff_dict[key_start + 'Optimize'])
		W['W'+str(i+1)] = W_0

		# Constraints
		W_c = {}
		W_c[key_start+'_TAPER_MAX'] = coeff_dict[key_start+'_TAPER_MAX']
		W_c[key_start+'_TAPER_MIN'] = coeff_dict[key_start+'_TAPER_MIN']
		W_c[key_start+'_ANGLE_MAX'] = coeff_dict[key_start+'_ANGLE_MAX']
		W_c[key_start+'_ANGLE_MIN'] = coeff_dict[key_start+'_ANGLE_MIN']
		W_c[key_start+'_DIHEDRAL_MAX'] = coeff_dict[key_start+'_DIHEDRAL_MAX']
		W_c[key_start+'_DIHEDRAL_MIN'] = coeff_dict[key_start+'_DIHEDRAL_MIN']
		W_c[key_start+'_X_OFFSET_MAX'] = coeff_dict[key_start+'_X_OFFSET_MAX']
		W_c[key_start+'_X_OFFSET_MIN'] = coeff_dict[key_start+'_X_OFFSET_MIN']
		W_c[key_start+'_CHORD_MIN'] = coeff_dict[key_start+'_CHORD_MIN'] 
		W_c[key_start+'_CHORD_MAX'] = coeff_dict[key_start+'_CHORD_MAX']
		W_c[key_start+'_WINGSPAN_MIN'] = coeff_dict[key_start+'_WINGSPAN_MIN']
		W_c[key_start+'_WINGSPAN_MAX'] = coeff_dict[key_start+'_WINGSPAN_MAX']
		W['W'+str(i+w)+'c'] = W_c


	#-------- Vertical Tail -------------------
	global V
	for i in range(V_TAIL):
		key_start = 'V_TAIL'+str(i+1)
		V = {}

		#Initial starting points
		V_0 = []
		V_0.append(coeff_dict[key_start+'_Name'])
		V_0.append(coeff_dict['AIRFOIL_INIT_'+key_start])
		V_0.append(coeff_dict['ROOT_CHORD_INIT_'+key_start])
		V_0.append(coeff_dict['WINGSPAN_INIT_'+key_start])
		V_0.append(coeff_dict[key_start+'_Num_Sections'])
		V_0.append(coeff_dict['X_OFFSET_INIT'+key_start])
		V_0.append(coeff_dict['Z_OFFSET_INIT'+key_start])
		V_0.append(coeff_dict[key_start + 'Optimize'])

		V['V'+str(i+1)] = V_0

		# Constraints
		V_c = {}
		V_c[key_start+'_TAPER_MAX'] = coeff_dict[key_start+'_TAPER_MAX']
		V_c[key_start+'_TAPER_MIN'] = coeff_dict[key_start+'_TAPER_MIN']
		V_c[key_start+'_ANGLE_MAX'] = coeff_dict[key_start+'_ANGLE_MAX']
		V_c[key_start+'_ANGLE_MIN'] = coeff_dict[key_start+'_ANGLE_MIN']
		V_c[key_start+'_DIHEDRAL_MAX'] = coeff_dict[key_start+'_DIHEDRAL_MAX']
		V_c[key_start+'_DIHEDRAL_MIN'] = coeff_dict[key_start+'_DIHEDRAL_MIN']
		V_c[key_start+'_X_OFFSET_MAX'] = coeff_dict[key_start+'_X_OFFSET_MAX']
		V_c[key_start+'_X_OFFSET_MIN'] = coeff_dict[key_start+'_X_OFFSET_MIN']
		V_c[key_start+'_Y_OFFSET_MAX'] = coeff_dict[key_start+'_Y_OFFSET_MAX']
		V_c[key_start+'_Y_OFFSET_MIN'] = coeff_dict[key_start+'_Y_OFFSET_MIN']
		V_c[key_start+'_CHORD_MIN'] = coeff_dict[key_start+'_CHORD_MIN'] 
		V_c[key_start+'_CHORD_MAX'] = coeff_dict[key_start+'_CHORD_MAX']
		V_c[key_start+'_WINGSPAN_MIN'] = coeff_dict[key_start+'_WINGSPAN_MIN']
		V_c[key_start+'_WINGSPAN_MAX'] = coeff_dict[key_start+'_WINGSPAN_MAX']
		V['V'+str(i+w)+'c'] = W_c	
	#-------- Horizontal Tail -----------------
	global H
	for i in range(H_TAIL):
		key_start = 'H_TAIL'+str(i+1)
		H = {}

		#Initial starting points
		H_0 = []
		H_0.append(coeff_dict[key_start+'_Name'])
		H_0.append(coeff_dict['AIRFOIL_INIT_'+key_start])
		H_0.append(coeff_dict['ROOT_CHORD_INIT_'+key_start])
		H_0.append(coeff_dict['WINGSPAN_INIT_'+key_start])
		H_0.append(coeff_dict[key_start+'_Num_Sections'])
		H_0.append(coeff_dict['X_OFFSET_INIT'+key_start])
		H_0.append(coeff_dict[key_start + 'Optimize'])

		H['H'+str(i+1)] = H_0

		# Constraints
		H_c = {}
		H_c[key_start+'_TAPER_MAX'] = coeff_dict[key_start+'_TAPER_MAX']
		H_c[key_start+'_TAPER_MIN'] = coeff_dict[key_start+'_TAPER_MIN']
		H_c[key_start+'_ANGLE_MAX'] = coeff_dict[key_start+'_ANGLE_MAX']
		H_c[key_start+'_ANGLE_MIN'] = coeff_dict[key_start+'_ANGLE_MIN']
		H_c[key_start+'_DIHEDRAL_MAX'] = coeff_dict[key_start+'_DIHEDRAL_MAX']
		H_c[key_start+'_DIHEDRAL_MIN'] = coeff_dict[key_start+'_DIHEDRAL_MIN']
		H_c[key_start+'_X_OFFSET_MAX'] = coeff_dict[key_start+'_X_OFFSET_MAX']
		H_c[key_start+'_X_OFFSET_MIN'] = coeff_dict[key_start+'_X_OFFSET_MIN']
		H_c[key_start+'_CHORD_MIN'] = coeff_dict[key_start+'_CHORD_MIN'] 
		H_c[key_start+'_CHORD_MAX'] = coeff_dict[key_start+'_CHORD_MAX']
		H_c[key_start+'_WINGSPAN_MIN'] = coeff_dict[key_start+'_WINGSPAN_MIN']
		H_c[key_start+'_WINGSPAN_MAX'] = coeff_dict[key_start+'_WINGSPAN_MAX']
		H['H'+str(i+1)+'c'] = H_c	

	#-------- Boom ----------------------------
	global B
	for i in range(BOOM):
		key_start = 'BOOM'+str(i+1)
		B = {}

		B_0 = []
		B_0.append(coeff_dict['DENSITY_INIT_'+key_start])
		B_0.append(coeff_dict['LENGTH_INIT_'+key_start])

		B['B'+str(i+1)] = B_0

		B_c = {}
		B_c[key_start+'_DENSITY_MAX'] = coeff_dict[key_start+'_DENSITY_MAX']
		B_c[key_start+'_DENSITY_MIN'] = coeff_dict[key_start+'_DENSITY_MIN']
		B_c[key_start+'_LENGTH_MAX'] = coeff_dict[key_start+'_LENGTH_MAX']
		B_c[key_start+'_LENGTH_MIN'] = coeff_dict[key_start+'_LENGTH_MIN']
		B['B'+str(i+1)+'c'] = B_c
		

	global AC_0
	AC_0 = AC(AIRCRAFT_NAME)

	for i in range(WING):
		Wing = W['W'+str(i+1)]
		AC_0.add_wing(Wing[0], Wing[1], Wing[2], Wing[3], Wing[4], Wing[5])
	for i in range(H_TAIL):
		H_tail = H['H'+str(i+1)]
		AC_0.add_h_tail(H_tail[0], H_tail[1], H_tail[2], H_tail[3], H_tail[4], 3)
	for i in range(V_TAIL):
		V_tail = V['V'+str(i+1)]
		AC_0.add_v_tail(V_tail[0], V_tail[1], V_tail[2], V_tail[3], V_tail[4], 6)
	for i in range(BOOM):
		boom = B['B'+str(i+1)]
		AC_0.add_boom(boom[0], boom[1])
	
		


