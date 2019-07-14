'''
https://www.hackerrank.com/challenges/new-year-chaos/problem

Sample Input
2
5
2 1 5 3 4
5
2 5 1 3 4

Sample Output
3
Too chaotic
'''

#!/bin/python3


# Complete the minimumBribes function below.
def minimumBribes(q):
    moves_no = 0

    for i in range(len(q)):
        move = q[i] - i - 1
        
        # if any move is more than 2 steps, then print out "Too chaotic"
        if move > 2:
            print("Too chaotic")
            return
    
    # run 2 loops to sort all numbers, with early stopping when all numbers are sorted
    for c1 in range(len(q)):    
        for c2 in range(len(q)):
            c3 = len(q) - c2 - 1
            move = q[c3] - c3 - 1
                
            if c3>0:                
                if q[c3] < q[c3-1]:
                    moves_no += 1
                    q[c3],q[c3-1] = q[c3-1]*1,q[c3]*1
                    
        # check if all numbers are in order then stop the sort and print result
        move_check = 0        
        for i in range(len(q)):
            move = q[i] - i - 1
            move_check += (move >0)*1

        if move_check == 0:
            print(moves_no)
            return
        
    print(moves_no)
            

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        minimumBribes(q)
