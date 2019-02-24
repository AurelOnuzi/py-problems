import threading
import sys
import unittest
import io
from contextlib import redirect_stdout


class ThreadSynchronization:
    def __init__(self, start, end, step_rate, event_set, event_clear):
        self.start = start
        self.end = end
        self.step_rate = step_rate
        self.event_set = event_set
        self.event_clear = event_clear

    def output_thread_and_num(self):
        for i in range(self.start, self.end + 1, self.step_rate):
            print("Thread {}: The number is '{}'".format(threading.currentThread().getName(), i))
            self.event_set.set()
            self.event_clear.clear()
            self.event_clear.wait()
        self.event_set.set()


class ThreadTest(unittest.TestCase):
    def test_one_to_three(self):
        test_threads = []
        first_thread_event = threading.Event()
        second_thread_event = threading.Event()
        to_test = io.StringIO()
        test_string = "Thread 1: The number is '1'" \
                      "\nThread 2: The number is '2'" \
                      "\nThread 1: The number is '3'"

        ts_odd = ThreadSynchronization(1, 3, 2, first_thread_event, second_thread_event)
        ts_even = ThreadSynchronization(2, 3, 2, second_thread_event, first_thread_event)
        threads.append(threading.Thread(name="1", target=ts_odd.output_thread_and_num))
        threads.append(threading.Thread(name="2", target=ts_even.output_thread_and_num))

        with redirect_stdout(to_test):
            for test_thread in test_threads:
                test_thread.start()
            for test_thread in test_threads:
                test_thread.join()

        self.assertMultiLineEqual(to_test.getvalue().rstrip(), test_string)

if __name__ == "__main__":
    """
    Unit tests to validate design
    """
    setup_test = ThreadTest()
    setup_test.test_one_to_three()

    threads = []
    first_event = threading.Event()
    second_event = threading.Event()

    # default case provide on request for 1 to 100 inclusive, divisors of 3
    try:
        if len(sys.argv) < 2:
            first_thread = ThreadSynchronization(1, 100, 2, first_event, second_event)
            second_thread = ThreadSynchronization(2, 100, 2, second_event, first_event)
        else:
            # take arguments of start, end from command line
            first_thread = ThreadSynchronization(int(sys.argv[1]), int(sys.argv[2]), 2, first_event, second_event)
            second_thread = ThreadSynchronization(int(sys.argv[1]) + 1, int(sys.argv[2]), 2, second_event, first_event)

        threads.append(threading.Thread(name="1", target=first_thread.output_thread_and_num))
        threads.append(threading.Thread(name="2", target=second_thread.output_thread_and_num))
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()

    except Exception as e:
        # log exception somewhere
        print('Error running program: {}'.format(e))
