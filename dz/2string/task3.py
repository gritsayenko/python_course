s = 'Nisl scelerisque justo per hac cras purus lectus maecenas litora facilisi potenti'
s_last = s[-1]
r = []
for i in range(0, len(s)):
    if s[i] == s_last:
        r.append(i+1)
print(*r, sep=", ")
