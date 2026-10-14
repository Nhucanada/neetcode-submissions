class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numberSet = set(numbers)

        for number in numbers:
            if target - number in numberSet:
                if target - number == number:
                    return [numbers.index(number) + 1, numbers.index(target - number) + 2]
                return [numbers.index(number) + 1, numbers.index(target - number) + 1]