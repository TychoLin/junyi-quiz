def reverse(S, start, stop):
    if start < stop - 1:
        S[start], S[stop - 1] = S[stop - 1], S[start]
        reverse(S, start + 1, stop - 1)


s = 'junyiacademy'
print(s)
s = list(s)
reverse(s, 0, len(s))
print(''.join(s))


sentence = 'flipped class room is important'
def reverse_sentence(sentence):
    data = sentence.split(sep=' ')
    for i, s in enumerate(data):
        data[i] = s[::-1]
    return ' '.join(data)
print(reverse_sentence(sentence))