

import truth
import replace


if __name__ == '__main__':
    """
        BRIEF  Main execution
    """
    while True:
        try:
            print(truth.Table(*replace.Input().Preprocessing()))
        except (SyntaxError, NameError, TypeError) as e:
            print(e)
            
            