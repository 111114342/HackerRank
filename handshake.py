'''
https://www.hackerrank.com/challenges/handshake/problem
'''


def handshake(n):
    if n == 0:
        return 0
    
    else:
        handshake_no = 0
        for i in range(1,n):
            handshake_no = handshake_no + (n-i)

        return handshake_no
