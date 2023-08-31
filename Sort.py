def bubble_sort(list):
    n = len(list)
    
    for i in range(n):
        changed = False
        for j in range(0, n - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                changed = True
                print(list)
        if not changed:
            break
                
numbers = [9, 5, 2, 8, 1, 3, 10, 7, 6, 4]

bubble_sort(numbers)

print("Posortowana lista:", numbers)