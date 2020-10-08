# ----------------------------------------------------------------------

# Card                | Prefix                                 | Length

# ----------------------------------------------------------------------

# American Express    | 34, 37                                 | 15

# Diners Club         | 36, 38                                 | 14, 15

# Visa                | 4                                      | 16

# Visa Electron       | 4026, 417500, 4508, 4844, 4913, 4917   | 16

# Discover Card       | 6011, 622126-622925, 644-649, 65       | 16

# China Union Pay     | 622926-622930, 624-626, 6282-6288      | 16-19

def get_issuer(card_number):

    """takes a credit card number returns the name of issuer """

    # build dict

    issuer_dict = {'American Express': [34, 37], 'Diners Club': [36, 38], 'Visa': [4], 
    'Visa Electron': [4026, 417500, 4508, 4844, 4913, 4917], 'Discover Card': list(range(622126, 622925+1)) + list(range(644, 649+1)) + [6011, 65],
    'China Union Pay': list(range(622926, 622930+1)) + list(range(624, 626+1)) + list(range(6282, 6288+1))}

    # if statemments based on length and then lookup using dictionary
    # if 15 length: only need to look at American Express and Diner's Club values

    if len(card_number) == 15:
        if int(card_number[0:2]) in issuer_dict['American Express']:
            return 'American Express'

        elif int(card_number[0:2]) in issuer_dict['Diners Club']:
            return 'Diners Club'
    elif len(card_number) == 14:
        for prefix in issuer_dict['Diners Club']:
            if card_number.startswith(str(prefix)):
                return 'Diners Club'    
    elif len(card_number) > 16:
        for prefix in issuer_dict['China Union Pay']:
            if card_number.startswith(str(prefix)):
                return 'China Union Pay'
    elif len(card_number) == 16:
        if card_number.startswith('4'):
            for prefix in issuer_dict['Visa Electron']:
                if card_number.startswith(str(prefix)):
                    return 'Visa Electron'
            else:
                return 'Visa'
        
        if card_number.startswith('6'):
            for prefix in issuer_dict['Discover Card']:
                if card_number.startswith(str(prefix)):
                    return 'Discover Card'
                else:
                    for prefix in issuer_dict['China Union Pay']:
                        if card_number.startswith(str(prefix)):
                            return 'China Union Pay'
    
    return 'Unknown'
            

assert get_issuer('341235468923456') == 'American Express'
assert get_issuer('36123546892345') == 'Diners Club'
assert get_issuer('4175002354689234') == 'Visa Electron'
assert get_issuer('4231123546892344') == 'Visa'
assert get_issuer('6229202354689234') == 'Discover Card'
assert get_issuer('626920235468923455') == 'China Union Pay'
assert get_issuer('123112354689234') == 'Unknown'


