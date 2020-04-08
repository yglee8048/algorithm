# 변수

```python
a, b = input("1 2 : ").split()
print(a, b, sep=", ") # '1' ,'2'

a, b = map(int, input("1 2 : ").split())
print(a, b, sep=",") # 1,2
```

# 반복문

for-else문

```python
for x in range(10):
  if x >= 11:
    break
else:
  print("for-else") # for-else
```

> for문이 정상종료(break 없이)되면 else 문이 실행된다.

# 문자열

.upper()  
.lower()  
.isupper()  
.islower()  
string.find("str") : 문자열 찾기  
string.isalpha(): 알파벳인 경우 true  
ord(string) : 문자열의 ASCII 넘버

# 리스트

```python
# 리스트 더하기
a = [1]
b = [2]
print(a + b) # [1, 2]

# 리스트 곱하기
a = [0] * 3
print(a) # [0, 0, 0]


a = [1,2,3,4]

# 요소 추가하기
a.append(3) # [1, 2, 3, 4, 3]
a.insert(0,3) # [3, 1, 2, 3, 4]

# 빼기
a.pop() # [1,2,3]
a.pop(1) # [1,3,4]
a.remove(1) # [2,3,4]

# 찾기
a.index(1) # 0

# 연산
sum(a) # 10
max(a) # 4
min(a) # 1

# 정렬
a.sort() # [1,2,3,4]
a.sort(reverse=True) # [4,3,2,1]

# 초기화
a=list()
a=[]
a.clear()
a = [1,2]
a = list(range(1,3))
```

# 리스트 내장함수

```python
a = [1,21,13,24]
# slice
print(a[:1]) # [1]
# length
print(len(a)) # 4

# 리스트 요소 접근하기
for i in range(len(a)):
    print(a[i], end=" ") # 1 21 13 24
print()

for x in a:
    print(x, end=" ") # 1 21 13 24
print()


# enumerate
# list -> tuple, 요소의 index와 value 모두 접근
for x in enumerate(a):
    print(x) # (0, 1) (1, 21) (2, 13) (3, 24)

# tuple : unchangable, 바꿀 수 없다.
b = (1,2)
b[0] = 2 # ERROR!!!

for x in enumerate(a):
    print(x[0], x[1], sep="/") # 0/1 1/21 2/13 3/24

for index, value in enumerate(a):
    print(index, value) # 0 1  1 21  2 13  3 24

# all : 모든 조건이 참인 경우 참
if all(15 > x for x in a): # NO
    print("YES")
else:
    print("NO")

# any : 하나라도 참이면 참
if any(15 > x for x in a): # YES
    print("YES")
else:
    print("NO")
```

# 이차원 리스트

```python
# 이차원 배열 만들기
a = [[0] * 3]
print(a) # [[0,0,0]]

a = [[0]*3 for _ in range(3)]
print(a) # [[0,0,0][0,0,0][0,0,0]]

# 요소 접근하기(순회)
for x in a:
  print(x) # [0,0,0]
  for y in x:
    print(y) # 0

# 요소 접근하기(직접)
a[0][1] = 1
a[1][1] = 2
print(a) = [[0,1,0][0,2,0][0,0,0]]
```
