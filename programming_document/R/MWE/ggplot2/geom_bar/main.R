#!/usr/bin/env Rscript

library(ggplot2)
a = read.table('result.tsv', sep = '\t')
ggplot(a, aes(x=V1, y=V2)) + geom_bar(stat="identity")
