#!/usr/bin/env python3

import sys
import csv


class FlightsByDestinationsMapper:
    def __init__(self):
        pass

    def mapping(self):
        for row in csv.reader(iter(sys.stdin.readline, '')):
            if row[0] != 'Year':
                print('{}\t{}'.format(row[17], 1))


def main(argv):
    flights_by_destinations_mapper = FlightsByDestinationsMapper()
    flights_by_destinations_mapper.mapping()


if __name__ == "__main__":
    main(sys.argv[:1])
