def urlify(text: list[str]) -> int:
    slow = fast = 0
    count_space = 0

    while fast < len(text):
        if text[fast] == '':
            break
        if text[fast] == ' ':
            count_space += 1
        fast += 1

    del text[:fast - 1:-1]
    new_size = fast - 1 + (2 * count_space)
    text += [''] * (2 * count_space)

    slow = len(text) - 1
    fast -= 1

    while fast >= 0:
        if text[fast] == ' ':
            text[slow] = '0'
            text[slow - 1] = '2'
            text[slow - 2] = '%'
            slow -= 3
        else:
            text[slow] = text[fast]
            slow -= 1

        fast -= 1

    return new_size + 1


text = list('my url') + [''] * 21
new_len = urlify(text)

assert new_len == 8
assert text[:new_len] == list('my%20url')

text = list('')
new_len = urlify(text)

assert new_len == 0
assert text[:new_len] == list('')

text = list(' my url ')
new_len = urlify(text)

assert new_len == 14
assert text[:new_len] == list('%20my%20url%20')

text = list(' my   url ')
new_len = urlify(text)

assert new_len == 20
assert text[:new_len] == list('%20my%20%20%20url%20')

text = list(' my url with multiple spaces and words ')
new_len = urlify(text)

assert new_len == 55
assert text[:new_len] == list('%20my%20url%20with%20multiple%20spaces%20and%20words%20')

text = list(' ')
new_len = urlify(text)

assert new_len == 3
assert text[:new_len] == list('%20')

text = list('myurl')
new_len = urlify(text)

assert new_len == 5
assert text[:new_len] == list('myurl')

text = list('  ')
new_len = urlify(text)

assert new_len == 6
assert text[:new_len] == list('%20%20')
