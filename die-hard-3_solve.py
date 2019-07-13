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
 
    if c > max(b,a):
        result = "NO"
    elif min(a,b) == 1:
        result = "YES"
    elif c%(max(a,b)-min(a,b))==0:
        result = "YES"
    elif c%(min(a,b))==0:
        result = "YES"
    elif c == a or c == b:
        result = "YES"
    else:
        gcd = 1
        if max(a,b)%min(a,b)==0:
            gcd = min(a,b)
        else:
            for count in range(2,int(min(a,b)/2+1)):
                i = int(min(a,b)/2+1) - count
                if a%i == 0 and b%i == 0:
                    gcd = i
                    break
                
        if c%gcd ==0 :
            result = "YES"
        else:
            result = "NO"
        
    return result
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        abc = input().split()

        a = int(abc[0])

        b = int(abc[1])

        c = int(abc[2])

        result = solve(a, b, c)

        fptr.write(result + '\n')

    fptr.close()
