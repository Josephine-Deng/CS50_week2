# generate 10 random integers between 1 and 100
import random
rand=[random.randint(1,100) for _ in range(10)]

#output the details about the numbers
print('the numbers are:',rand)
print('Total numbers:',len(rand))
print('sum:',sum(rand))
print('min:',min(rand))
print('max:',max(rand))
print('Average:',sum(rand)/len(rand))

#sorted the numbers
rand.sort()
print('from small to big',rand)
rand.sort(reverse=True)
print('from big to small',rand)

#output the number greater than average
print('the number greater than average :',end='')
avg=sum(rand)/len(rand)
for num in rand:
    if num>avg:
        print(num,end=' ')