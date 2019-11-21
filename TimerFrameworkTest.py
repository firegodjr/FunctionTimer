import neattime


filepath = input("Enter the name of the test file you want to use: ")
tester = neattime.TimeTester(filepath)
results = tester.test_all(300)

csv = ""
for case in results.keys():
    csv += "{},\n".format(case)
    for arg in results[case].keys():
        csv += ",{},{},\n".format(arg, ",".join(results[case][arg]))