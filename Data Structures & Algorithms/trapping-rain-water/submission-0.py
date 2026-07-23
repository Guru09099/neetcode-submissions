class Solution:
    def trap(self, height: List[int]) -> int:
        st = []
        res = 0

        for i in range(len(height)):
            while st and height[i] >= height[st[-1]]:
                mid = height[st.pop()]
                if st:
                    right = height[i]
                    left = height[st[-1]]
                    h = min(left, right) - mid
                    w = i - st[-1] - 1
                    res += h * w
            st.append(i)
        return res