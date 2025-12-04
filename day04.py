#! /usr/local/bin/python3
#########################################
# ---- Day 4: Printing Department  ---- #
#########################################

from os import remove
import AOCUtils
DAY = AOCUtils.setDay(__file__)
logger = AOCUtils.setLogger(DAY)

######
# -- TESTS --
######
def test_part1():
  input = AOCUtils.loadInput(DAY)

  assert(totalRolls(input, 4, False)) == 13

def test_part2():
  input = AOCUtils.loadInput(DAY)

  assert(totalRolls(input, 4, True)) == 43

######
# -- MAIN --
######
def totalRolls(grid, maxRolls, canRemove):
  total = 0
  totalRows = len(grid)
  totalCols = len(grid[0])
  # Directions for 8 neighbors (including diagonals)
  directions = [(-1, -1), (-1, 0), (-1, 1),
                (0, -1),           (0, 1),
                (1, -1),  (1, 0),  (1, 1)]
  new_grid = []
  for r in range(totalRows):
    if (canRemove):
      new_grid.append('')
    for c in range(totalCols):
      # logger.debug(f"{r}|{c}->{grid[r][c]}")
      removeRoll = False
      if grid[r][c] == '@':
        neighbor_count = 0
        for dr, dc in directions:
          nr, nc = r + dr, c + dc
          if 0 <= nr < totalRows and 0 <= nc < totalCols:
            if grid[nr][nc] == '@':
              neighbor_count += 1
              if neighbor_count >= maxRolls:
                break

        if neighbor_count < maxRolls:
          total += 1
          removeRoll = True

      if (canRemove):
        new_grid[r] += '.' if removeRoll == True else grid[r][c]

  logger.debug(f"TOTAL:{total}")
  if (canRemove == False or total == 0):
    return total

  logger.debug(f"NEW:{new_grid}")
  return total + totalRolls(new_grid, maxRolls, canRemove)

def main():
  AOCUtils.getArgs()
  input = AOCUtils.loadInput(DAY)
  grid = input

  logger.debug(grid)

  print('-- part 1: ', totalRolls(grid, 4, False))
  AOCUtils.printTimeTaken()

  print('-- part 2: ', totalRolls(grid, 4, True))
  AOCUtils.printTimeTaken()

if __name__ == '__main__':
    main()
