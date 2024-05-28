#softeer 부트캠프 코테
from collections import deque

input_str = list(map(str,input().split()))

def encrypt(str):
    key = []
    for i in str[1]:
        key.append(ord(i)-ord('a'))

    message = []
    for i in str[3]:
        message.append(ord(i)-ord('a'))

    sum = deque()
    for i in range(len(str[1])):
        temp = key[i] + message[i]
        if temp > 25:
            temp -= 26
        sum.append(temp)
    for i in range(int(str[2])):
        sum.append(sum.popleft())
    ans = []
    for i in sum:
        ans.append(chr(i+ord('a')))
    print(''.join(ans))


def decrypt(str):
    key = []
    for i in str[1]:
        key.append(ord(i)-ord('a'))

    message = deque()
    for i in str[3]:
        message.append(ord(i)-ord('a'))

    for i in range(int(str[2])):
        message.appendleft(message.pop())
    
    sum = []
    for i in range(len(str[1])):
        temp = message[i] - key[i]
        if temp < 0:
            temp += 26
        sum.append(temp)
    ans = []
    for i in sum:
        ans.append(chr(i+ord('a')))
    print(''.join(ans))

if (input_str[0] == 'encrypt'):
    encrypt(input_str)
elif (input_str[0] == 'decrypt'):
    decrypt(input_str)
