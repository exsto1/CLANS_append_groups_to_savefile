filename = "PF01388/PF01388_clusters.clstr"
min_seq = 20


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


for i in range(len(clusters)):
    out_big = open("PF01388_clusters/PF01388_big_clusters%s.txt" % i, "w")
    for i1 in clusters[i]:
        out_big.write(i1)
        out_big.write("\n")
    out_big.close()

out_small = open("PF01388_clusters/PF01388_small_clusters.txt", "w")
for i in small_clusters:
    out_small.write(i)
    out_small.write("\n")
