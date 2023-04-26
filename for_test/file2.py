def ppprint():
    print('aaa')
    
class AAA():
    def __init__(self):
        self.temp_number = 1.9
        
    def use_other(self, func):
        func()
    
    @property
    def get_numnber(self):
        self.temp_number += 1
        return self.temp_number
    
    
a = AAA()
a.use_other(ppprint)
