class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:  # Verificar si la lista está vacía
            return ''

        prefix = ''
        for letra in zip(*strs):  # Usar zip para iterar por las letras de las palabras
            if len(set(letra)) == 1:  # Si todas las letras son iguales
                prefix += letra[0]
            else:
                break

        return prefix
            


sol = Solution()
# print(sol.longestCommonPrefix(["",""]))
a = {'': 1}
print(max(a.values()))



    
    

        
