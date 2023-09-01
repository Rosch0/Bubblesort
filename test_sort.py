from Sort import Sorter

def test_bubble_sort():
    #Sorting from smallest to largest number
    sorter = Sorter()
    numbers1 = [9, 5, 2, 8, 1, 3, 10, 7, 6, 4]
    sorter.bubble_sort(numbers1)
    assert numbers1 == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

test_bubble_sort()