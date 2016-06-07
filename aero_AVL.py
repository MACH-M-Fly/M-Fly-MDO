from __future__ import print_function
from openmdao.api import Component, Group, Problem

# Imported from Python standard
import sys
import os
import time
import math
import numpy

class aero_AVL(Component):
	""" Makes the appropriate run file and outputs the computed numbers """
	def __init__(self):
		super(aero_AVL, self).__init__()