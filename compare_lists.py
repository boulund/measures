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
    parser.add_argument("--rbo", action="store_true", default=False,
            help="Only return the Rank-Based Overlap as a single float [%(default)s].")
    parser.add_argument("--ao", action="store_true", default=False,
            help="Only return the Average Overlap as a single float [%(default)s].")
    
    if len(argv) < 2:
        parser.print_help()
        exit(1)
    
    return parser.parse_args()


def parse_metaphlan2(f):
    for line in f:
        lineage, proportion = line.strip().split("\t")
        leaf = lineage.split("|")[-1]
        if leaf.startswith("s__"):
            yield leaf


def parse_kaiju(f):
    f.readline() # Skip second header line
    for line in f:
        if line.startswith("-"):
            return
        yield " ".join(line.split()[2:]).strip()


def parse_centrifuge(f):
    observed_species = []
    for line in f:
        (name, taxID, taxRank, genomeSize, numReads, 
                numUniqueReads, abundance) = line.strip().split("\t")
        if taxRank == "species":
            observed_species.append((name, float(abundance)))
    sorted_species = sorted(observed_species, key=lambda x: x[1], reverse=True)
    return (s[0] for s in sorted_species)


def parse_list(fn):
    with open(fn) as f:
        # Determine file type
        firstline = f.readline()
        if firstline.startswith("#SampleID"):
            return list(parse_metaphlan2(f))
        elif firstline.startswith("        %"):
            return list(parse_kaiju(f))
        elif firstline.startswith("name\ttaxID"):
            return list(parse_centrifuge(f))
        else:
            print("Can't recognize filetype of", fn)
            raise ValueError



def main(list1, list2, p=0.98, t=10, rbo=False, ao=False):
    if not any([rbo, ao]):
        for rank, items in enumerate(zip(list1[:t], list2[:t]), start=1):
            if items[0] == items[1]:
                print("{:>4} | {:<60} | =".format(rank, items[0]))
            else:
                print("{:>4} | {:<60} | {}".format(rank, *items))
        print("Average Overlap score (only {} first entries):  {}".format(t, AverageOverlap.score(list1, list2, t)))
        print("Rank Biased Overlap score (entire list):        {}".format(RBO.score(list1, list2, p)))
        print("-"*20)
    else:
        if rbo:
            print(RBO.score(list1, list2, p))
        elif ao:
            print(AverageOverlap.score(list1, list2, t))


if __name__ == "__main__":

    options = parse_args()
    list1 = parse_list(options.LIST1)
    list2 = parse_list(options.LIST2)

    if not any([options.rbo, options.ao]):
        print("Comparing '{}' with '{}'".format(options.LIST1, options.LIST2))
        print("-"*20)
    main(list1, list2, options.p, options.t, options.rbo, options.ao)
