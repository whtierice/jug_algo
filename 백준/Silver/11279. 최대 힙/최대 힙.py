import sys

reps = int(sys.stdin.readline().strip())

mq= []
cnt = 0



for i in range(reps):

    x = int(sys.stdin.readline().strip())
    if x > 0:
            mq.append(x)
            
            idx = len(mq) -1
            while idx > 0:
                pn = (idx - 1) // 2 
                if mq[idx] > mq[pn]:
                    mq[idx], mq[pn] = mq[pn], mq[idx]
                    idx = pn
                else:
                    break
    else:
        if not mq:
            print(0)
        else:
            print(mq[0])
            mq[0], mq[-1] = mq[-1], mq[0]
            mq.pop()

            index = 0
            while True:
                mini = index


                
                left = 2 * index +1
                right = 2 * index + 2



                if left < len(mq) and mq[mini] < mq[left]:
                    mini = left
                    
                if right < len(mq) and mq[mini] < mq[right]:
                    mini = right

            
                if mini == index:
                    break

                mq[index], mq[mini] = mq[mini], mq[index] 
                index = mini



                



