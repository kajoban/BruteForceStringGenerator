import random;
import string;
import time;

def toString(inList):

    line = ''.join(inList);
    print(line, end = '')
    print("\n")

def nameGen(inString):

    target = list(inString)
    current = ['']*len(target)
    alphabet = [chr(i) for i in range(127)]
    
    pos = 0
        
    while(pos < len(target)):

        current[pos] = random.choice(alphabet)

        toString(current)

        if(current[pos] == target[pos]):
            pos = pos + 1;

        time.sleep(0.01)


def main():

    nameGen("Hello World!")


main()
