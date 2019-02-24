import sys
import unittest
import io
from contextlib import redirect_stdout


class OptimizedMath:
    def __init__(self):
        self.start = None
        self.end = None
        self.number_representation = {
            1: "one",
            2: "two",
            3: "three",
            4: "four",
            5: "five",
            6: "six",
            7: "seven",
            8: "eight",
            9: "nine",
        }

    def set_start(self, start):
        self.start = start

    def set_end(self, end):
        self.end = end

    def get_number_name(self, num):
        return self.number_representation.get(num)

    def process_divisors(self, divisors):
        base_respond = "The number "
        if divisors is None:
            for num in range(self.start, self.end + 1):
                print(base_respond + "'{}' is {}.".format(num, odd_even_string_repr(num)))
        else:
            divisibles = []
            for num in range(self.start, self.end + 1):
                divisibles.clear()
                for divisor in divisors:
                    if is_divisible_by_num(num, divisor):
                        if not is_odd(num) and not divisibles:
                            divisibles.append(self.get_number_name(2))
                        divisibles.append(self.get_number_name(divisor))
                if not divisibles:
                    print(base_respond + "'{}' is {}.".format(num, odd_even_string_repr(num)))
                else:
                    print(base_respond + "'{}' is divisible by {}.".format(num, ' and '.join(divisibles)))


class MathTest(unittest.TestCase):
    def test_one_to_six_by_three(self):
        test_string = "The number '1' is odd." \
                      "\nThe number '2' is even." \
                      "\nThe number '3' is divisible by three." \
                      "\nThe number '4' is even." \
                      "\nThe number '5' is odd." \
                      "\nThe number '6' is divisible by two and three."
        self.om = OptimizedMath()
        self.om.set_start(1)
        self.om.set_end(6)
        to_test = io.StringIO()
        with redirect_stdout(to_test):
            self.om.process_divisors([3])

        self.assertMultiLineEqual(to_test.getvalue().rstrip(), test_string)

    def test_one_to_thirty_by_three_and_five(self):
        test_string = "The number '1' is odd." \
                      "\nThe number '2' is even." \
                      "\nThe number '3' is divisible by three." \
                      "\nThe number '4' is even." \
                      "\nThe number '5' is divisible by five." \
                      "\nThe number '6' is divisible by two and three." \
                      "\nThe number '7' is odd." \
                      "\nThe number '8' is even." \
                      "\nThe number '9' is divisible by three." \
                      "\nThe number '10' is divisible by two and five." \
                      "\nThe number '11' is odd." \
                      "\nThe number '12' is divisible by two and three." \
                      "\nThe number '13' is odd." \
                      "\nThe number '14' is even." \
                      "\nThe number '15' is divisible by three and five." \
                      "\nThe number '16' is even." \
                      "\nThe number '17' is odd." \
                      "\nThe number '18' is divisible by two and three." \
                      "\nThe number '19' is odd." \
                      "\nThe number '20' is divisible by two and five." \
                      "\nThe number '21' is divisible by three." \
                      "\nThe number '22' is even." \
                      "\nThe number '23' is odd." \
                      "\nThe number '24' is divisible by two and three." \
                      "\nThe number '25' is divisible by five." \
                      "\nThe number '26' is even." \
                      "\nThe number '27' is divisible by three." \
                      "\nThe number '28' is even." \
                      "\nThe number '29' is odd." \
                      "\nThe number '30' is divisible by two and three and five."

        self.om = OptimizedMath()
        self.om.set_start(1)
        self.om.set_end(30)
        to_test = io.StringIO()
        with redirect_stdout(to_test):
            self.om.process_divisors([3, 5])

        self.assertMultiLineEqual(to_test.getvalue().rstrip(), test_string)


def is_odd(num):
    return num & 1


def is_divisible_by_num(current, divisor):
    return current % divisor == 0


def odd_even_string_repr(num):
    if is_odd(num):
        return "odd"
    else:
        return "even"

if __name__ == "__main__":
    """
    Unit tests to validate design
    """
    setup_test = MathTest()
    setup_test.test_one_to_six_by_three()
    setup_test.test_one_to_thirty_by_three_and_five()

    # default case provide on request for 1 to 100 inclusive, divisors of 3
    try:
        if len(sys.argv) < 2:
            om = OptimizedMath()
            om.set_start(1)
            om.set_end(100)
            om.process_divisors([3, 5])
        else:
            # expanded program to take dynamic start, end, and set of multiple divisors
            # take arguments of start, end, and set of divisors from command line
            om = OptimizedMath()
            om.set_start(int(sys.argv[1]))
            om.set_end(int(sys.argv[2]))
            om.process_divisors([int(divisor) for divisor in sys.argv[3].split(',')])
    except Exception as e:
        # log exception somewhere
        print('Error running program: {}'.format(e))
