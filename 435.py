from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key=lambda x: x[1])
           
        anterior_fim = float('-inf') 

        nao_sobrepostos = 0

        for inicio, fim in intervals:
            if inicio >= anterior_fim:
                nao_sobrepostos += 1
                anterior_fim = fim

        return len(intervals) - nao_sobrepostos