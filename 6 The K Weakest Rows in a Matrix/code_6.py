class Solution:
    def kWeakestRows(self, mat: list[list[int]], k: int) -> list[int]:
        def sumarLista(lista: list[int]) -> int:
            resultado = 0
            for i in range(len(lista)):
                resultado += lista[i]
            
            return resultado

        for i in range(len(mat)):
            mat[i] = [sumarLista(mat[i]), i]

        resultado = sorted(mat, key=lambda x: x[0])  
        resultado = [fila[1] for fila in resultado]  
        return resultado[:k] 
        
            
    
    
if __name__ == "__main__":
    
    solution  = Solution()
    k = 4
    mat = [
        [1,1,0,0,0],
        [1,1,1,0,0],
        [1,1,1,1,0]
    ]
    
    print(solution.kWeakestRows(mat,k))