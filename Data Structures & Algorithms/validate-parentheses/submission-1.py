class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        mp ={")":"(", "}":"{", "]":"["}

        for ch in s:
            if ch in mp:
                if st  and st[-1] == mp[ch]:
                    st.pop()
                else:
                    return False
            else:
                st.append(ch)
        return len(st) == 0
