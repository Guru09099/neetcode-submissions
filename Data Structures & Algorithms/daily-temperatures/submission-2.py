class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        st = []

        for i, t in enumerate(temperatures):
            while st and t > st[-1][1]:
                stI, stT = st.pop()
                res[stI] = i - stI
            st.append((i, t))
        return res
        