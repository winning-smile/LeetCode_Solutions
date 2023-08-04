class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        array = strs.copy()
        maxelem = []

        for i in range(len(array)):
            tmp = 0
            elem = strs.pop()
            if not elem:
                return ""
            for j in range(len(strs)):
                result = [ord(a) ^ ord(b) for a, b in zip(elem, strs[j])]

                for val in result:
                    if val == 0:
                        tmp += 1
                    elif not tmp:
                        return ""
                    else:
                        break

                if tmp:
                    maxelem.append(tmp)

        maxelem.sort()

        if maxelem and not maxelem[0]:
            return ""

        elif maxelem:
            numchars = maxelem[0]
            index = array.index(array[maxelem.index(numchars)])
            answer = array[index][0:numchars]
            return answer
        
        else:
            return ""