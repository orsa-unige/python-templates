#!/usr/bin/Rscript

library(jsonlite)

args <- commandArgs(trailingOnly = TRUE)

#nums = as.numeric(args)
nums = fromJSON(args)

b=nums['b']

print(b)
