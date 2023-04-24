# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 21:05:56 2023

@author: 4111029021 資管一 黃柏軒

演算法期中考第八題
"""

import random
import timeit

n = list(range(10, 1001, 10))
# 第a小題range(10, 1001, 10)
# 第c小題改成range(100, 10001, 100)
# 程式執行後都有圖片可以查看


# Insert sort
def insert_sort(l):
    for i in range(len(l)):
        temp = l[i]
        number = i-1
        while(number >= 0 and temp < l[number]):
            l[number+1] = l[number]
            number-=1
        l[number+1] = temp


temp_S, S, x = [], [], []

for i in range(len(n)):
    for j in range(n[i]):
        temp_S.append(random.randint(1, 100))
    insert_sort(temp_S)
    S.append(temp_S)
    x.append(temp_S[random.randint(0, len(temp_S)-1)])
    temp_S = []
    
    
# Linear search
def linear_search(num):
    for i in range(len(S[num])):
        if S[num][i] == x[num]:
            break


# Binary search
def binary_search(num):
    for i in range(len(S[num])):
        low = 0
        high = len(S[num])-1
        while( low<=high ):
            mid = int( (low+high)/2 )
            if x[num] < S[num][mid]:
                high = mid-1
            elif x[num] > S[num][mid]:
                low = mid+1
            else:
                return 0
        

# Fibonacci search
def fibo(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibo(n-2)+fibo(n-1)

fib = []
for i in range(22):
    fib.append(fibo(i))
        
def get(fib, n):
    i = 0
    while fib[i] <= n:
        i += 1
    return i-1
        
def fibonacci_search(num):
    max = len(S[num])
    y = get(fib, max+1)
    m = max - fib[y] 
    b = y - 1  
    i = b
    
    if S[num][i] < num:
        i += m
    while fib[b] > 0:
        if S[num][i] < num:
            b -= 1
            i += fib[b]
        elif S[num][i] > num:
            b -= 1
            i -= fib[b]
        else:
            break


# Caculate average execute time
l_time1,l_time2,l_time3=[],[],[]

for i in range(len(n)):
    time1 = timeit.timeit('linear_search(i)', setup='from __main__ import linear_search, i', number=1)
    time2 = timeit.timeit('binary_search(i)', setup='from __main__ import binary_search, i', number=1)
    time3 = timeit.timeit('fibonacci_search(i)', setup='from __main__ import fibonacci_search, i', number=1)
    l_time1.append(time1)
    l_time2.append(time2)
    l_time3.append(time3)
    
average1 = sum(l_time1)/100
average2 = sum(l_time2)/100
average3 = sum(l_time3)/100


# Drawing a line chart

import matplotlib.pyplot as plt

y1, y2, y3 = [], [], []
for i in range(len(l_time1)):
    y1.append(l_time1[i]*10**5)
    y2.append(l_time2[i]*10**5)
    y3.append(l_time3[i]*10**5)

plt.plot(n, y1, color='red', lw='1.0', ls='-.', marker='.', label='linear_search')
plt.plot(n, y2, color='orange', lw='1.0', ls='-.', marker='.', label='binary_search')
plt.plot(n, y3, color='yellow', lw='1.0', ls='-.', marker='.', label='fibonacci_search')

plt.legend()
plt.grid(color='black', ls=':', lw='1', alpha=0.5)
plt.title('Computational Complexity', fontsize=15)
plt.xlabel('execution (number of time)', fontsize=10)
plt.ylabel('average execution time (10^-5 sec)', fontsize=10)




