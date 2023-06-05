import random
import queue

f = open('Humoresque_lyric.txt')
lyric = f.read()

count = [0, 0, 0]
correct = [0, 1, 0, 0, 1, 1, 0, 2, 2, 1]

q = queue.Queue()

def rand():
    r = random.randint(0,2)
    if(r == 0):
        count[0] += 1
        print('すき',end=' ')
    if(r == 1):
        count[1] += 1
        print('きらい',end=' ')
    if(r == 2):
        count[2] += 1
        print('きら',end=' ')
    return r

for num in range(10):
    q.put(rand())

while True:
    num = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for n in range(10):
        num[n] = q.get()
    for n in range(10):
        q.put(num[n])
    if(num == correct):
        break
    else:
        q.get()
        q.put(rand())

print()
print()

print(lyric)

print()
print("すき:", count[0], " きら:",count[1], " きらい:", count[2])
print("total:", count[0]+count[1]+count[2])