def digitize(n):
    return list(map(int, sorted(list(str(n)), reverse=True)))


    

digitize(135)