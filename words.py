words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']

word = []

for i in range(len(words)):
    words[i] = list(str(words[i]))
    words[i].sort()
    word += [''.join(words[i])]     # set 변환을 위해 join() 사용

word_set = set(word)
word_list = list(word_set)          # 중복 제거 후 다시 list 변환

grouping = {}

for x in range(len(word_list)):
    grouping[word_list[x]] = ''         # [word_list[x]] key값에 대입하기 위해 비어있는 value 생성
    for i in range(len(word)):
        if word_list[x] == word[i]:
            grouping[word_list[x]] += word_list[x]
            
for key, value in grouping.items():
    print(f'{key} : {value}', end= ' / ')
