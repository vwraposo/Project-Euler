ans = 0;
for x in range (999, 99, -1):
    for y in range (999, 99, -1):
        pal = str (x * y)
        if pal == pal[::-1] and int (pal) > ans:
            ans = int (pal)
print (ans)
