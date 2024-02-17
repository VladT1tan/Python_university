def remove_zeroes(numbers: list[int]) -> int:
    fast = count_zero = index_zero = 0

    for idx in numbers:
        if idx == 0:
            index_zero = numbers.index(0)
            break

    for num in numbers:
        if num == 0:
            fast += 1
            numbers.remove(0)
            count_zero += 1
        else:
            fast += 1
            continue

    numbers += [0] * count_zero
    return index_zero

nums = [0,42,21,0,100,0,5,1,0,7,3,0,404,0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42,21,100,5,1,7,3,404]

print(new_len)
print(nums[:new_len])
print()

nums = []
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [0]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [00000]
new_len = remove_zeroes(nums)

assert new_len == 0
assert nums[:new_len] == []

print(new_len)
print(nums[:new_len])
print()

nums = [0,0,0,0,42,21,0,100,0,5,1,0,7,3,0,404,0,0,0,0]
new_len = remove_zeroes(nums)

assert new_len == 8
assert nums[:new_len] == [42,21,100,5,1,7,3,404]

print(new_len)
print(nums[:new_len])
print()
