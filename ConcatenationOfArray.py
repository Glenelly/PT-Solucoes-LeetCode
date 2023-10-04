from typing import List

class Solution1:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums * 2
    
class Solution2:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        
        #atribui o tamanho do array nums
        n = len(nums)
        #cria um array vazio
        ans = []

        #Laço for para passar pelo tamanho do array nums 
        for i in range(n):
            #Atribui ao array ans os valores do array nums  
            ans.append(nums[i])
            #Junta os valores dos dois arrays 
            contatenando = nums + ans 
            
        return(contatenando)