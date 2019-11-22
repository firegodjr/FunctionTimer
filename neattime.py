
# NeatTime by Ethan Schrunk
# A standardized solution for doing sets of timing tests
# This was probably unnecessary but I don't care
# 11/18/19

import timeit
import time
import traceback


# Contains the name and list input for a single test
class TestArguments:
    def __init__(self, name: str, array: list):
        self.name = name
        self.array = array


# Contains the name, function snippet, and initialization snippet for a particular algorithm
class TestCase:
    def __init__(self, name: str, func: str, init=""):
        self.name = name
        self.func = func
        self.init = init


# A class built for easy testing of multiple functions and array test cases
class TimeTester:
    # Plaintext test files have this structure:
    #
    #    case <name of case (eg. Bottom Up)>###<code to test>###<init for code>
    #    ...
    #    args <name of args (eg. Best Case)>###<list of args>
    #    ...
    #
    # "case" and "args" lines can be anywhere in the file, as long as
    #    they're on their own line
    def __init__(self, test_file_path=""):

        self.test_cases = []
        self.test_args = []

        if test_file_path != "":
            file = open(test_file_path, "r")
            line = file.readline()
            while line != "":
                if line.startswith("case"):
                    case = line[4:].split("###")
                    self.test_cases.append(TestCase(case[0].strip(" "), case[1].strip(" "), case[2].strip(" ")))
                elif line.startswith("args"):
                    args = line[4:].split("###")
                    self.test_args.append(TestArguments(args[0].strip(" "), eval(args[1])))
                line = file.readline()

            file.close()

    # Tests all given cases and returns a 2d dictionary with structure
    # { case.name : { args.name : time_per_n[] } }
    def test_all(self, run_count, max_len=100, step_count=1):
        case_times = {}
        for tc in self.test_cases:
            case_times[tc.name] = {}
            for a in self.test_args:
                if max_len > len(a.array):
                    max_len = len(a.array)
                times = self.test_n_range(tc, a, run_count, range(1, max_len, step_count))
                case_times[tc.name][a.name] = times
        return case_times

    # Tests the given case with the given args once per n in n_range
    @staticmethod
    def test_n_range(test_case: TestCase, test_args: TestArguments, run_count: int, n_range: list):
        times = []
        for n in n_range:
            array_str = str(test_args.array[:n])
            func = test_case.func.format(array_str, array_str, array_str, array_str)
            try:
                times.append(min(timeit.repeat(func, test_case.init, time.clock, run_count, 25)) / 25 * 10 ** 9)
            except Exception:
                print("Fatal error occurred when attempting to test {} with {}".format(test_case.name, test_args.name))
                traceback.print_exc()


        return times
