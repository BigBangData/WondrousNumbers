# performs collatz calculation and outputs a vector
collatz <- function(n, m=NULL) {
    if(n==1) return(c(m, 1));
    collatz(ifelse(n%%2==0, n/2, 3*n +1), c(m, n))
}

# outputs total number of operations
numops <- function(x) {
    length(collatz(x)) - 1
}

# performs a series of calculations and outputs total operations
vec <- 2:1000
for (i in vec) vec[i] <- numops(i)
print(vec)