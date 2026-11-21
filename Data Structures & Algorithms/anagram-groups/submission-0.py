class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        store = {}
        anagrams = []
        for str in strs:
            sorted_str = "".join(sorted(str))
            if sorted_str in store:
                store[sorted_str].append(str)
            else:
                store[sorted_str] = [str]

        for anagram in store:
            anagrams.append(store[anagram])

        return anagrams

                