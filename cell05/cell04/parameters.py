import sys

# sys.argv contains the script name plus all arguments.
# Subtract 1 to exclude the script name itself.
num_parameters = len(sys.argv)-1

print(f"Number of parameters: {num_parameters}.")
