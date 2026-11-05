class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(len(position)):
            cars.append([position[i], speed[i]])

        cars.sort(reverse=True)

        for j in range(len(cars)):
            time = (target - cars[j][0]) / cars[j][1]

            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)

        return len(stack)