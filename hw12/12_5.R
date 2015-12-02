c1 <- c(1,1,8,2,3,7,6,6,7,5,4)
c2 <- c(6,7,6,4,3,7,5,3,4,3,2)

points <- data.frame(c1,c2)

# prepare hierarchical cluster
hc = hclust(dist(points), method = "complete")
# very simple dendrogram
plot(hc)


data <- read.table("AlgHW12.txt", sep = ' ', header = TRUE, row.names = 1)

sums <- data.frame()
for (i in 1:nrow(data)){
  row <- data[i,1]
  sum <- sum(data[i, 2:1921])
  vec <- data.frame(toString(row), sum)
  sums <- rbind(sums, vec)
}
names(sums) <- c("row", "sum")

res <- sums[order(sums$sum, decreasing = TRUE)]
res[,1]



