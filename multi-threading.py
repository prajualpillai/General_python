import threading
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime

import numpy as np
import pandas as pd

THREAD_POOL_SIZE = 6
thread_pool = ThreadPoolExecutor(max_workers=THREAD_POOL_SIZE)

pending_threads: dict = {
    "threads": []
}


def wait_for_ops():
    while pending_threads["threads"]:
        thread = pending_threads["threads"].pop()
        thread.result()


class MultiThreading():

    def __init__(self):
        self.actual = []
        self.sum = 0
        self.lock = threading.Lock()

    def modify_data(self, value):
        """
        Dummy function to mimic any modification done to data
        :param value:
        :return:
        """
        self.lock.acquire()
        self.actual.append(str(value))
        self.lock.release()

    def df_handling_async(self, arr):
        for i in arr:
            add_thread = thread_pool.submit(
                self.modify_data,
                value=i
            )
            pending_threads["threads"].append(add_thread)

        wait_for_ops()
        return pd.DataFrame(self.actual, columns=["new_data"])

    def add_data(self, value):
        value = value ** 2
        value = value ** 0.5
        value += value
        self.lock.acquire()
        self.sum += value
        self.lock.release()

    def add_async(self, arr):
        for i in arr:
            add_thread = thread_pool.submit(
                self.add_data,
                value=i
            )
            pending_threads["threads"].append(add_thread)

        wait_for_ops()

        return self.sum

    def regular_add(self, arr):
        """
        Performs regular sum of the array
        :param arr:
        :return:
        """
        arr_sum = 0
        for i in arr:
            temp = i
            temp = temp ** 2
            temp = temp ** 0.5
            temp += temp
            arr_sum += temp
        return arr_sum


if __name__ == "__main__":
    arr = list(map(int, input("Enter space separated values: ").split(" ")))
    arr = arr * 40
    obj = MultiThreading()
    st = datetime.now()
    ans = obj.add_async(arr)
    print(f"sum: {ans}, Time: {datetime.now() - st}")
    st = datetime.now()
    ans = obj.regular_add(arr)
    print(f"sum: {ans}, Time: {datetime.now() - st}")
