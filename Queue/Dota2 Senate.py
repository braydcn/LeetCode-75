class Solution(object):
    def predictPartyVictory(self, senate):
        """
        :type senate: str
        :rtype: str
        """
        dires = deque()
        radiants = deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                radiants.append(i)
            if senate[i] == "D":
                dires.append(i)

        while radiants and dires:
            r = radiants.popleft()
            d = dires.popleft()

            if r < d:
                radiants.append(r + len(senate))
            else:
                dires.append(d + len(senate))
        return "Radiant" if radiants else "Dire"