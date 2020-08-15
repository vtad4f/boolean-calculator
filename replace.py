

import boolean


class Forbidden:
    SYMBOLS = [
        ("*", "'~', '!', 'not'"), # Now allowed since it's on the wrong side
        ("'", "'~', '!', 'not'"), # Now allowed since it's on the wrong side
        ("`", "'~', '!', 'not'")  # Now allowed since it's on the wrong side
    ]


class Input(object):
    """
        BIREF  Make replacements so that the logical symbols we are used to
               reading can be evaluated by python.
               
               '~ A'     will represent 'not A'
               'A + B'   will represent 'A or B'
               'A - B'   will represent 'A nor B'
               'A * B'   will represent 'A and B'
               'A @ B'   will represent 'A nand B'
               'A >> B'  will represent 'A implies B'
               'A / B'   will represent 'A does not imply B'
               'A << B'  will represent 'B implies A'
               'A // B'  will represent 'B does not imply A'
               'A % B'   will represent 'A iff B'
               'A ^ B'   will represent 'A xor B'
    """
    
    # TODO - Add the Unicode chars that Notepad++ didn't recognize
    SYMBOLS = [
        ("!="     , "^" ),
        ("<>"     , "^" ),
        ("¬"      , "~" ),
        ("!"      , "~" ),
        ("∧"      , "*" ),
        ("^"      , "*" ),
        ("&"      , "*" ),
        ("&&"     , "*" ),
        ("∨"      , "+" ),
        ("V"      , "+" ),
        ("|"      , "+" ),
        ("||"     , "+" ),
        ("⇒"      , ">>"),
        ("→"      , ">>"),
        ("->"     , ">>"),
        ("-->"    , ">>"),
        ("-/->"   , "/" ),
        ("--/->"  , "/" ),
        ("--/-->" , "/" ),
        ("←"      , "<<"),
        ("<-"     , "<<"),
        ("<--"    , "<<"),
        ("<-/-"   , "//"),
        ("<-/--"  , "//"),
        ("<--/--" , "//"),
        ("⇔"      , "%" ),
        ("↔"      , "%" ),
        ("="      , "%" ),
        ("≡"      , "%" )
    ]
    
    TEXT = [
        ("NOT"             , "~" ),
        ("AND"             , "*" ),
        ("NAND"            , "@" ),
        ("OR"              , "+" ),
        ("NOR"             , "-" ),
        ("IMPLIES"         , ">>"),
        ("DOESNT IMPLY"    , "/" ),
        ("DOES NOT IMPLY"  , "/" ),
        ("IFF"             , "%" ),
        ("IF AND ONLY IF"  , "%" ),
        ("IS EQUIVALENT TO", "%" ),
        ("XNOR"            , "%" ),
        ("XOR"             , "^" )
    ]
    
    TRUE_FALSE = [
        (str(boolean.boolean.TRUE) , "T"),
        (str(boolean.boolean.FALSE), "F"),
        ("TRUE" , "T"),
        ("FALSE", "F"),
    ]
    
    ALPHA = set(list("ABCDEGHIJKLMNOPQRSUWXYZ"))
    
    
    def __init__(self):
        """
            BRIEF  Cache the uppercase user input
        """
        self.content = input().strip().upper()
        
        self.exit = ('EXIT' in self.content)
        self.help = ('HELP' in self.content)
        
    def Preprocessing(self):
        """
            BRIEF  Perform string replacements
        """
        for symbol, alternative in Forbidden.SYMBOLS:
            if symbol in self.content:
                raise SyntaxError("{0} isn't allowed! Use {1} instead.".format(symbol, alternative))
                
        self._Replace(Input.SYMBOLS)
        self._Replace(Input.TEXT)
        self._Replace(Input.TRUE_FALSE)
        
        s_symbols = []
        for a in self.content:
            if (a in Input.ALPHA) and not (a in s_symbols):
                s_symbols.append(a)
                
        return self.content, s_symbols
        
    def _Replace(self, replacements):
        """
            BRIEF  Replace all the instances of before with after in contents
        """
        for before, after in reversed(replacements):
            self.content = self.content.replace(before, after)
            
            
if __name__ == '__main__':
    """
        BRIEF  Main execution
    """
    
    