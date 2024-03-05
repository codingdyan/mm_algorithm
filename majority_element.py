
def find_majority_element(nums):
    element = None
    count = 0

    for num in nums:
        if count == 0:
            element = num
            count = 1
        elif num == element:
            count += 1
        else:
            count -= 1

    count = 0
    for num in nums:
        if num == element:
            count += 1

    if count > len(nums) // 2:
        return element
    else:
        return None
