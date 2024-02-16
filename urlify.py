def urlify(text: list[str]) -> int:
    slow = fast = 0
    count_space = 0

    while fast < len(text):
        if text[fast] == ' ':
            count_space += 1
        fast += 1

    count_space *= 2
    text += [''] * count_space

    slow = len(text) - 1
    fast -= 1
    while fast > 0:
        if text[fast] == ' ':
            fast -= 1
            break
        else:
            text[slow], text[fast] = text[fast], text[slow]
            fast -= 1
            slow -= 1

    while slow > 0:
        if text[slow] == ' ' or text[slow] == '':
            text[slow] = '0'
            slow -= 1
            text[slow] = '2'
            slow -= 1
            text[slow] = '%'
            slow -= 1
        else:
            slow -= 1

    return len(text)


text = list('my    url  ')
new_len = urlify(text)

assert new_len == 26
assert text[:new_len] == list('my%20%20%20%20url%20%20')