from calc import *

if __name__ == '__main__':
    """
    a = 0b0101010101010101
    b = 0b0011001100110011
    c = 0b0000111100001111
    d = 0b0000000011111111
    for i in operate_line([a, b, c, d], 2 ** 4):
        print(i)
    """
    for times in range(2):
        outFile = open(str(times+1) + '.txt', 'w+')
        with open(str(times) + '.txt', 'r') as inFile:
            while True:
                line = inFile.readline()
                if not line:
                    break
                for res in operate_line([int(l) for l in line.split()]):
                    for i in res:
                        outFile.write(str(i) + ' ')
                    outFile.write('\n')
