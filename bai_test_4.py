def is_non_decreasing(num):
    num_str = str(num)
    return all(num_str[i] <= num_str[i + 1] for i in range(len(num_str) - 1))

def count_non_decreasing_numbers(file_path):
    non_decreasing_numbers = {}
    with open(file_path, 'r') as file:
        for line in file:
            numbers = list(map(int, line.strip().split()))
            for num in numbers:
                if is_non_decreasing(num):
                    if num in non_decreasing_numbers:
                        non_decreasing_numbers[num] += 1
                    else:
                        non_decreasing_numbers[num] = 1
    return non_decreasing_numbers

def main():
    data1 = count_non_decreasing_numbers('DATA1.in')
    data2 = count_non_decreasing_numbers('DATA2.in')

    common_numbers = sorted(set(data1.keys()) & set(data2.keys()))
    
    for num in common_numbers:
        print(num, data1[num], data2[num])

if __name__ == "__main__":
    main()
