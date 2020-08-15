

class boolean(object):
    """
        BRIEF  This is an abuse of the normal functionality of these operators
               in python. We are re-using them because python does not allow
               us to define custom operators.
               
               It is important for or and nor to be represented by + and - for
               the sake or order of operation.
    """
    TRUE  = 1
    FALSE = 0
    
    def __init__(self, value):
        """
            BRIEF  Notice that the implementation does not require particular
                   values for 1 and 0; just that they are distinct
        """
        self.value = value # boolean.TRUE or boolean.FALSE
        
    def __str__(self):
        """
            BRIEF  Just print the TRUE/FALSE value
        """
        return str(self.value)
        
    def __invert__(self):
        """
            BRIEF  '~ A' will represent 'not A'
        """
        return boolean(boolean.FALSE) if self.value else boolean(boolean.TRUE)
        
    def __mul__(self, other):
        """
            BRIEF  'A * B' will represent 'A and B'
        """
        return boolean(boolean.TRUE) if (self.value is boolean.TRUE and other.value is boolean.TRUE) else boolean(boolean.FALSE)
        
    def __matmul__(self, other):
        """
            BRIEF  'A @ B' will represent 'A nand B'
        """
        return boolean(boolean.TRUE) if (self.value is boolean.TRUE and other.value is boolean.TRUE) else boolean(boolean.FALSE)
        
    def __add__(self, other):
        """
            BRIEF  'A + B' will represent 'A or B'
        """
        return boolean(boolean.FALSE) if (self.value is boolean.FALSE and other.value is boolean.FALSE) else boolean(boolean.TRUE)
        
    def __sub__(self, other):
        """
            BRIEF  'A - B' will represent 'A nor B'
        """
        return boolean(boolean.TRUE) if (self.value is boolean.FALSE and other.value is boolean.FALSE) else boolean(boolean.FALSE)
        
    def __rshift__(self, other):
        """
            BRIEF  'A >> B' will represent 'A implies B'
        """
        return boolean(boolean.FALSE) if (self.value is boolean.TRUE and other.value is boolean.FALSE) else boolean(boolean.TRUE)
        
    def __truediv__(self, other):
        """
            BRIEF  'A / B' will represent 'A does not imply B'
        """
        return boolean(boolean.TRUE) if (self.value is boolean.TRUE and other.value is boolean.FALSE) else boolean(boolean.FALSE)
        
    def __lshift__(self, other):
        """
            BRIEF  'A << B' will represent 'B implies A'
        """
        return boolean(boolean.FALSE) if (self.value is boolean.FALSE and other.value is boolean.TRUE) else boolean(boolean.TRUE)
        
    def __floordiv__(self, other):
        """
            BRIEF  'A // B' will represent 'B does not imply A'
        """
        return boolean(boolean.TRUE) if (self.value is boolean.FALSE and other.value is boolean.TRUE) else boolean(boolean.FALSE)
        
    def __mod__(self, other):
        """
            BRIEF  'A % B' will represent 'A iff B'
        """
        return boolean(boolean.TRUE) if (self.value is other.value) else boolean(boolean.FALSE)
        
    def __xor__(self, other):
        """
            BRIEF  'A ^ B' will represent 'A xor B'
        """
        return boolean(boolean.FALSE) if (self.value is other.value) else boolean(boolean.TRUE)
        
        
if __name__ == '__main__':
    """
        BRIEF  Main execution
    """
    
    