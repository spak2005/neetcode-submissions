class Solution:

    def encode(self, strs: List[str]) -> str:
        store = ""
        for str in strs:
            store += f"{len(str)}*{str}"
        print(store)
        return store
        
            

    def decode(self, s: str) -> List[str]:
        res, i, j = [], 0, 0

        while i < len(s):
            j = s.index("*", i)

            dist = int(s[i:j])
            res.append(s[j+1:j+dist+1])

            i = j + dist + 1

        return res

        # "5*Hello5*World"

        
            