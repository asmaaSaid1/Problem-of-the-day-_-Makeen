# Python function that rotates a list to the left:


def rotate_left(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]


num_rotation=int(input("enter number of rotations?"))
print(rotate_left([1, 2, 3, 4, 5],num_rotation ))


