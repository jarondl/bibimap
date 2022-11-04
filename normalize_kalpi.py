#!/usr/bin/python3

import argparse
import csv
import fileinput
import sys


FIRST_ROW_PREFIX = 'סמל ועדה,ברזל,שם ישוב,סמל ישוב,קלפי,ריכוז,שופט,בזב,מצביעים,פסולים,כשרים,'
SEMEL=3
KALPI=4
RESULTS=11

def validate_first_row(first_row):
  #if not first_row.startswith(FIRST_ROW_PREFIX):
  #  raise ValueError(f'unexpected first line: "{first_row}",\n expected to start with {FIRST_ROW_PREFIX}')
  pass

def party_printer(first_row):
  print('PARTY_ID,PARTY_NAME')
  for n, party in enumerate(first_row.strip().split(',')[RESULTS:]):
    print(f'{n},{party}')
  return 

def result_printer(f: fileinput.FileInput):
  out = csv.writer(sys.stdout)

  # Using their names.
  out.writerow(['SEMEL_YISHUV','KALPI2022','KALPI_FULL','PARTY_ID', 'RESULT'])
  for row in csv.reader(f):
    semel = row[SEMEL]
    kalpi_full = row[KALPI]
    kalpi = kalpi_full.partition('.')[0]
    for n, result in enumerate(row[RESULTS:]):
      if result == '0':
        continue
      out.writerow([semel, kalpi, kalpi_full, n, result])
      

def main() -> int:
  parser = argparse.ArgumentParser(prog = "Kalpi_Normalizer")
  parser.add_argument('-p', '--parties', action='store_true', help="Party list mode collects party names")
  parser.add_argument('csv_input')
  args = parser.parse_args()

  with fileinput.input(args.csv_input) as f:
    first = f.readline()
    validate_first_row(first)
    if args.parties:
      return party_printer(first)
    result_printer(f)
     
  return 0

if __name__ == '__main__':
  sys.exit(main())

