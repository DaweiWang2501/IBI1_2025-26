# What does this piece of code do?
# Answer:This script calculates the sum of 11 random integers, each integers between 1 and 10.

# Import libraries
# randint allows drawing a random number,
# e.g. randint(1,5) draws a number between 1 and 5
from random import randint 
#Import the tool for generating random integers

# ceil takes the ceiling of a number, i.e. the next higher integer.
# e.g. ceil(4.2)=5
from math import ceil
#Import the tool for rounding up
total_rand = 0 # Stores the running total of random numbers
progress=0 # Counter to track the number of circles
while progress<=10: #if the process≤10,then continuning
	progress+=1 # the process plus 1(total 11)
	n = randint(1,10) # Generate a random integer between 1 and 10
	total_rand+=n # Add the random number to the total

print(total_rand) # Output the final accumulated number