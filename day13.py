#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/13

import sys

def happy_max(filename):
  return 0

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  a = happy_max(sys.argv[1])
  print "Maximum Happiness: " + str(a)
  
  #b = red_math(sys.argv[1])
  #print "Elf math: " + str(b)

if __name__ == '__main__':
  main()