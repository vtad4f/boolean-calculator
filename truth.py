

import replace
import boolean


class Table(object):
    """
        BRIEF  Used to turn an expression into a truth table string
    """
    
    def __init__(self, expression, s_symbols):
        """
            BRIEF  Cache the expression and sentence symbols
        """        
        self.expression = expression
        self.s_symbols = s_symbols
        
        # TODO - Maybe we can statically initialize these
        globals()["T"] = boolean.boolean(boolean.boolean.TRUE)
        globals()["F"] = boolean.boolean(boolean.boolean.FALSE)
        
    def __str__(self):
        """
            BRIEF  Convert the expression and sentence symbols into a truth
                   table string
        """
        indent = '   '
        num_s = len(self.s_symbols)
        if num_s == 0:
            return indent + str(eval(self.expression))
            
        else:
            table = '{0}{1}|\n{0}{2}+-\n'.format(indent, ''.join(self.s_symbols), '-'*len(self.s_symbols))
            
            for i in range(2**num_s):
                bin_str = bin(i)[2:].zfill(num_s)
                table += "{0}{1}|{2}\n".format(indent, bin_str, self._EvalExpression(*map(int,bin_str)))
                
            return table
            
    def _EvalExpression(self, *values):
        """
            BRIEF  Evaluate the expression after making assignments
        """
        self._MakeAssignments(*values)
        return str(eval(self.expression))
        
    def _MakeAssignments(self, *values):
        """
            BRIEF  Assign variables in the global namespace
        """
        for i, s in enumerate(self.s_symbols):
            globals()[s] = boolean.boolean(values[i])
            
if __name__ == '__main__':
    """
        BRIEF  Main execution
    """
    
    