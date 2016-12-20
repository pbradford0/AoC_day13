#Author: Phil Bradford
#Solution for http://adventofcode.com/2015/day/13

import sys
import itertools

def get_happy(relation, left_human, right_human):
  happy_val = 0
  for pairing in relation:
    if pairing[0] == left_human and pairing[-1] == right_human:
      happy_val = pairing[1]
      break
  return happy_val

def happy_max(filename):
  input = open(filename, 'rU')
  happy_list = []
  seats = []
  names = []
  prev_chair = ""
  happiness = 0
  max_happiness = 0
  x = 0
  #try every permutation of seats to find happy max
  #first create a list of (Alice, +54, Bob) tuples
  for line in input:
    line = line.split()
    #make a list of just each name, used later
    if line[0] not in names:
      names.append(line[0])
    #account for gain or loss
    if line[2] == "lose":
      happy_list.append( (line[0], int(line[3])*-1, line[10][:-1]) )
    else:
      happy_list.append( (line[0], int(line[3]), line[10][:-1]) )
  #create a list of all seating permutations
  seats = itertools.permutations(names)
  for seating in seats:
    #calculate the happiness for each pass
    #start by comparing the first and last: always look back
    prev_chair = seating[-1]
    for chair in seating:
      happiness += get_happy(happy_list, prev_chair, chair)
      #print str(get_happy(happy_list, prev_chair, chair)) + " +",
      #print str(prev_chair) + " -> " + str(chair) + " should be " + str(get_happy(happy_list, prev_chair, chair))
      prev_chair = chair
    #print "= " + str(happiness) + "."
    #if happiness >= max_happiness:
    #  print str(max_happiness) + " <= " + str(happiness)
    max_happiness = max(happiness, max_happiness)
    happiness = 0
  return max_happiness

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