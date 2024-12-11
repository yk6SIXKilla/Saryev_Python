#С начала суток прошло N секунд (N — целое). Найти количество
# секунд, прошедших с начала последнего часа
try:
    N = int(input("Введите количество секунд, прошедших с начала суток: "))
    seconds_in_hour = 3600
    seconds_passed_last_hour= N % seconds_in_hour
    print("Количество секунд, прошедших с начала последнего часа:", seconds_passed_last_hour)
except ValueError:
    print("Ошибка: введите целое число.")