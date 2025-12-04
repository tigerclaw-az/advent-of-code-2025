#! /usr/local/bin/python3
#######################################
#   ---- Day 02: Gift Shop  ----      #
#######################################

import AOCUtils
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

######
# -- TESTS --
######
def test_part1():
  input = AOCUtils.loadInput(DAY)

  assert(validateIDs(input, True)) == 1227775554

def test_part2():
  input = AOCUtils.loadInput(DAY)

  assert(validateIDs(input, False)) == 4174379265

######
# -- MAIN --
######
def isInvalid(id: str, isEven):
  idLen = len(id)
  if (isEven and idLen % 2 != 0):
    return False

  midpoint = idLen // 2
  if isEven:
    firstHalf = id[:midpoint]
    secondHalf = id[midpoint:]
    logger.debug("{}|{}".format(firstHalf, secondHalf))

    return firstHalf == secondHalf
  else:
    for n in range(1, midpoint+1):
      searchNum = id[:n]
      splitNum = id.split(searchNum)
      logger.debug(splitNum)
      if ''.join(splitNum) == '':
        return True

    return False

def validateIDs(data, isEven):
  total = 0
  for line in data:
    logger.debug(line)
    ids = line.split('-')
    logger.debug(ids)
    for id in range(int(ids[0]), int(ids[1])+1):
      if (isInvalid(str(id), isEven)):
        logger.info("invalid::{}".format(id))
        total += id

  return total

def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  logger.info(input)

  print('-- part 1: ', validateIDs(input[0].split(','), True))
  AOCUtils.printTimeTaken()

  print('-- part 2: ', validateIDs(input[0].split(','), False))
  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
