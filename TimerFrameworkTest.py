import neattime
from MCMmethods import memo_wrapper, recursive_wrapper, bottom_wrapper, optimal_parenth


filepath = input("Enter the name of the test file you want to use (Why not try MCM_test.txt?): ")
tester = neattime.TimeTester(filepath)
results = tester.test_all(1)

csv = ""
for case in results.keys():
    for arg in results[case].keys():
        csv += "{},{},\n".format(case, ",".join(map(str, results[case][arg])))

csv_file = open("RESULTS_{}.csv".format(filepath), "w+")
csv_file.write(csv)
csv_file.close()


print(optimal_parenth(memo_wrapper([1, 2, 3, 4, 5, 6, 7]), 1, 6))
print(optimal_parenth(recursive_wrapper([1, 2, 3, 4, 5, 6, 7]), 1, 6))
print(optimal_parenth(bottom_wrapper([1, 2, 3, 4, 5, 6, 7]), 1, 6))