class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        merged = []
        while len(word1) > 0 and len(word2) > 0:
            # emulating .pop()
            merged.append(word1[0])
            word1 = word1[1:]
            merged.append(word2[0])
            word2 = word2[1:]
        if len(word1) > 0:
            merged.append(word1)
        elif len(word2) > 0:
            merged.append(word2)
        return ''.join(merged)