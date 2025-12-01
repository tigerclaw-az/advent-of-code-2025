#! /usr/local/bin/python3
###########################################
#    ---- Day 1: Secret Entrance ----     #
###########################################

from math import floor
import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

MAX_POS = 100

######
# -- TESTS --
######
def test_part1():
  input = AOCUtils.loadInput(DAY)

  assert(part1(input, 50)) == 3

def test_part2():
  input = AOCUtils.loadInput(DAY)

  assert(part2(input, 50)) == 6

######
# -- MAIN --
######

def part1(data, pos):
  count = 0

  for line in data:
    d,val = line[:1],int(line[1:])
    pos = (pos+val if d == "R" else (pos-val+MAX_POS)) % MAX_POS
    if (pos == 0): count += 1

    logger.info("{}|{} -> {}...{}".format(d,val,pos,count))

  return count

def part2(data, pos):
  count = 0
  new_pos = pos

  for line in data:
    d,val = line[:1],int(line[1:])
    new_pos = (pos+val if d == "R" else (pos-val+MAX_POS)) % MAX_POS
    count += floor(val/MAX_POS)
    if (pos != 0 and (new_pos == 0 or (d == "R" and new_pos < pos) or (d == "L" and new_pos > pos))):
      count += 1

    logger.info("{}|{} -> {}...{}".format(d,val,new_pos,count))

    pos = new_pos


  return count

def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  logger.info(input)

  # print('-- part 1: ', part1(input, 50))
  # AOCUtils.printTimeTaken()

  print('-- part 2: ', part2(input, 50))
  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
