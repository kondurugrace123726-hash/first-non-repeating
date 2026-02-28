def first_non_repeating(s: str):
    freq = {}

    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s:
        if freq[ch] == 1:
            return ch
    return -1

if __name__ == "__main__":
    ch = 'abcdabc'
    s = ch.strip()
    result = first_non_repeating(s)
    print(result)