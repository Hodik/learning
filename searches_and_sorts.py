def bubble_sort(numbers: list[int]) -> list[int]:
   
    
    for i in range(len(numbers) - 1):
        swapped: bool = False
        for j in range(len(numbers) - i - 1):
            if numbers[j] > numbers[j + 1]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                swapped = True
                
        if not swapped:
            return numbers
            
    return numbers
            

def selection_sort(numbers: list):
    
    for i in range(len(numbers) - 1):
        m: int = i + 1
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[m]:
                m = j
                
        if numbers[i] > numbers[m]:
            numbers[i], numbers[m] = numbers[m], numbers[i]
            
            
    return numbers
    
    
    
def merge_sort(numbers: list[int]) -> list[int]:
    
    if len(numbers) == 1:
        return numbers
    
    m = int(len(numbers) / 2)
    l_sorted, r_sorted = merge_sort(numbers[:m]), merge_sort(numbers[m:])
    
    lp, rp = 0,0
    r = []
    while rp < len(r_sorted) and lp < len(l_sorted):
        if l_sorted[lp] <= r_sorted[rp]:
            r.append(l_sorted[lp])
            lp += 1
        else:
            r.append(r_sorted[rp])
            rp += 1
            

    while lp < len(l_sorted):
        r.append(l_sorted[lp])
        lp += 1
        
    while rp < len(r_sorted):
        r.append(r_sorted[rp])
        rp += 1
        
    return r
        
    
def linear_search(numbers: list[int], s: int) -> bool:
    for n in numbers:
        if n == s:
            return True
            
    return False
    
    
def binary_search(sorted_numbers: list[int], s: int) -> bool:
    
    if len(sorted_numbers) == 1 and sorted_numbers[0] != s:
        return False
        
    m = int(len(sorted_numbers) / 2)
    if sorted_numbers[m] == s:
        return True
        
    elif sorted_numbers[m] > s:
        return binary_search(sorted_numbers[:m], s)
        
    elif sorted_numbers[m] < s:
        return binary_search(sorted_numbers[m + 1:], s)
        
        
print(selection_sort([2,4,5,6,98,23,10,1]))
print(bubble_sort([2,4,5,6,98,23,10,1]))

print(linear_search([2,4,5,6,98,23,10,1], 2))
print(binary_search(bubble_sort([2,4,5,6,98,23,10,1]), 6))


print(merge_sort([2,4,5,6,98,23,10,1]))

                        
