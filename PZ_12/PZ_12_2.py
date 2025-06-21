#Составить генератор (yield), который переведет символы строки из нижнего
#регистра в верхний.


def to_upper_generator(s):
    for char in s:
        yield char.upper()

# Пример использования:
input_str = "привет, мир!"
result = ''.join(to_upper_generator(input_str))
print(result)