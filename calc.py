

import truth
import replace

HEADER = """
+------------------------------------------------------------------------------+
| 2-VALUE BOOLEAN CALCULATOR                                                   |
+------------------------------------------------------------------------------+
| Hello user, to begin simply type an expression. For example:                 |
|   1 --> 0                                                                    |
|   not X                                                                      |
|   A or B                                                                     |
| To see a list of operators, type 'help'                                      |
| When you are ready to quit, type 'exit'                                      |
+------------------------------------------------------------------------------+
"""

HELP = """
   Use any of the following operators with variables ABCDEGHIJKLMNOPQRSUWXYZ:
       "NOT", "~",
       "AND", "^", "*", "&", "&&",
       "NAND",
       "OR", "+", "v", "|", "||",
       "NOR",
       "IMPLIES", ">>", "->", "-->",
       "DOESNT IMPLY", "DOES NOT IMPLY", "-/->", "-/->", "--/->", "--/-->",
       "<-", "<--",
       "<-/-", "<-/--", "<--/--",
       "IFF", "IF AND ONLY IF", "IS EQUIVALENT TO", "XNOR", "=",
       "XOR", "!=", "<>"
       
   These values correspond to 'always true' and 'always false', respectively:
       "1", "T", "TRUE",
       "0", "F", "FALSE"
"""

if __name__ == '__main__':
    """
        BRIEF  Main execution
    """
    print(HEADER)
    while True:
        try:
            user_input = replace.Input()
            if user_input.exit:
                break
            elif user_input.help:
                print(HELP)
            else:
                print(truth.Table(*user_input.Preprocessing()))
        except (SyntaxError, NameError, TypeError) as e:
            print(e)
            
            