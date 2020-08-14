

class Bool(object):
    """
        BRIEF  This is an abuse of the normal functionality of these operators
               in python. We are re-using them because python does not allow
               us to define custom operators.
               
               I could have built these operators up from 
    """
    TRUE  = 1
    FALSE = 0
    
    def __init__(self, value):
        """
            BRIEF  Notice that the implementation does not require particular
                   values for 1 and 0; just that they are distinct
        """
        self.value = value # Bool.TRUE or Bool.FALSE
        
    def __str__(self):
        """
            BRIEF  Just print the TRUE/FALSE value
        """
        return str(self.value)
        
    def __invert__(self)
        """
            BRIEF  '~ A' This will represent 'not A'
        """
        return Bool(Bool.FALSE) if self.value else Bool(Bool.TRUE)
        
    def __add__(self, other):
        """
            BRIEF  'A + B' This will represent 'A or B'
        """
        return Bool(Bool.FALSE) if (self.value is Bool.FALSE and other.value is Bool.FALSE) else Bool(Bool.TRUE)
        
    def __sub__(self, other):
        """
            BRIEF  'A - B' This will represent 'A nor B'
        """
        return Bool(Bool.TRUE) if (self.value is Bool.FALSE and other.value is Bool.FALSE) else Bool(Bool.FALSE)
        
    def __mul__(self, other):
        """
            BRIEF  'A * B' will represent 'A and B'
        """
        return Bool(Bool.TRUE) if (self.value is Bool.TRUE and other.value is Bool.TRUE) else Bool(Bool.FALSE)
        
    def __matmul__(self, other):
        """
            BRIEF  'A @ B' will represent 'A nand B'
        """
        return Bool(Bool.TRUE) if (self.value is Bool.TRUE and other.value is Bool.TRUE) else Bool(Bool.FALSE)
        
    def __rshift__(self, other):
        """
            BRIEF  'A >> B' will represent 'A implies B'
        """
        return Bool(Bool.FALSE) if (self.value is Bool.TRUE and other.value is Bool.FALSE) else Bool(Bool.TRUE)
        
    def __truediv__(self, other):
        """
            BRIEF  'A / B' will represent 'A does not imply B'
        """
        return Bool(Bool.TRUE) if (self.value is Bool.TRUE and other.value is Bool.FALSE) else Bool(Bool.FALSE)
        
    def __lshift__(self, other):
        """
            BRIEF  'A << B' will represent 'B implies A'
        """
        return Bool(Bool.FALSE) if (self.value is Bool.FALSE and other.value is Bool.TRUE) else Bool(Bool.TRUE)
        
    def __floordiv__(self, other):
        """
            BRIEF  'A // B' will represent 'B does not imply A'
        """
        return Bool(Bool.TRUE) if (self.value is Bool.FALSE and other.value is Bool.TRUE) else Bool(Bool.FALSE)
        
    def __mod__(self, other):
        """
            BRIEF  'A % B' will represent 'A iff B'
        """
        return Bool(Bool.TRUE) if (self.value is other.value) else Bool(Bool.FALSE)
        
    def __xor__(self, other):
        """
            BRIEF  'A ^ B' will represent 'A xor B'
        """
        return Bool(Bool.FALSE) if (self.value is other.value) else Bool(Bool.TRUE)
        
        
def __init__ == '__main__':
    """
        BRIEF  Main execution
    """
    
    