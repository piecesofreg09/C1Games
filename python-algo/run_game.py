import os
import subprocess
import sys

# Runs a single game
def run_single_game(process_command):
    print("Start run a match")
    p = subprocess.Popen(
        process_command,
        shell=True,
        stdout=sys.stdout,
        stderr=sys.stderr
        )
    # daemon necessary so game shuts down if this script is shut down by user
    p.daemon = 1
    p.wait()
    print("Finished running match")
    
    
run_single_game("cd {} && java -jar engine.jar work {} {}".format(parent_dir, algo1, algo2))