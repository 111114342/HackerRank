'''
https://www.hackerrank.com/challenges/die-hard-3/problem

Given 2 jugs of capacity a and b gallons, and an infinite supply of water, can you fill one of the jugs with exactly c gallons of water ? 
Input Format
First line contains the number of testcases T. T lines follow. 
Each line contains 3 space separated integers a, b and c . a and b indicate the capacity of the two jugs respectively, and c denotes the exact capacity with which one of the jugs should be filled. 
Output Format
For each test case, print "YES" (in a new line) if one of the jugs can be filled with exactly c gallons of water and "NO" (in a new line) if they cannot be filled. ( quotes are for clarity )
'''

def solve(a, b, c):
    # if c is more than both jugs then cannot fill c in any jug
    if c > max(a,b):
        result = "NO"
  
    # if any jug is 1 gallon, then can fill any amount 
    elif min(a,b) == 1:
        result = "YES"
    # if c is divisible by the different between the two jugs, then "YES" 
    elif c%(max(a,b)-min(a,b))==0:
        result = "YES"
      
    # if c is divisible by any jug or equal to any jug, then "YES"  
    elif c%(min(a,b))==0:
        result = "YES"
    elif c == a or c == b:
        result = "YES"
    
    # else, check if c is divisible by greatest common divisor (gdc), then "YES"
    else:
        # find gcd
        gcd = 1
        if max(a,b) % min(a,b) == 0:
            gcd = min(a,b)
        else:
            for count in range(2,int(min(a,b)/2+1)):
                i = int(min(a,b)/2+1) - count
                if a%i == 0 and b%i == 0:
                    gcd = i
                    break
        
        # check if c is divsiible by gcd
        if c % gcd == 0 :
            result = "YES"
        else:
            result = "NO"
        
    return result
