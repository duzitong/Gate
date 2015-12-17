from calc import *

if __name__ == '__main__':
  a = 0b1101
  b = 0b0110
  c = 0b1000
  for i in operate_line([a, b, c], 4):
    print(i)

