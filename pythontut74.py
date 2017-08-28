# 1, 1, 2, 3, 5, 8,
''' fibbonachi numbers'''

fn = []

def FN(num):
    if num == 0:
        result = 0
    elif num == 1:
        result = 1
    else:
        result = (FN(num-1)+FN(num-2))
    return result

for i in range (1,15):
    fn.append(FN(i))

print(fn)

