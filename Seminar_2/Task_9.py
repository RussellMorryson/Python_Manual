# По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1 Решить задачу используя цикл
# while
# Input: 5
# Output: 120

# Произведение чисел от 1 до N

N = int(input("Введите число N: "))
result = 1
while(N > 0):
    result = result * N
    N -= 1
print (result)