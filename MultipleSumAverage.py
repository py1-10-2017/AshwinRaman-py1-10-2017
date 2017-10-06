
for odd in range (1,1000, 2): #prints all odd numbers between 1 and 1000.
	print odd

for num in range (5,1000000): #prints all the multiples of 5 from 5 to 1,000,000.
    if num%5 == 0:
        print num

a = [1, 2, 5, 10, 255, 3] #prints the sum of all the values in the list.
print sum(a)

a = [1, 2, 5, 10, 255, 3] #prints the average of the values in the list.
print sum(a)/len(a)
