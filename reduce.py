def reduce(iterable, fn, memo):
    for item in iterable:
        memo = fn(item, memo)
    return memo


def partition(iterable, fn):
    return ([item for item in iterable if fn(item)], [item for item in iterable if not fn(item)])


#print(reduce([1,2,3,4,5], lambda item, memo: memo + 1 if item % 2 == 0 else memo, 0))
print(partition([1,2,3,4,5,6], lambda x: x % 3 == 0))
print(reduce([2,4,6,7], lambda item, memo: item % 2 == 0 and memo, True))