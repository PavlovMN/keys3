def find_sum_between_max_min(arr):
    """
    Находит сумму отрицательных элементов между максимальным и минимальным элементами массива.
    
    Args:
        arr: одномерный массив чисел
        
    Returns:
        int: сумма отрицательных элементов между max и min
    """
    if len(arr) == 0:
        return 0
    
    # Находим индексы максимального и минимального элементов
    max_index = arr.index(max(arr))
    min_index = arr.index(min(arr))
    
    # Определяем границы для поиска
    start = min(max_index, min_index)
    end = max(max_index, min_index)
    
    # Находим сумму отрицательных элементов между ними
    sum_negative = 0
    for i in range(start + 1, end):  # +1 чтобы не включать сами max/min элементы
        if arr[i] < 0:
            sum_negative += arr[i]
    
    return sum_negative

def main():
    # Ввод размера массива
    try:
        n = int(input("Введите размер массива N: "))
        if n <= 0:
            print("Размер массива должен быть положительным числом!")
            return
    except ValueError:
        print("Ошибка ввода! Введите целое число.")
        return
    
    # Ввод элементов массива
    arr = []
    print(f"Введите {n} элементов массива:")
    for i in range(n):
        try:
            element = float(input(f"Элемент {i+1}: "))
            arr.append(element)
        except ValueError:
            print("Ошибка ввода! Введите число.")
            return
    
    # Вывод исходного массива
    print(f"\nИсходный массив: {arr}")
    
    # Поиск максимального и минимального элементов
    max_val = max(arr)
    min_val = min(arr)
    max_index = arr.index(max_val)
    min_index = arr.index(min_val)
    
    print(f"Максимальный элемент: {max_val} (индекс {max_index})")
    print(f"Минимальный элемент: {min_val} (индекс {min_index})")
    
    # Вычисление суммы отрицательных элементов между max и min
    result = find_sum_between_max_min(arr)
    
    print(f"Сумма отрицательных элементов между максимальным и минимальным: {result}")

if __name__ == "__main__":
    main()
