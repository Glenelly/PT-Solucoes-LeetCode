from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #atribuir o tamanho do "nums" a "n"
        n = len(nums)

        #Laço for para passar pelo indices de n 
        for i in range(n):                                                                      #O(n)
            #Segundo laço for para atribuir o indice de i + 1 
            for j in range(i + 1, n):                                                           #O(n)
                #verificar se (nums no indice i) + (nums no indice j) da o valor do target 
                if(nums[i] + nums[j] == target):
                    #Se a condição for verdadeira então imprime os indices i e j 
                    return[i, j]
        return[]
    #O(n^2)
    #Runtime: 2462ms Memory: 17 MB, ou seja, consome menos memoria mas é mais lento   
    
    
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #Dicionario vazio para armazenar os valores da lista nums que já foram vistos
        #junto com o indice 
        seen = {}

        #Laço for para pegar os valores e os indices atravez do enumerate
        for i, num in enumerate(nums):                                                         #O(n)
            #condição para saber se existe algum número no "nums" que somado com o num
            #resulta no valor esperado pelo target
            if target - num in seen:
                #retorna o indice dos dois números
                return ([seen[target - num], i])
            #Verifica se o valor do num não está na lista para que o número não se repita
            elif num not in seen:
                seen[num] = i
                
    #O(n)
    #Runtime: 57 ms Memory: 17.7 MB, ou seja, consome mais memoria mas é mais rápido que a primeira solução.
    
    
    