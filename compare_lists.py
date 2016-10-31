#!/usr/bin/env python3
# Compare metagenome taxonomic abundance rankings
# using rank biased overlap.
# Fredrik Boulund 2016

from sys import argv, exit
import argparse
from measures.rankedlist import RBO, AverageOverlap

def parse_args():
    desc = ("Compare metagenome taxonomic abundance rankings "
            "(expects lists in Kaiju report output format). "
            "Fredrik Boulund 2016.")
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument("LIST1")
    parser.add_argument("LIST2")
    parser.add_argument("-p", default=0.98, type=float,
            help="p-value to use when comparing lists [%(default)s].")
    parser.add_argument("-t", default=25, type=int,
            help="Number of top list values to display alongside comparison [%(default)s].")
    
    if len(argv) < 2:
        parser.print_help()
        exit(1)
    
    return parser.parse_args()


def parse_list(fn):
    with open(fn) as f:
        f.readline() # Skip header lines
        f.readline() # Skip header lines
        for line in f:
            if line.startswith("-"):
                return
            yield " ".join(line.split()[2:]).strip()


def main(list1, list2, p=0.98, t=10):
    for rank, items in enumerate(zip(list1[:t], list2[:t]), start=1):
        if items[0] == items[1]:
            print("{:>2} | {:<30} | =".format(rank, items[0]))
        else:
            print("{:>2} | {:<30} | {}".format(rank, *items))
    print("Average Overlap score (only {} first entries):  {}".format(t, AverageOverlap.score(list1, list2, t)))
    print("Rank Biased Overlap score (entire list):        {}".format(RBO.score(list1, list2, p)))
    print("-"*20)


if __name__ == "__main__":

    options = parse_args()
    list1 = list(parse_list(options.LIST1))
    list2 = list(parse_list(options.LIST2))

    print("Comparing '{}' with '{}'".format(options.LIST1, options.LIST2))
    print("-"*20)
    main(list1, list2, options.p, options.t)
