#!/usr/bin/env Rscript

library(ggplot2)
t = read.table('result.tsv', sep = '\t')
graph = ggplot(t, aes(x=V1, y=V2)) + geom_bar(stat="identity")
ggsave(file="error_rate.png", plot = graph)
