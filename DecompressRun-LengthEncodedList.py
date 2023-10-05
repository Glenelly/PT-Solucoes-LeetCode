from typing import List

class Solution1:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #criando um array vazio para guardar o resultado 
        resultado = []

        #Laço for para passar pelo array nums começando da posição 0 e pulando de 2 em 2 números 
        for i in range(0, len(nums), 2):
            #criando uma variavel freq para guardar os valores de nums na posição i
            freq = nums[i]
            #criando uma variavel val para guardar os valores de nums na posição i + 1
            val = nums[i + 1]
            #Criando variavel para armazenar os valores da variavel val dentro de um array e multiplicando pelo freq
            listaGerada = [val] * freq 
            #juntando os valores 
            resultado.extend(listaGerada)

        return resultado
    #Runtime: 64 ms  Memory: 16.8 MB Essa solução é mais rápida e ambas tem a mesma memória  

class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        #Restrições
        if len(nums) <= 2 and len(nums) <= 100:
            nums = nums
            
        if len(nums) % 2 == 0:
            rnums = nums
            
        for i in nums:
            if i > 100:
                nums = nums
                
        #Solução

        #criando um array vazio para guardar o resultado 
        resultado = []

        #Laço for para passar pelo array nums começando da posição 0 e pulando de 2 em 2 números 
        for i in range(0, len(nums), 2):
            #criando uma variavel freq para guardar os valores de nums na posição i
            freq = nums[i]
            #criando uma variavel val para guardar os valores de nums na posição i + 1
            val = nums[i + 1]
            #Criando variavel para armazenar os valores da variavel val dentro de um array e multiplicando pelo freq
            listaGerada = [val] * freq 
            #juntando os valores 
            resultado.extend(listaGerada)

        return resultado

    #Runtime: 67 ms  Memory: 16.8 MB Essa solução é mais lenta e mbas tem a mesma memória  