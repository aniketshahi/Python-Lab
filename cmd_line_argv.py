import sys

# Check the number of command-line arguments
if len(sys.argv) < 2:
    print("Usage: python script.py <arg1> [arg2] [arg3] ...")
    sys.exit(1)  # Exit the script with a non-zero status to indicate an error

# Access and print command-line arguments
script_name = sys.argv[0]
arguments = sys.argv[1:]

print(f"Script Name: {script_name}")
print(f"Number of Arguments: {len(arguments)}")
print("Arguments:", arguments)
