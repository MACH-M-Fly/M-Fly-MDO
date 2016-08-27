# Main aircraft configuration File
# This file is where the aircraft configuration is interpreted and modified
# 
from AC_Config import AC

def init():
	#================================================================
	# Aircraft configuration (should become a file reading procedure)
	#================================================================

	global AIRCRAFT_NAME = 'new_AC'

	#----------------- Wing(s) --------------------------------------
	# Number of wings
	global WING = 1 

	# Number of wing sections
	global WING_SEC = 10

	# Wing Initial Condition
	# name, airfoil, root chord, wing span, number of sections, X offset
	W1 = ['Wing1', 'E420.dat', 1.6, 5, WING_SEC, 3]

	# combine all data
	W = {'W1' : W1}

	#----------------- H-Tail (s) -----------------------------------
	# Number of horizontal tails
	global H_TAIL = 1

	# Number of sections
	global H_SEC = 2

	# Horizontal Tail Initial Condition
	H1 = ['H_tail1', 'E420.dat', 1, 2, H_SEC]

	H = {'H1': H1}

	#----------------- V-Tail (s) -----------------------------------
	# Number of vertical tails
	global V_TAIL = 1

	# Number of vertical tail sections
	global V_SEC = 2

	# Vertical Tail Initial Conditions
	V1 = ['V_tail1', 'E420.dat', 0.5,3,V_SEC]

	V = {'V1': V1}

	global AC_CONFIG = [WING, H_TAIL, V_TAIL]
	global AC_SEC_NUM = [WING_SEC, H_SEC, V_SEC]

	#---------------- Boom (s) --------------------------------------
	BOOM = 1
	B1 = [1, 3]
	B = {'B1': B1}

	#=============================================================
	# Constraints
	#=============================================================

	#-------Overall constraints-----------------------------------
	global TAPER_MAX = 1.0
	global TAPER_MIN = 0.001
	global ANGLE_MAX = 10.0
	global ANGLE_MIN = -10.0
	global DIHEDRAL_MAX = 10.0
	global DIHEDRAL_MIN = -10.0

	#-------Wing--------------------------------------------------
	global WING_CONSTRAINTS = {'Num' : WING}

	# Temporary until file parsing function is done
	WING1_CHORD_MIN = 1
	WING1_CHORD_MAX = 3
	WING1_WINGSPAN_MIN = 4
	WING1_WINGSPAN_MAX = 20
	WING1_X_START = 0
	WING1_X_END = 2

	#Assemble into dictionary
	Wing1Con = {}
	Wing1Con['WING1_CHORD_MIN'] = WING1_CHORD_MIN
	Wing1Con['WING1_CHORD_MAX'] = WING1_CHORD_MAX
	Wing1Con['WING1_WINGSPAN_MIN'] = WING1_WINGSPAN_MIN
	Wing1Con['WING1_WINGSPAN_MAX'] = WING1_WINGSPAN_MAX
	Wing1Con['WING1_X_START'] = WING1_X_START
	Wing1Con['WING1_X_END'] = WING1_X_END
	WING_CONSTRAINTS['Wing1Con'] = Wing1Con

	#-------H-Tail--------------------------------------------------
	global H_TAIL_CONSTRAINTS = {'Num' : H_TAIL}

	# Temporary until file parsing function is done
	H_TAIL1_CHORD_MIN = 0.2
	H_TAIL1_CHORD_MAX = 2
	H_TAIL1_WINGSPAN_MIN = 0.1
	H_TAIL1_WINGSPAN_MAX = 3
	H_TAIL1_X_START = 6
	H_TAIL1_X_END = 10

	#Assemble into dictionary
	H_TAIL1Con = {}
	H_TAIL1Con['H_TAIL1_CHORD_MIN'] = H_TAIL1_CHORD_MIN
	H_TAIL1Con['H_TAIL1_CHORD_MAX'] = H_TAIL1_CHORD_MAX
	H_TAIL1Con['H_TAIL1_WINGSPAN_MIN'] = H_TAIL1_WINGSPAN_MIN
	H_TAIL1Con['H_TAIL1_WINGSPAN_MAX'] = H_TAIL1_WINGSPAN_MAX
	H_TAIL1Con['H_TAIL1_X_START'] = H_TAIL1_X_START
	H_TAIL1Con['H_TAIL1_X_END'] = H_TAIL1_X_END
	H_TAIL_CONSTRAINTS['H_TAIL1Con'] = H_TAIL1Con

	#-------V-Tail--------------------------------------------------
	global V_TAIL_CONSTRAINTS = {'Num' : V_TAIL}

	# Temporary until file parsing function is done
	V_TAIL1_CHORD_MIN = 0.1
	V_TAIL1_CHORD_MAX = 2
	V_TAIL1_WINGSPAN_MAX = 0.1
	V_TAIL1_WINGSPAN_MIN = 3
	V_TAIL1_X_START = 6
	V_TAIL1_X_END = 10

	#Assemble into dictionary
	V_TAIL1Con = {}
	V_TAIL1Con['V_TAIL1_CHORD_MIN'] = V_TAIL1_CHORD_MIN
	V_TAIL1Con['V_TAIL1_CHORD_MAX'] = V_TAIL1_CHORD_MAX
	V_TAIL1Con['V_TAIL1_WINGSPAN_MIN'] = V_TAIL1_WINGSPAN_MIN
	V_TAIL1Con['V_TAIL1_WINGSPAN_MAX'] = V_TAIL1_WINGSPAN_MAX
	V_TAIL1Con['V_TAIL1_X_START'] = V_TAIL1_X_START
	V_TAIL1Con['V_TAIL1_X_END'] = V_TAIL1_X_END
	V_TAIL_CONSTRAINTS['V_TAIL1Con'] = V_TAIL1Con


	
	





	#=============================================================
	# Starting points for each surface
	#=============================================================

	global TAPER_INIT_WING = []
	for num in range(WING_SEC-1):
		TAPER_INIT_WING.append(1)
	global ANGLE_INIT_WING = []
	for num in range(WING_SEC-1):
		ANGLE_INIT_WING.append(1)
	global DIHEDRAL_INIT_WING = []
	for num in range(WING_SEC-1):
		DIHEDRAL_INIT_WING.append(1)
	global X_OFFSET_INIT_WING = []
	for num in range(WING_SEC-1):
		X_OFFSET_INIT_WING.append(1)

	global TAPER_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		TAPER_INIT_V_TAIL.append(1)
	global ANGLE_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		ANGLE_INIT_V_TAIL.append(1)
	global DIHEDRAL_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		DIHEDRAL_INIT_V_TAIL.append(1)
	global X_OFFSET_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		X_OFFSET_INIT_V_TAIL.append(1)
	
	global TAPER_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		TAPER_INIT_H_TAIL.append(1)
	global ANGLE_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		ANGLE_INIT_H_TAIL.append(1)
	global DIHEDRAL_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		DIHEDRAL_INIT_H_TAIL.append(1)
	global X_OFFSET_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		X_OFFSET_INIT_H_TAIL.append(1)
	
	#=============================================================
	# Setting Geometry conditions
	#=============================================================

	# Object initialization
	global AC_0 = AC(AIRCRAFT_NAME)

	AC_0.wing['Num'] = WING
	AC_0.h_tail['Num'] = H_TAIL
	AC_0.v_tail['Num'] = V_TAIL
	AC_0.boom['Num'] = BOOM

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
	
		

#def parse_config_file(self):

