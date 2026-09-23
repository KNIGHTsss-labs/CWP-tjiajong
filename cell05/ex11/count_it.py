import sys

params = sys.argv[1:]

if params:
    print(f"parameters: {len(params)}")
    for param in params:
        print(f"{param}: {len(param)}")
else:
    print("none")