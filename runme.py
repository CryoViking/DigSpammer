# Author: Cryosis
# Date: 2022-11-22

import sys
import os
import subprocess

# The main method
def __main__():
    filename = "domains.txt"
    with open(filename, "r") as handle:
        # Get first line
        line = handle.readline()

        # Iterate while line is not None
        while line is not None:
            print(f"Digging line: {line}")
            subprocess.run(["dig", line])
            # Get next line
            line = handle.readline()

if __name__ == "__main__":
    __main__()