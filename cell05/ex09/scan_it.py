import sys

if len(sys.argv) == 3:
    keyword = sys.argv[1]
    text = sys.argv[2]
    
    # Count occurrences if keyword is non-empty
    count = text.count(keyword) if keyword else 0
    
    if count > 0:
        print(count)
    else:
        print("none")
else:
    print("none")