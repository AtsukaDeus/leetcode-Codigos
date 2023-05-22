class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        def sumarLista(lista: list[int]) -> int:
            suma = 0
            for i in range(len(lista)):
                suma += lista[i]
            return suma
        
        customerWealth = []
        for i in range(len(accounts)):
            customerWealth.append(sumarLista(accounts[i]))
        return max(customerWealth)


if __name__ == '__main__':
    solution = Solution()
    accounts = [[2,8,7],[7,1,3],[1,9,5]]
    print(solution.maximumWealth(accounts))