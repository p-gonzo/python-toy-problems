def merge_sort(l, comparator=lambda x, y: x < y):

    def split(l):
        if len(l) < 2:
            return l
        
        left = l[ : len(l) // 2 ]
        right = l[ len(l) // 2 : ]

        sorted_left = split(left)
        sorted_right = split(right)

        return(merge(sorted_left, sorted_right))

    def merge(left, right):
        result = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if comparator(left[i], right[j]):
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result += left[i:]
        result += right[j:]

        return result

    return split(l)

print(merge_sort([6,4,9,8]))
def obj_comparator(a, b):
    return a['val'] < b['val']
print(merge_sort([{'val': 6}, {'val': 4}, {'val': 9}, {'val': 8}], obj_comparator))