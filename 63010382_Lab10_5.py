def minimum_weight(order_list, total):  # recursion
    if total == 1:
        return sum(num)
    min_weight = 10000000000000000000000000
    for index in range(len(order_list)):
        if len(order_list[index:]) < total - 1:
            break
        this_box    =   sum(order_list[:index])
        other_box   =   minimum_weight(order_list[index:], total - 1)
        min_weight  =   min(max(this_box, other_box), min_weight)
    return min_weight

def min_box(lst, number_of_boxes):
    left = max(lst)
    right = sum(lst)
    while left <= right:
        total_size = (left+right)//2
        total_count = 0
        i = 0
        while i < len(lst):
            weight = 0
            while i < len(lst) and weight + lst[i] <= total_size:
                weight += lst[i]
                i += 1
            total_count += 1

        if total_count <= number_of_boxes:
            right = total_size - 1
        elif total_count > number_of_boxes:
            left = total_size + 1

    return left



lst, total = input("Enter Input : ").split('/')
total = int(total)
lst = list(map(int, lst.split()))
print(f"Minimum weigth for {total} box(es) = {min_box(lst, total)}")