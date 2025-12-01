#! /usr/local/bin/python3
#######################################
# ---  Day 02: Red-Nosed Reports  --- #
#######################################

import AOCUtils
import re
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

######
# -- TESTS --
######
def test_part1():
  input = AOCUtils.loadInput(DAY)

  assert(part1(input)) == 2

def test_part2():
  input = AOCUtils.loadInput(DAY)

  assert(part2(input)) == 4

######
# -- MAIN --
######
def part1(data):
  total = 0

  for levels in data:
    prevLevel = 0
    count = 0
    is_safe = True
    arrLevels = levels.split(' ')
    for n in range(len(arrLevels)):
      level = int(arrLevels[n])
      if (prevLevel == 0):
        prevLevel = level
        continue

      diff = prevLevel - level
      count = count - 1 if prevLevel < level else count + 1
      logger.info("{} - {} = {} || {} < {}".format(prevLevel, level, diff, count, n))
      if (diff == 0 or abs(diff) > 3 or abs(count) < n):
        is_safe = False
        break

      prevLevel = level

    logger.info(is_safe)
    if (is_safe == True):
      total += 1

  return total

def part2(data):
  total = 0

  for levels in data:
    prevLevel = 0
    count = 0
    is_safe = True
    arrLevels = levels.split(' ')
    is_removed = False
    for n in range(len(arrLevels)):
      level = int(arrLevels[n])
      if (prevLevel == 0):
        prevLevel = level
        continue

      diff = prevLevel - level
      count_change = -1 if prevLevel < level else 1
      count += count_change
      logger.info("{} - {} = {} || {} < {}".format(prevLevel, level, diff, count, n))
      if (diff == 0 or abs(diff) > 3 or abs(count) < n):
        if (is_removed):
          is_safe = False
          break

        is_removed = True
        count += count_change * -1

      prevLevel = level

    logger.info(is_safe)
    if (is_safe == True):
      total += 1

  return total

def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  logger.info(input)

  print('-- part 1: ', part1(input))
  AOCUtils.printTimeTaken()

  # print('-- part 2: ', part2(input))
  # AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
