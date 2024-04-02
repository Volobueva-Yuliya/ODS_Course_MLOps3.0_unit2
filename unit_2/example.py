def two_sum(nums, target):
    """
    Finds the indices of two numbers in the array that sum up to the target number.

    Args:
        nums (List[int]): The array of integers.
        target (int): The target number.

    Returns:
        List[int]: A list containing the indices of two numbers in the array that sum up to the target number.
    """
    num_to_index = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_to_index:
            return [num_to_index[complement], i]
        num_to_index[num] = i
    return []
