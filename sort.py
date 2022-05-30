from datetime import datetime
import sys

sys.setrecursionlimit(10000)


def selection_sort(arr):
    """
    Has a complexity of O(n^2)
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[j] < arr[i]:
                (arr[j], arr[i]) = (arr[i], arr[j])
    return arr


def insertion_sort(arr):
    """

    :param arr:
    :return:
    """
    for i in range(len(arr)):
        pos = i
        while pos > 0 and arr[pos] < arr[pos - 1]:
            (arr[pos], arr[pos - 1]) = (arr[pos - 1], arr[pos])
            pos -= 1
    return arr


def insert(seq, k):
    pos = k
    while pos > 0 and seq[pos] < seq[pos - 1]:
        (seq[pos], seq[pos - 1]) = (seq[pos - 1], seq[pos])
        pos -= 1
    return seq


def issort(seq, k):
    """

    :param seq:
    :param k:
    :return:
    """
    if k > 1:
        seq = issort(seq, k - 1)
        seq = insert(seq, k - 1)
    return seq


if __name__ == "__main__":
    # arr_ip = list(map(int, input("Enter sorted space separated values - ").split(" ")))
    arr_ip = list(range(5000, 0, -1))
    arr_ip2 = arr_ip[0:]
    arr_ip3 = arr_ip[0:]
    # st = datetime.now()
    # print(selection_sort(arr_ip), "time", datetime.now() - st)
    st = datetime.now()
    insertion_sort(arr_ip2)
    print("time", datetime.now() - st)
    st = datetime.now()
    issort(arr_ip3, len(arr_ip3))
    print("time", datetime.now() - st)
