def find_sum_between_max_min(arr):
    """
    Находит сумму отрицательных элементов между максимальным и минимальным элементами массива.
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
    negative_elements = []
    for i in range(start + 1, end):  # +1 чтобы не включать сами max/min элементы
        if arr[i] < 0:
            sum_negative += arr[i]
            negative_elements.append((i, arr[i]))
    
    return sum_negative, negative_elements, start, end

def main():
    # Тестовые примеры
    test_arrays = [
        [5, -2, 8, -3, 1, -4, 9],  # Пример 1: max и min рядом
        [1, -5, 3, -2, 7, -1, 4],  # Пример 2: есть отрицательные между
        [-1, 2, -3, 4, -5],        # Пример 3: max и min рядом
        [10, 5, 3, 1, 8],          # Пример 4: нет отрицательных
        [1, 2, 3, 4, 5],           # Пример 5: нет отрицательных
        [5, -1, 3, -2, 8, -3, 2],  # Пример 6: есть отрицательные между
        [2, -4, 1, -1, 3, -2, 5]   # Пример 7: несколько отрицательных между
    ]
    
    for i, arr in enumerate(test_arrays, 1):
        print(f"\n=== Тест {i} ===")
        print(f"Массив: {arr}")
        
        max_val = max(arr)
        min_val = min(arr)
        max_index = arr.index(max_val)
        min_index = arr.index(min_val)
        
        print(f"Максимальный элемент: {max_val} (индекс {max_index})")
        print(f"Минимальный элемент: {min_val} (индекс {min_index})")
        
        result, negative_elements, start, end = find_sum_between_max_min(arr)
        
        print(f"Диапазон поиска: индексы {start+1} до {end-1}")
        if negative_elements:
            print(f"Отрицательные элементы между max и min: {[elem[1] for elem in negative_elements]}")
            print(f"Их индексы: {[elem[0] for elem in negative_elements]}")
        else:
            print("Отрицательных элементов между max и min не найдено")
        
        print(f"Сумма отрицательных элементов: {result}")

if __name__ == "__main__":
    main()
