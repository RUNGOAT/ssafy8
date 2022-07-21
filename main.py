lst = [1, 1, 3, 3, 0, 1, 1]

# i = 0
# while lst[i]:
for i in range(len(lst) - 1):
    a = 0
    if lst[i] == lst[i+1]:
        lst[i+1] = None
    i += 1
for i in lst:
    if i == None:
        lst.remove(i)

print(lst)

    