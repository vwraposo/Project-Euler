def prod (l):
    ans = 1
    for i in l:
        ans *= i
    return ans

s = str (input ())
l = list (map (int, s));
#print (l)
ans = 0;
for i in range (0, 1000):
    p = prod (l[i:i+13])
    if (p > ans):
        ans = p
print (ans)
