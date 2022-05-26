from datetime import datetime


def search(seq, v):
    """
    Simple binary search in an unsorted sequence, time taken same in list and array
    :param seq: sequence array or lists
    :param v: value
    :return: boolean
    """
    for x in seq:
        if x == v:
            return True
    return False


def bsearch(seq, v, l, r):
    """
    Binary search on a sorted sequence. BS on a sorted array has a complexity of Olog(n)
    :param seq:
    :param v: value to find
    :param l: lower limit of sequence
    :param r: upper limit of sequence
    :return:
    """
    if (r - l) == 0:
        return False

    mid = (l + r) // 2
    if v == seq[mid]:
        return True
    elif v < seq[mid]:
        bsearch(seq, v, l, mid)
    else:
        bsearch(seq, v, mid + 1, r)


if __name__ == "__main__":
    arr = list(map(int, input("Enter sorted space separated values - ").split(" ")))
    val = int(input("Enter value to be found - "))
    st = datetime.now()
    print(search(arr, val), "time", datetime.now() - st)
    st = datetime.now()
    print(bsearch(arr, val, 0, len(arr)), "time", datetime.now() - st)
