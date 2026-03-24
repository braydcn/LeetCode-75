class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        # index = position in space
        # Negative/Positive = Left/Right
        # Value = Size
    
        result = []
        for i in range(len(asteroids)):
            destroyed = False
            while len(result) > 0 and asteroids[i] < 0 and result[-1] >= 0:
                if abs(asteroids[i]) > abs(result[-1]):
                    result.pop()
                elif abs(asteroids[i]) == abs(result[-1]):
                    result.pop()
                    destroyed = True
                    break
                else:
                    destroyed = True
                    break
            if not destroyed:
                result.append(asteroids[i])
        return result