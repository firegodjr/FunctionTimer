import neattime


filepath = input("Enter the name of the test file you want to use: ")
tester = neattime.TimeTester(filepath)
results = tester.test_all(300)

csv = ""
for case in results.keys():
    csv += "{},\n".format(str(case))
    for arg in results[case].keys():
        csv += ",{},{},\n".format(str(arg), str(",".join(results[case][arg])))

csv_file = open("RESULTS_{}.csv".format(filepath), "w+")
csv_file.write(csv)
csv_file.close()
