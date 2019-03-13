la = [0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 0, 0]
count = 0
i = 0
while i < len(la) - 1:
    if la[i] == 0 and la[i+1] == 1:
        count += 1
    i += 1

print("count = {:d}\n".format(count))
