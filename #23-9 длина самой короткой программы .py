for d in range (1,20): #прогоняем длину - (d) программы
    def f(s, e, d, c):
        if s > e or c > d: # c > d если он не дошел до 9217 за заданную длинну, выводим нолик
            return 0
        if s == e:
            return 1
        if s < e:
            return f(s + 1, e, d, c + 1) + f(s * 2, e, d, c + 1) + f(s * 3, e, d, c + 1) #совершаем действие и увеличиваем счетчик действий на единицу
    if f(1, 9217, d, 0) != 0: #если он все-таки дошел за заданную длинну до 9217, то есть вывел НЕ ноль
        print(d) #то сразу выводим ответ, ведь это и есть минимальная длинна
        break