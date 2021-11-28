
collatz <- function(n, m=NULL) {
  if(n==1) return(length(c(m, n))-1)
  collatz(ifelse(n%%2==0, n/2, 3*n +1), c(m, n))} 
  
# calculates many numbers at once
many <- function(x, y=NULL) {
        if (x==1001) return(hist(y, breaks = 999))
		many(x+1, c(y, collatz(x)))}
