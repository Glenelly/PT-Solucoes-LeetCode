class Solution:
    def isPalindrome(self, x: int) -> bool:
        #Convertendo um int para uma string 
        x_str = str(x)

        #revertendo a string usando a técnica de fatiamento [::-1]
        reverse = x_str[::-1]

        #Verificando se o número armazenado no x é igual da direita pra esquerda
        #e da esquerda pra direita 
        if(reverse == x_str):
            return("true")
        else:
            print("false")