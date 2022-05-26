from datetime import datetime


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


if __name__ == "__main__":
    arr_ip = list(map(int, input("Enter sorted space separated values - ").split(" ")))
    arr_ip2 = arr_ip[0:]
    st = datetime.now()
    print(selection_sort(arr_ip), "time", datetime.now() - st)
    st = datetime.now()
    print(insertion_sort(arr_ip2), "time", datetime.now() - st)
