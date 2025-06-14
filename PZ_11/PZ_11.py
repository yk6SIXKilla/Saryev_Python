import random


# Генерация двух файлов с последовательностями чисел
def generate_file(filename, count):
    numbers = [random.randint(-20, 20) for _ in range(count)]
    with open(filename, 'w') as f:
        f.write(' '.join(map(str, numbers)))
    return numbers


numbers1 = generate_file('file1.txt', 20)
numbers2 = generate_file('file2.txt', 20)


# Чтение файлов и обработка данных
def read_numbers(filename):
    with open(filename, 'r') as f:
        return list(map(int, f.read().split()))


nums1 = read_numbers('file1.txt')
nums2 = read_numbers('file2.txt')

# Элементы первого и второго файлов
all_nums1 = nums1
all_nums2 = nums2

# Элементы первого файла, присутствующие во втором
in_both_1 = [n for n in nums1 if n in nums2]

# Элементы второго файла, присутствующие в первом
in_both_2 = [n for n in nums2 if n in nums1]

# Количество элементов
total_count = len(nums1) + len(nums2)

# Количество отрицательных и положительных элементов
neg_count = sum(1 for n in nums1 + nums2 if n < 0)
pos_count = sum(1 for n in nums1 + nums2 if n > 0)

# Запись результата в новый файл
with open('result.txt', 'w') as f:
    f.write('Элементы первого файла:\n')
    f.write(' '.join(map(str, all_nums1)) + '\n\n')
    f.write('Элементы второго файла:\n')
    f.write(' '.join(map(str, all_nums2)) + '\n\n')
    f.write('Элементы первого файла, присутствующие во втором:\n')
    f.write(' '.join(map(str, in_both_1)) + '\n\n')
    f.write('Элементы второго файла, присутствующие в первом:\n')
    f.write(' '.join(map(str, in_both_2)) + '\n\n')
    f.write(f'Количество элементов: {total_count}\n')
    f.write(f'Количество отрицательных элементов: {neg_count}\n')
    f.write(f'Количество положительных элементов: {pos_count}\n')

print('Готово! Результаты записаны в файл result.txt')
