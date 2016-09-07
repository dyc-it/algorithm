#!/usr/evn python

def lastBallLocation(depth, count):
    #initialize all switchs with closed status
    switchs = [False] * (1 << depth)
    n = (1<<depth) -1 #n indicates the maximum label of the ball
    k = n
    
    for i in range(0, count): # traverse route of all the balls
        k = 1 # the ball start from root node with label 1
        while True:
            switchs[k] = not switchs[k] # when the ball comes, the switch reverser its status
            if switchs[k]: # if switch is open, go left
                k = 2 * k
            else: # if switch is closed, go right
                k = 2 * k + 1
            if k > n: #when k is bigger than n, the ball arrives the bottom
                break
    # when all balls arrive the bottom, the k value divided by 2 is the label of the last ball's terminal point
    print depth, count, n, k/2
    
if __name__ == '__main__':
    depths = [4, 3, 10, 2, 8, 16]
    counts = [2, 4, 1, 2, 128, 12345]
    for i in range(0, len(depths)):
        lastBallLocation(depths[i], counts[i])
