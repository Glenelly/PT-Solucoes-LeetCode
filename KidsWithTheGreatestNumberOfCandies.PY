from typing import List

class Solution1:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        #Constraints
        
        n = len(candies)
                
        if(n <= 2 and n <=100):
            n = n
                    
        for i in candies:
            if i > 100:
                return(i)
                break
        
        if extraCandies > 50:
            return(extraCandies)
            
        #solution
        
        #criando um array vazio para guardar o resultado
        resultado = []
        #variavel para armazenar o valor máximo do array candies
        ValorMax = max(candies)

        #laço for para passar pelos indices no tamanho do array candies
        for i in range(n):
            #verificando se o valor armazenado no array candies da posição i mais o valor de extraCandies
            #é maior que o maior valor armazenado no array candies 
            if candies[i] + extraCandies >= ValorMax:
                resultado.append(True)
            else: 
                resultado.append(False)
                
        return resultado
    
    #Runtime: 49 ms  Memory: 16.1 MB Essa solução é mais rápida e que ocupa menos memória 

        
class Solution2:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        n = len(candies)

         #criando um array vazio para guardar o resultado
        resultado = []
        #variavel para armazenar o valor máximo do array candies
        ValorMax = max(candies)

        #laço for para passar pelos indices no tamanho do array candies
        for i in range(n):
            #verificando se o valor armazenado no array candies da posição i mais o valor de extraCandies
            #é maior que o maior valor armazenado no array candies 
            if candies[i] + extraCandies >= ValorMax:
                resultado.append(True)
            else: 
                resultado.append(False)
                
        return resultado
    
    #Runtime: 56 ms  Memory: 16.2 MB Essa solução é mais lenta e ocupa mais memória   