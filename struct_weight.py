'''
aero_MTOW.py: Runs takeoff simulation to determine MTOW








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


class struct_weight(Component):
	""" Calculates the empty weight of the aircraft """
	def __init__(self):

		super(struct_weight, self).__init__()

		
		

	def solve_nonlinear(self, params, unknowns, resids):
		




			 	
