class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        trabalhadores = sorted([(w / q, q) for q, w in zip(quality, wage)])

        fila = []
        qualidade_total = 0
        custo_minimo = float('inf')

        for razao, qualidade in trabalhadores:
            heapq.heappush(fila, -qualidade)
            qualidade_total += qualidade

            if len(fila) > k:
                qualidade_total += heapq.heappop(fila)

            if len(fila) == k:
                custo = razao * qualidade_total
                custo_minimo = min(custo_minimo, custo)

        return custo_minimo
