import version1
import version2

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    solution1 = version1.Solution()
    solution2 = version2.Solution()

    test_nums = [
        [1, 2, 3, 1],
        [1, 2, 3, 4],
        [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
    ]
    for test_case in test_nums:
        print("Solution 1: {0}".format(str(solution1.containsDuplicate(test_case))))
        print("Solution 2: {0}".format(str(solution2.containsDuplicate(test_case))))

