# Daily Workshop

## 1. 간단한 N의 약수

<br>

<br>

## 2. List의 합 구하기

```py
def list_sum(lst):
    total = 0
    for i in lst:
        total += i
    print(total)
    
list_sum([1, 2, 3, 4, 5])
```

<br>

<br>

## 3. Dictionary로 이루어진 List의 합 구하기

```py
def dict_list_sum(lst):
    result = 0
    for dict in lst:
        result += dict['age']
    print(result)

dict_list_sum([{'name' : 'kim', 'age' : 12}, {'name' : 'lee', 'age' : 4}])

```

<br>

<br>

## 4. 2차원 List의 전체 합 구하기

```py
def all_list_sum(lst):
    total = 0
    for i in lst:
        for j in i:
            total += j
    print(total)

all_list_sum([[1], [2, 3], [4, 5, 6], [7, 8, 9, 10]])

```

<br>

<br>

## 5. 숫자의 의미

```py
def get_secret_word(lst):
    word = []
    for i in lst:
        word.append(chr(i))
    print(''.join(word))

get_secret_word([83, 115, 65, 102, 89])

```

