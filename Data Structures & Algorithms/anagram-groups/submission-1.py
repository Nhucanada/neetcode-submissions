class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedOnes = {}
        sortedAna = []

        for s in strs:
            key = ''.join(sorted(s))

            if key in sortedOnes:
                sortedAna[sortedOnes[key]].append(s)
            else:
                sortedOnes[key] = len(sortedAna)
                sortedAna.append([s])

        return sortedAna