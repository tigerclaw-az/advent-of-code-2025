#! /usr/local/bin/python3
#######################################
#     ---- Day 03: Lobby  ----        #
#######################################

import AOCUtils
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

######
# -- TESTS --
######
def test_part1():
  input = AOCUtils.loadInput(DAY)

  assert(maximumJoltage(input, 2)) == 357

def test_part2():
  input = AOCUtils.loadInput(DAY)

  assert(maximumJoltage(input, 12)) == 3121910778619

######
# -- MAIN --
######
def largestJoltage(bank, num):
  # Convert the bank string into a list of digits
  digits = list(bank)
  # Convert each digit to an integer for comparison
  digits_int = list(map(int, digits))

  # We need to select <num> digits to form the maximum number, preserving order
  # Approach: Use a greedy algorithm similar to "max number after removing k digits"

  # Number of digits to remove: total length - num
  to_remove = len(digits) - num
  selected = []

  for digit in digits:
    # Remove smaller digits from the selected list when possible
    while to_remove > 0 and selected and selected[-1] < digit:
        selected.pop()
        to_remove -= 1
    selected.append(digit)

  # If still need to remove digits, remove from the end
  while to_remove > 0:
    selected.pop()
    to_remove -= 1

  # The selected list now contains the largest possible sequence of 12 digits
  # Convert back to string
  return int(''.join(map(str, selected)))

def maximumJoltage(data, num):
  total = 0
  for line in data:
    total += largestJoltage(line, num)

  return total

def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)

  logger.debug(input)

  print('-- part 1: ', maximumJoltage(input, 2))
  AOCUtils.printTimeTaken()

  print('-- part 2: ', maximumJoltage(input, 12))
  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
