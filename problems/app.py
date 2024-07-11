def canConstruct(ransomNote: str, magazine: str) -> bool:
    freq = {}
    for i in magazine:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    for i in ransomNote:
        if i in freq:
            freq[i] -= 1
            if freq[i] < 0:
                return False
        else:
            return False
    
    return True

if __name__ == '__main__':
    print(canConstruct("a", "b"))
    print(canConstruct("aa", "ab"))
    print(canConstruct("aa", "aab"))
    print(canConstruct("a", "b"))
    print(canConstruct("aa", "aab"))