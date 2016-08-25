# Main aircraft configuration File

def init():
	#================================================================
	# Aircraft configuration (should become a file reading procedure)
	#================================================================

	AIRCRAFT_NAME = 'new_AC'
	# Number of wings
	WING = 1 

	# Number of wing sections
	WING_SEC = 10

	# Wing Initial Condition
	# name, airfoil, root chord, wing span, number of sections, X offset
	W1 = ['Wing1', 'E420.dat', 1.6, 5, WING_SEC, 3]

	#Constraints
	W1_c = 

	# combine all data
	W = {'W1' : W1}
	# Number of horizontal tails
	H_TAIL = 1

	# Number of sections
	H_SEC = 2

	# Horizontal Tail Initial Condition
	H1 = ['H_tail1']

	H = {'H1': H}

	# Number of vertical tails
	V_TAIL = 1

	# Number of vertical tail sections
	V_SEC = 2

	# Vertical Tail Initial Conditions
	V1 = ['V_tail1']

	V = {'V1': V}

	AC_CONFIG = [WING, H_TAIL, V_TAIL]
	AC_SEC_NUM = [WING_SEC, H_SEC, V_SEC]

	BOOM = 1
	B1 = []
	B = {'B1': B1}

	#-------Overall constraints
	TAPER_MAX = 1.0
	TAPER_MIN = 0.001
	ANGLE_MAX = 10.0
	ANGLE_MIN = -10.0
	X_OFFSET_MAX = 

	#=============================================================
	# Starting points for each surface
	#=============================================================

	TAPER_INIT_WING = []
	for num in range(WING_SEC-1):
		TAPER_INIT_WING.append(1)
	ANGLE_INIT_WING = []
	for num in range(WING_SEC-1):
		ANGLE_INIT_WING.append(1)
	DIHEDRAL_INIT_WING = []
	for num in range(WING_SEC-1):
		DIHEDRAL_INIT_WING.append(1)
	X_OFFSET_INIT_WING = []
	for num in range(WING_SEC-1):
		X_OFFSET_INIT_WING.append(1)

	TAPER_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		TAPER_INIT_V_TAIL.append(1)
	ANGLE_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		ANGLE_INIT_V_TAIL.append(1)
	DIHEDRAL_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		DIHEDRAL_INIT_V_TAIL.append(1)
	X_OFFSET_INIT_V_TAIL = []
	for num in range(V_SEC-1):
		X_OFFSET_INIT_V_TAIL.append(1)
	
	TAPER_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		TAPER_INIT_H_TAIL.append(1)
	ANGLE_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		ANGLE_INIT_H_TAIL.append(1)
	DIHEDRAL_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		DIHEDRAL_INIT_H_TAIL.append(1)
	X_OFFSET_INIT_H_TAIL = []
	for num in range(H_SEC-1):
		X_OFFSET_INIT_H_TAIL.append(1)
	
	#=============================================================
	# Setting Geometry conditions
	#=============================================================

	# Object initialization
	AC_O = AC(AIRCRAFT_NAME)

	AC_0.wing['Num'] = WING
	AC_0.h_tail['Num'] = H_TAIL
	AC_0.v_tail['Num'] = V_TAIL
	AC_0.boom['Num'] = BOOM

	for i in range(WING):
		Wing = W['W'+str(i+1)]
		AC_0.add_wing(Wing[0], Wing[1], Wing[2], Wing[3], Wing[4], Wing[5])
	for i in range(H_TAIL):
		H_tail = H['H'+str(i+1)]
		AC_0.add_h_tail(H_tail[0], H_tail[1], H_tail[2], H_tail[3], H_tail[4], H_tail[5])
	for i in range(V_TAIL):
		V_tail = V['V'+str(i+1)]
		AC_0.add_v_tail(V_tail[0], V_tail[1], V_tail[2], V_tail[3], V_tail[4], V_tail[5])
	for i in range(BOOM):
		boom = B['B'+str(i+1)]
		AC_0.add_boom(boom[0], boom[1])
	
		



