class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        ret = []

        rows = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        row_map = {}
        for i, row in enumerate(rows):
            for c in row:
                row_map[c] = i

        for word in words:
            word_lower = word.lower()
            t = row_map[word_lower[0]]
            ok = True
            for c in word_lower[1:]:
                if row_map[c] != t:
                    ok = False
                    break

            if ok:
                ret.append(word)

        return ret
