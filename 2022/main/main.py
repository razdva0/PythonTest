def decrypt(encrypted_text, n):
    final = encrypted_text
    s = int(len(final) / 2)
    j = 0
    while j < n:
        i = 0
        text = ''
        while i < s:
            text += final[i + s - 1]
            text += final[i]
            i += 1
        final = text
        j += 1
    return final
