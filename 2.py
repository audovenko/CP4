a, b = map(int, input("Введите размерность двух массивов через пробел, нажмите ENTER, введите первый массив, нажмите ENTER, введите второй массив ").split())
ans = []
x = [int(i) for i in input().split()]
y = [int(i) for i in input().split()]
for i in x:
    if i in y and i not in ans:
        ans.append(i)

print(ans)

