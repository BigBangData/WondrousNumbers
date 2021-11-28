# calculates and outputs total number of operations in one go

numops <- function(n, m=NULL) {
  if(n==1) return(length(c(m, n))-1)
  numops(ifelse(n%%2==0, n/2, 3*n +1), c(m, n))
}
  
numops(17)

# output the hailstone sequence of numbers
hailstone <- function(n, m=NULL) {
  if(n==1) return(c(m, n))
  hailstone(ifelse(n%%2==0, n/2, 3*n +1), c(m, n))
}

hailstone(17)









# calculates many numbers at once 
  
many <- function(x, y=NULL) {
        if (x==1001) return(y);
		many(x+1, c(y, collatz(x)))}


# how it works in each iteration
		
many(1)

many(1, NULL)
FALSE
x = 2
y = c(NULL, 0)

pass2
many(2, 0)
FALSE
x = 3
y = c(0, 1)

pass3
many(3, (0, 1))
FALSE
x = 4
y = c((0, 1), 7)

pass4 
many(4, (0, 1, 7))
FALSE
x = 5
y = c((0, 1, 7), 2)

etc...

pass1001
x == 1001? TRUE 
	return(0, 1, 7, 2....)

	

	
	

		

		

		     
  
