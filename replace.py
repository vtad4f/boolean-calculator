
import bool


class Forbidden:
    SYMBOLS = [
        ("*", "~"), # Now allowed since it's on the wrong side
        ("'", "~")  # Now allowed since it's on the wrong side
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
        ("¬"      , "~" ),
        ("∧"      , "*" ),
        ("^"      , "*" ),
        ("∨"      , "+" ),
        ("V"      , "+" ),
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
        ("NOT"              , "~" ),
        ("AND"              , "*" ),
        ("NAND"             , "@" ),
        ("OR"               , "+" ),
        ("NOR"              , "-" ),
        ("IMPLIES"          , ">>"),
        ("DOESN'T IMPLY"    , "/" ),
        ("DOES NOT IMPLY"   , "/" ),
        ("IFF"              , "%" ),
        ("IF AND ONLY IF"   , "%" ),
        ("IS EQUIVALENT TO" , "%" ),
        ("XNOR"             , "%" ),
        ("XOR"              , "^" )
    ]
    
    TRUE_INSTANCE = "bool.Bool(1)"
    FALSE_INSTANCE = "bool.Bool(0)"
    
    TRUE_FALSE = [
        ("1"    , TRUE_INSTANCE ),
        ("0"    , FALSE_INSTANCE),
        ("T"    , TRUE_INSTANCE ),
        ("F"    , FALSE_INSTANCE),
        ("TRUE" , TRUE_INSTANCE ),
        ("FALSE", FALSE_INSTANCE),
    ]
    
    def __init__(self):
        """
            BRIEF  
        """
        self.content = input()
        
    def Preprocessing(self):
        """
            BRIEF  
        """
        for symbol, alternative in Forbidden.SYMBOLS:
            if symbol in self.content:
                raise Exception("{0} isn't allowed! Use {1} instead.".format(symbol, alternative))
                
        for replacements in [Input.SYMBOLS, Input.TEXT, Input.TRUE_FALSE]:
            for before, after in reversed(replacements):
                self.content = self.content.replace(before, after)
                
        return self.content
        
        