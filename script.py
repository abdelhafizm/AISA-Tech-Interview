def question_1(file_name):
    # Write a program that outputs:
    # 1. How many numbers are in the dataset.
    # 2. The sum of the numbers.
    # 3. The average of the numbers.
    nums = []
    with open(file_name) as file: 
        for row in file:
            nums = nums + row.strip().split(" ")

    print("numbers in dataset: ", len(nums))
    
    sum = 0

    for n in nums:
        sum += int(n)
    
    print("sum: ", sum)

    print("average: ", sum/100)

    return



def question_2(file_name):
    # Write a program that outputs:
    # 1. How many unique numbers are in the dataset.
    # 2. Which numbers show up more than twice in the dataset, and how many times do they appear.
    nums = []
    with open(file_name) as file: 
        for row in file:
            nums = nums + row.strip().split(" ")


    unique_nums = {}

    for n in nums:
        if n not in unique_nums:
            unique_nums[n] = 1
            continue
        unique_nums[n] += 1
    
    
    print("number of unique nums: ", len(unique_nums))

    for a in unique_nums:
        if unique_nums[a] > 2:
            print("number: ", a, " appears ", unique_nums[a], "times" )


    return 



def run_interview(file_name):
    question_1(file_name)
    question_2(file_name)


if __name__ == '__main__':
    file_name = 'input.txt'
    run_interview(file_name)
