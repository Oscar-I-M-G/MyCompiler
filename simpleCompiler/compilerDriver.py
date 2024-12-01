## Here is my simple compiler driver

# The steps are:
"""
1. gcc -E -P INPUT_FILE -o PREPROCESSED_FILE
   This will preprocess the input file ,
   -E : tells gcc to run only the preprocessor
   -P : tells the preprocessor not to emite linemarkers ()
   
   the preprocessde file should have .i extension
   
2. gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none PREPROCESS_FILE
    Generate assembly code from the preprocessd file
    remove the preprocessed file after this step

3. gcc ASSEMBLY_FILE -o OUTPUT_FILE
    Generate the final output file , no extensions needed

"""


import subprocess
import sys
import shlex

# Get the input file location from the command line

if len(sys.argv) != 2 or not sys.argv[1].strip():
    print("Usage: python3 compilerDriver.py <input_file>")
    sys.exit(1)


input_file = sys.argv[1].strip()

file_name = input_file.split("/")[-1].split(".")[-2]
file_destination = "/".join(input_file.split("/")[:-1])+ "/"
preprocessed_file = file_destination+file_name + ".i"
assembly_file = file_destination+file_name + ".s"

firstCommand = f"gcc -E -P {input_file} -o {preprocessed_file}"

secondCommand = f"gcc -S -O -fno-asynchronous-unwind-tables -fcf-protection=none {preprocessed_file} -o {assembly_file}"
thirdCommand = f"gcc {assembly_file} -o {file_destination}{file_name}"

splitFirstCommand = shlex.split(firstCommand)
splitSecondCommand = shlex.split(secondCommand)
splitThirdCommand = shlex.split(thirdCommand)

## First command
subprocess.run(splitFirstCommand)

## Second command
subprocess.run(splitSecondCommand)


## remove the preprocess file
subprocess.run(["rm", f"{preprocessed_file}"])

## Third command
subprocess.run(splitThirdCommand)

result = subprocess.run([file_destination+file_name])

print(result.returncode)
