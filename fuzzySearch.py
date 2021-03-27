# Creates Vladislav Bachmackiy (A-ST-RA)

class FuzzySearch:
    """FuzzySearch class by A-ST-RA"""

    # Inaccuracy parameters
    def __init__(self, inaccuracy):
        """Constructor"""
        self.inaccuracy = inaccuracy

    def search(self, values, search_param):
        """Search func"""
        if (len(values) <= 1):
            return "array length <= 1"
        counter = 0

        for value in values:
            counter = 0
            void_char_amount = len(value) - len(search_param)

            if (void_char_amount <= self.inaccuracy) and (void_char_amount >= 0):
                for i in range(len(search_param) - void_char_amount):
                    if (value[i].lower != search_param[i].lower):
                        counter += 1
                counter += void_char_amount
                if(counter <= self.inaccuracy):
                    return value
        

            elif (void_char_amount <= (self.inaccuracy * (-1)) and void_char_amount < 0):
                for i in range(len(value)):
                    if (value[i].lower != search_param[i].lower):
                        counter += 1
                counter += (void_char_amount * (-1))
                if(counter <= self.inaccuracy):
                    return value
        
        return "no matches found"
            
