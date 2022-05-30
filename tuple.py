a = (2,3,5,6,4,5,2,1,19,63)


print("Tuple a = ", a)
print("a có ", len(a), "phan tu")

dem = 0
for i in a[:]:
    if i%2 == 0:
        dem += 1

print("Phan tu chan : ", dem)