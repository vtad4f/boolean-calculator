

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
        if len(self.s_symbols) > 2:
            raise ValueError("Too many sentence symbols at this point in the development!")
            
        if len(self.s_symbols) == 0:
            return '   ' + str(eval(self.expression))
            
        else:
            table = '   '
            for s in self.s_symbols:
                table += s
            table += '|\n   {0}+-\n'.format('-' * len(self.s_symbols))
            
            if len(self.s_symbols) == 1:
                table += "   0|" + self._EvalExpression(0) + '\n'
                table += "   1|" + self._EvalExpression(1) + '\n'
                
            elif len(self.s_symbols) == 2:
                table += "   00|" + self._EvalExpression(0, 0) + '\n'
                table += "   01|" + self._EvalExpression(0, 1) + '\n'
                table += "   10|" + self._EvalExpression(1, 0) + '\n'
                table += "   11|" + self._EvalExpression(1, 1) + '\n'
                
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
    
    