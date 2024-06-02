class Solution:
    def intToRoman(self, num: int) -> str:
        # Define the mapping between integer values and their corresponding Roman numeral symbols
        mapping = {
            1000: 'M', 900: 'CM', 500: 'D', 400: 'CD',
            100: 'C', 90: 'XC', 50: 'L', 40: 'XL',
            10: 'X', 9: 'IX', 5: 'V', 4: 'IV', 1: 'I'
        }
        
        # Initialize the result string
        result = ''
        
        # Iterate through the mapping
        for value, symbol in mapping.items():
            # Repeat subtraction until the given number becomes zero
            while num >= value:
                result += symbol
                num -= value
        
        return result


class Solution:
    def intToRoman(self, num: int) -> str:
        n = num
        result = ""

        while True:
            if 1000 <= n:
                result += "M"
                n -= 1000
            else:
                break
        while True:    
            if 900 <= n:
                result += "CM"
                n -= 900  
            else:
                break    
        while True:    
            if 500 <= n:
                result += "D"
                n -= 500  
            else:
                break
        while True:    
            if 400 <= n:
                result += "CD"
                n -= 400  
            else:
                break    
        while True:    
            if 100 <= n:
                result += "C"
                n -= 100  
            else:
                break
        while True:    
            if 90 <= n:
                result += "XC"
                n -= 90  
            else:
                break    
        while True:    
            if 50 <= n:
                result += "L"
                n -= 50  
            else:
                break
        while True:    
            if 40 <= n:
                result += "XL"
                n -= 40  
            else:
                break    
        while True:    
            if 10 <= n:
                result += "X"
                n -= 10  
            else:
                break
        while True:    
            if 9 <= n:
                result += "IX"
                n -= 9  
            else:
                break                
        while True:    
            if 5 <= n:
                result += "V"
                n -= 5  
            else:
                break
        while True:    
            if 4 <= n:
                result += "IV"
                n -= 4  
            else:
                break
        while True:    
            if 1 <= n:
                result += "I"
                n -= 1  
            else:
                break
        
        return result


#case 2
class Solution:
    def intToRoman(self, num: int) -> str:
        n = num
        result = ""

        while True:
            if 1000 <= n:
                result += "M"
                n -= 1000
                
            elif 900 <= n:
                result += "CM"
                n -= 900  
                
            elif 500 <= n:
                result += "D"
                n -= 500  
              
            elif 400 <= n:
                result += "CD"
                n -= 400  
                
            elif 100 <= n:
                result += "C"
                n -= 100  
                
            elif 90 <= n:
                result += "XC"
                n -= 90  
                
            
            elif 50 <= n:
                result += "L"
                n -= 50  
                
            elif 40 <= n:
                result += "XL"
                n -= 40  
              
            elif 10 <= n:
                result += "X"
                n -= 10  
                
            elif 9 <= n:
                result += "IX"
                n -= 9  
              
            elif 5 <= n:
                result += "V"
                n -= 5  
                
            elif 4 <= n:
                result += "IV"
                n -= 4  
                
            elif 1 <= n:
                result += "I"
                n -= 1  
            else:
                break
        
        return result
    

class Solution:
    def intToRoman(self, num: int) -> str:
        n = num
        result = ""

        while 1000 <= n:
            
            result += "M"
            n -= 1000
            
        while 900 <= n:    
            
            result += "CM"
            n -= 900  
                
        while 500 <= n:    
            
            result += "D"
            n -= 500  
            
        while 400 <= n:    
            
            result += "CD"
            n -= 400  
                
        while 100 <= n:    
            
            result += "C"
            n -= 100  
            
        while 90 <= n:    
            
            result += "XC"
            n -= 90  
               
        while 50 <= n:    
            
            result += "L"
            n -= 50  
            
        while 40 <= n:    
            
            result += "XL"
            n -= 40  
               
        while 10 <= n:    
            
            result += "X"
            n -= 10  
            
        while 9 <= n :    
            
            result += "IX"
            n -= 9  
                            
        while 5 <= n:    
            
            result += "V"
            n -= 5  
            
        while 4 <= n:    
            
            result += "IV"
            n -= 4  
            
        while  1 <= n:    
        
            result += "I"
            n -= 1  
            
        
        return result

