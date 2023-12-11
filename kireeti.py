n = 10
k = 20

a = (n > 10) and (k == 20)
b = (n > 10) or (k == 20)
c = not((n > 10) and (k == 20))
d = not(n > 10) and not(k == 20)
e = (n > 10) or (k == 10 or k != 5)

print(f"a. (n > 10) and (k == 20) = {a}")
print(f"b. (n > 10) or (k == 20) = {b}")
print(f"c. not((n > 10) and (k == 20)) = {c}")
print(f"d. not(n > 10) and not(k == 20) = {d}")
print(f"e. (n > 10) or (k == 10 or k != 5) = {e}")
