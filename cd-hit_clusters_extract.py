import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input", help=".clstr file from Cd-Hit.")
parser.add_argument("-m", "--min", help="minimum sequnces per cluster", type=int, default=0)
parser.add_argument("-o", "--output", help="output folder. Will be created if doesn't exist", default="./clusters")
parser.add_argument("-s", "--small", help="base name of file with all small clusters", default="small_clusters")
parser.add_argument("-b", "--big", help="base name of filea with big clusters", default="cluster_")

args = parser.parse_args()

filename = os.path.abspath(args.input)
min_seq = args.min
output_folder = os.path.abspath(args.output)
small_name = args.small
big_name = args.big


# Extract and filter clusters
file = open(filename).read()
entries = file.split('>Cluster ')
entries = [i.split("\n") for i in entries if i]

small_clusters = []
clusters = []
for i in range(len(entries)):
    entries[i] = [i1 for i1 in entries[i][1:] if i1]
    for i1 in range(len(entries[i])):
        entries[i][i1] = entries[i][i1].split('>')[1].split("...")[0]

    if len(entries[i]) <= min_seq:
        for i1 in entries[i]:
            small_clusters.append(i1)
    else:
        clusters.append(entries[i])

clusters.sort(key=lambda i: len(i), reverse=True)


# Saving process of big and small clusters.
for i in range(len(clusters)):
    out_big = open("%s/%s%s.txt" % (output_folder, big_name, i), "w")
    for i1 in clusters[i]:
        out_big.write(i1)
        out_big.write("\n")
    out_big.close()

out_small = open("%s/%s" % (output_folder, small_name), "w")
for i in small_clusters:
    out_small.write(i)
    out_small.write("\n")
