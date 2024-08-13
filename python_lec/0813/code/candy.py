queue = []
new_no = 1
queue.append((new_no, 1))

total = 0
while True:
    no, cnt = queue.pop(0)
    total += cnt
    if total >= 20:
        print(no, total)
        break

    queue.append((no, cnt+1))
    new_no += 1
    queue.append((new_no, 1))
    print(queue)


# no, cnt = queue.pop(0)
# queue.append((no, cnt+1))
# queue.append((new_no + 1, 1))
# #[(1, 2), (2, 1)]
#
# no, cnt = queue.pop(0)
# queue.append((no, cnt+1))
# queue.append((new_no + 1, 1))
# # [(2, 1), (1, 3), (3, 1)]
#
# no, cnt = queue.pop(0)
# queue.append((1, cnt+1))
# queue.append((new_no + 1, 1))
# # [(2, 1), (1, 3), (3, 1)]
#
# no, cnt = queue.pop(0)
# queue.append((no, cnt+1))
# queue.append((new_no + 1, 1))
