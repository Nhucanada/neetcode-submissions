class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances = []
        closest_dists = []
        for point in points:
            distance = math.sqrt((point[0] - 0)**2 + (point[1] - 0)**2)
            dp = [distance, point[0], point[1]]
            distances.append(dp)
        
        heapq.heapify(distances)
        for i in range(k):
            topDistance = heapq.heappop(distances)
            closest_dists.append([topDistance[1], topDistance[2]])

        return closest_dists