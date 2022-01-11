def try_me(n):
    if n > 0:
        return n + try_me(n-1)
    else:
        return 0
