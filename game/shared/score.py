from os import stat

from urllib3 import Retry


class Score:
    """A color.

    The responsibility of Score is to hold and provide information about itself. 

    Attributes:
        _red (int): The red value. 
    """
    
    def __init__(self):
        """Constructs a new Score using the specified values. 
        
        Args:
            red (int): A red value.
            .
        """
        self.score = 0

     
    def get_score(self):
        

        return self._score   
    
    def set_score(self, score):
        

        self._score = score
  

