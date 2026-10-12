def substrings(s: str, k: int):
    if k <= 0 or k > len(s):
        return
    for i in range(len(s) - k + 1):
        yield s[i:i + k]

print(list(substrings("abcdef", 3)))  
print(list(substrings("test", 5)))    