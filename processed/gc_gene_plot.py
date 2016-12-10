# Dec 10 2016
# python script for plotting gc content and exon content and save as png files
# coding: utf-8

# import necessary libraries
import pandas
import matplotlib.pyplot as plt
# get_ipython().magic('matplotlib inline')

# import data
human_chr21 = pandas.read_csv("human_chr21.txt", sep="\t")
human_chr21.head()

# calculating gc content and save as new columns
human_chr21['gc_content'] = human_chr21['gc_bases']/  (human_chr21['win_end']-human_chr21['win_start'])
human_chr21.head()

# calculating exon content and save as new columns
human_chr21['gene_content'] = human_chr21['exon_bases']/  (human_chr21['win_end']-human_chr21['win_start'])
human_chr21.head()

# make scatter plot of exon vs gc content
plt.plot(human_chr21['gene_content'],human_chr21['gc_content'],'o')
plt.xlabel('Exon Content')
plt.ylabel('GC Content')
plt.ylim([0,0.55])

# save the plot as png file
plt.savefig('gene_vs_gc2.png')

