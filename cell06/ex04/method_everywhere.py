import sys

def shrink(text):
    print(text[:8])

def enlarge(text):
    text += 'Z' * (8 - len(text))
    print(text)

def main():
    if len(sys.argv) < 2:
        print("none")
        return
        
    for arg in sys.argv[1:]:
        if len(arg) > 8:
            shrink(arg)
        elif len(arg) < 8:
            enlarge(arg)
        else:
            print(arg)

if __name__ == "__main__":
    main()