import random
class Solution:
    
    LESS_USED_LETTERS = ['Z','X','K','Q','J']
    def best_character(self,password,index):
        # you can also do as it's the less frequenlty used letter in english  : 
        # filler = 'Z'
        filler = random.choice(self.LESS_USED_LETTERS)
        if not any(p.islower() for p in password):
            filler = filler.lower()
        elif not any(p.isdigit() for p in password):
            filler = str(random.randint(0,9))
        if password[index] == filler:
            filler = chr(ord(filler) - 1)
        return filler

    def update_character(self,password,index):
        filler = self.best_character(password, index)
        temp = list(password)
        temp[index] = filler
        return ''.join(temp)



    def add_character(self,password,index):
        filler = self.best_character(password, index)
        return password[:index] + filler + password[index:] 


    def has_uplowdig(self,password :str) -> bool:
        up = any(p.isupper() for p in password)
        low = any(p.islower() for p in password)
        dig = any(p.isdigit() for p in password)
        if up and low and dig :
           return True
        return False
    def find_index(self,password : str) -> int:
        # we will break the password into chunks so we can see if there's some repition going on
        chunks : str = []
        p_chunk : int = 0
        for i in range(1,len(password)):
           if password[i-1] != password[i]:
               chunks.append(password[p_chunk:i])
               p_chunk=i
        chunks.append(password[p_chunk:len(password)])
      
        max_length = max(len(chunk) for chunk in chunks)
        if max_length < 3 :
            return -1
        # we want to found the chunk that length%3 == 0 
        # else we gonna track the if there is 1 or 2 remain
        mod1,mod2 = -1,-1
        index = 0

        for chunk in chunks:
            length = len(chunk)
            
            if length < 3 :
                index += length
                continue
            if length % 3 == 0 :
                return index
            if length % 3 == 1 and mod1 == -1:
                mod1 = index
            if length % 3 == 2 and mod2 == -1:
                mod2 = index
            index += length
        
        if mod1 > -1:
            return mod1
        if mod2 > -1:
            return mod2
        return 0
            
    def is_password_strong(self,password:str) -> bool :

        # First thing we need to check if the string contain at least 6 and max 20
        if len(password) < 6 or len(password) > 20 :
            return False
        # Let's find the index now 
        if self.find_index(password) > -1 :
            return False      

        # and lastly let's check check if it has upper,lower and digit
        if self.has_uplowdig(password):
            return True

        return False
    def find_safe_index(self,password) -> int:
        for i in range(len(password)):
            p = password[i]
            truncated_password = password[:i] + password[i+1:]  
            if p.isupper() and any(p.isupper() for p in truncated_password): 
                return i
            if p.islower() and any(p.islower() for p in truncated_password):
                return i
            if p.isdigit() and any(p.isdigit() for p in truncated_password):
                return i
        return 0        


    def strongPasswordChecker(self, password: str) -> int: 
       steps  = 0
       print(len(password))
       while(True):
           repeat_index = self.find_index(password)
         
           if len(password) < 6 :
               index = 0
               if repeat_index > - 1:
                   index = repeat_index+2
               password = self.add_character(password,index)
           elif len(password)>20 :
                
                index = self.find_safe_index(password)
                if repeat_index > -1:
                    index = repeat_index+2
                password = password[:index] + password[index + 1:]
           else:
               
                if self.is_password_strong(password):
                    # exit loop
                    break
                index = self.find_safe_index(password)
                if repeat_index > -1:
                    index = repeat_index+2
                password = self.update_character(password,index)
           steps += 1
          

           if steps> 100:
                # too much exiting the loop
                break
           if self.is_password_strong(password):
                # exit loop
                break


       return steps
