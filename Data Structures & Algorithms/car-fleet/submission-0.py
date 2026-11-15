class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        stack = []

        for i in range(position):
            cars.append([position[i], speed[i]])
        cars.sort(reverse=True)

        for j in range(cars):
            time = (target - cars[i][0]) / cars[i][1]
            if not stack:
                stack.append(time)
            elif time > stack[-1]:
                stack.append(time)
        
        return len(stack)
            