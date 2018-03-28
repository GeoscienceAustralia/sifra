from __future__ import print_function
import os
from sifra.infrastructure_response import run_scenario

"""
Print out economic loss 
"""


root_dir = os.path.dirname(os.path.abspath(__file__))
conf_file = os.path.join(root_dir, "simulation_setup", "sysconfig_pscoal_600MW.conf")
run_scenario(conf_file)

