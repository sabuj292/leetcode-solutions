def romanToInt(s):
    roman = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}
    
    total = 0
    i = 0

    while i < len(s):
        if i + 1 < len(s) and roman[s[i + 1]] > roman[s[i]]:
            total += roman[s[i + 1]] - roman[s[i]]
            i += 2
        else:
            total += roman[s[i]]
            i += 1
    return total

print(romanToInt("III"))    # 3
print(romanToInt("IV"))     # 4
print(romanToInt("IX"))     # 9
print(romanToInt("LVIII"))  # 58
print(romanToInt("MCMXCIV"))# 1994
