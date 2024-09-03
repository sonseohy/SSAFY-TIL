def recur(level, alst, blst):   # 부분집합
    if level == N:
        if len(alst) != len(blst):
            return


    recur(level+1, alst+[level], blst)
    recur(level+1, alst, blst+[level])

def combi(level, st):   # 조합
    if level == M:
        pass

    for i in range(st, N-M+level+1):
        select[level] = i