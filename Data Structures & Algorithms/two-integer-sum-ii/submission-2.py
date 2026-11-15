class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numberSet = set(numbers)

        for number in numbers:
            if target - number in numberSet:
                return [list.index(int(number)), list.index(int(target - number))]