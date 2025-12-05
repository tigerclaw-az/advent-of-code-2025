#! /usr/local/bin/python3
#######################################
#     ---- Day 5: Cafeteria  ----     #
#######################################
from os import remove
import AOCUtils
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

######
# -- TESTS --
######
def test_part1():
  input = AOCUtils.loadInput(DAY)
  assert(totalFreshIDs(input)) == 3

def test_part2():
  input = AOCUtils.loadInput(DAY)
  assert(allFreshIDs(input)) == 14

######
# -- MAIN --
######
def isFresh(id, lower, upper):
  lMax = len(lower)
  uMax = len(upper)
  for idx,l in enumerate(lower):
    if (id >= l and id <= upper[idx]):
      logger.debug(f"{id}|{idx}->{l}-{upper[idx]}")
      return True

  return False

def totalFreshIDs(data):
  total = 0
  lower = []
  upper = []
  # duplicates = {}
  for line in data:
    # Skip blank line
    if line == "":
      logger.debug(f"{lower}, {upper}")
      continue

    try:
      start, end = line.split("-")
      logger.debug(f"start:{start},end:{end}")
      lower.append(int(start))
      upper.append(int(end))
    except:
      id = int(line)
      total += isFresh(id, lower, upper)

  return total

def getUniqueRanges(ranges):
  # Sort ranges by start
  ranges.sort(key=lambda x: x[0])
  merged = []
  for current in ranges:
    if not merged:
      merged.append(current)
    else:
      last_start, last_end = merged[-1]
      if current[0] <= last_end + 1:  # overlaps or adjacent
        # merge
        merged[-1] = (last_start, max(last_end, current[1]))
      else:
        merged.append(current)

  return merged

def allFreshIDs(data):
  total = 0
  idRanges = []
  for line in data:
    # Skip blank line
    if line == "":
      logger.debug(idRanges)
      uniqueRanges = getUniqueRanges(idRanges)
      for start, end in uniqueRanges:
        total += end - start + 1
      return total

    start, end = map(int, line.strip().split('-'))
    # logger.debug(f"start:{start},end:{end}")
    idRanges.append((start, end))

def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  logger.debug(input)

  print('-- part 1: ', totalFreshIDs(input))
  AOCUtils.printTimeTaken()

  print('-- part 2: ', allFreshIDs(input))
  AOCUtils.printTimeTaken()

if __name__ == '__main__':
  main()
