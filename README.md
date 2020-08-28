# CLANS_append_groups_to_savefile
Creating group files from Cd-Hit output clusters and automatic importing into CLANS savefile.

It is an equivalent of using CLANS built in tools:
- Using external file as search option
- Selecting found sequences
- Adding them as a group, renaming, recoloring and changing size

## Group file structure
Group file may be easily created from any fasta file following this template:

```
# CONFIG:name=XXX,size=XXX,hide=X,color=XXX;XXX;XXX;XXX
sequence_name_1
sequence_name_2
sequence_name_3
sequence_name_4
...
```

Note, that first line is completly optional and can be skipped. Script will use default values or those provided by user as a flag.

## CLANS groups
Names in CLANS and in output file from Cd-Hit must be identical. 
It shouldn't be a problem if the same .fasta file was used to produce both inputs - CLANS savefile and Cd-Hit clusters.
It is important as CLANS is using indexes of sequences instead of real names in groups section, so cluster files must be matched beforehand.    
See example below:
```
<seqgroups>
name=GROUP_NAME_0
type=0
size=4
hide=0
color=255;0;0;255
numbers=1704;1703;1702;1701;1700;
name=GROUP_NAME_1
type=0
size=4
hide=0
color=255;0;0;255
numbers=1684;1681;1676;1675;1674;1673;1672;1670;1669;
</seqgroups>
```
