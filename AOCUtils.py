import argparse
import logging
from time import time
import os
import sys
logging.basicConfig(level=logging.INFO)

logger = logging.getLogger('AOCUtils')
_startTime = None

DEBUG = True
TEST = False

def setDay(filename):
  return os.path.splitext(os.path.basename(filename))[0].replace('day', '')

def setLogger(day):
  global logger
  logger = logging.getLogger('day' + day)
  return logger

def getArgs():
  global DEBUG
  global TEST
  global logger

  parser = argparse.ArgumentParser()
  parser.add_argument("--debug", help="Enable debugging", action="store_true")
  parser.add_argument("--test", help="Use test file", action="store_true")
  args = parser.parse_args()
  DEBUG = args.debug
  TEST = args.test

  if DEBUG:
    logger.setLevel(logging.DEBUG)

def loadInput(day):
  global TEST
  global _startTime

  day = str(day)

  prefix = "input"
  suffix = ""
  if TEST or "pytest" in sys.modules.keys():
    suffix = "_test"

  filename = "{}{}{}.txt".format(prefix, day.zfill(2), suffix)
  filepath = os.path.join("inputs", filename)

  logger.debug("Loading file: {}...".format(filepath))

  with open(filepath) as f:
    content = [l.rstrip("\n") for l in f.readlines()]

  _startTime = time()

  if len(content) == 1:
    try:
      return int(content[0])
    except:
      try:
        return [int(i) for i in content[0].split()]
      except Exception as e:
        # logger.error(e)
        return [content[0]]
  else:
    try:
      return [i for i in content]
    except Exception as e:
      # logger.error(e)
      return content

def printTimeTaken():
  global _startTime
  _endTime = time()

  print("Time: {:.3f}s".format(_endTime - _startTime))
  _startTime = time()
