class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        fila = []
        valor_maximo = float('-inf')

        for indice_lista, lista in enumerate(nums):
            heapq.heappush(fila, (lista[0], indice_lista, 0))
            valor_maximo = max(valor_maximo, lista[0])

        melhor_inicio, melhor_fim = float('-inf'), float('inf')

        while fila:
            valor_minimo, indice_lista, indice_elemento = heapq.heappop(fila)

            if valor_maximo - valor_minimo < melhor_fim - melhor_inicio:
                melhor_inicio, melhor_fim = valor_minimo, valor_maximo

            if indice_elemento + 1 < len(nums[indice_lista]):
                proximo_valor = nums[indice_lista][indice_elemento + 1]
                heapq.heappush(fila, (proximo_valor, indice_lista, indice_elemento + 1))
                valor_maximo = max(valor_maximo, proximo_valor)
            else:
                break

        return [melhor_inicio, melhor_fim]