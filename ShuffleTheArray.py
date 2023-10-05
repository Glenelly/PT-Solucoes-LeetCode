from typing import List

class Solution1:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        #Restrições
        if n <= 1 or n <= 500:
            n = n
        
        for i in nums:
            if i > 1000:
                break
            else:
                nums = nums
                
        #Solução
        
        #Criando um array vazio que vai armazenar o valor do resultado
        arrayVazio = []

        #laço for para fazer o loop do número que está armazenado na variavel n 
        for i in range(n):
            #Guardando os valores de nums na posição i
            arrayVazio.append(nums[i])
            #Guardando os valores de nums na posição i + n
            arrayVazio.append(nums[i + n])

        return arrayVazio
    
    #Runtime: 56 ms  Memory: 16.4 MB Essa solução é mais rápida e a que ocupa mais memória  

class Solution2:
    def shuffle(self, nums: List[int], n: int) -> List[int]:

        #Criando um array vazio que vai armazenar o valor do resultado
        arrayVazio = []

        #laço for para fazer o loop do número que está armazenado na variavel n 
        for i in range(n):
            #Guardando os valores de nums na posição i
            arrayVazio.append(nums[i])
            #Guardando os valores de nums na posição i + n
            arrayVazio.append(nums[i + n])

        return arrayVazio
    
     #Runtime: 59 ms  Memory: 16.3 MB Essa solução é mais lenta e a que ocupa menos memória  