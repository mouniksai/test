def revstr(x, r):
    if r>=0:
        return x[r] + revstr(x, r-1)
    else:
        pass
revstr('madam', 4)
