import os
from sifra.infrastructure_response import run_scenario

"""
Print out economic loss 
"""

root_dir = os.path.dirname(os.path.abspath(__file__))
conf_file = os.path.join(root_dir, "tests", "test_scenario_pscoal_600MW.conf")
run_scenario(conf_file)