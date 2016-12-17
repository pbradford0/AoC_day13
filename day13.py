#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/13

def main():
  if len(sys.argv) != 2:
    print 'Please specify an input file'
    sys.exit(1)

  #a = elf_math(sys.argv[1])
  #print "Elf math: " + str(a)
  
  b = red_math(sys.argv[1])
  print "Elf math: " + str(b)

if __name__ == '__main__':
  main()