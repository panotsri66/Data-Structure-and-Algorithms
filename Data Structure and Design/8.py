s = list('a-139+*ง/0ขtอีAคะจeBstaiก')

is_sorted = False
while not is_sorted:
    for i in range(len(s)-1):
        if s[i] > s[i+1]:
            s[i+1], s[i] = s[i], s[i+1]
            break
    else:
        is_sorted=True

print("".join(s))


A="กอสะฟ"
print(A[3])