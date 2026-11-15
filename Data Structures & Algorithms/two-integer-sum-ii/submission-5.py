class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numberSet = set(numbers)

        for number in numbers:
            if target - number in numberSet:
                return [numbers.index(number) + 1, numbers.index(target - number) + 1]