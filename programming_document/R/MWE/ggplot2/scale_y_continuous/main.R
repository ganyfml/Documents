#!/usr/bin/env Rscript

library(ggplot2)
t = read.table('result.tsv', sep = '\t')
graph = ggplot(t, aes(x=V1, y=V2)) + scale_y_continuous(labels = scales::percent)
ggsave(file="error_rate.png", plot = graph)
