def name_of_digit(n):
    
    if n == 0:
        return 'zero'
    elif n == 1:
        return 'one'
    elif n == 2:
        return 'two'
    elif n == 3:
        return 'three'
    elif n == 4:
        return 'four'
    elif n == 5:
        return 'five'
    elif n == 6:
        return 'six'
    elif n == 7:
        return 'seven'
    elif n == 8:
        return 'eight'
    elif n == 9:
        return 'nine'

def name_of_tens(n):
    
    if n == 1:
        return 'ten'
    elif n == 2:
        return 'twenty'
    elif n == 3:
        return 'thirty'
    elif n == 4:
        return 'forty'
    elif n == 5:
        return 'fifty'
    elif n == 6:
        return 'sixty'
    elif n == 7:
        return 'seventy'
    elif n == 8:
        return 'eighty'
    elif n == 9:
        return 'ninety'
    
def name_of_teens(n):
    
    if n == 10:
        return 'ten'
    elif n == 11:
        return 'eleven'
    elif n == 12:
        return 'twelve'
    elif n == 13:
        return 'thirteen'
    elif n == 14:
        return 'fourteen'
    elif n == 15:
        return 'fifteen'
    elif n == 16:
        return 'sixteen'
    elif n == 17:
        return 'seventeen'
    elif n == 18:
        return 'eighteen'
    elif n == 19:
        return 'nineteen'

def name_of_two_digits(n):
    integer_name = ''
    tens = int(n / 10)
    ones = n % 10

    if ones == 0:
        integer_name = integer_name + name_of_tens(tens)
    elif n in range (11, 20):
        integer_name = integer_name + name_of_teens(n)
    else:
        integer_name = integer_name + name_of_tens(tens) + ' ' + name_of_digit(ones)

    return integer_name

def name_of_three_digits(n):
    integer_name = ''
    hundreds = int(n / 100)
    tens = int(n / 10) % 10
    ones = n % 10
    two_digit = tens * 10 + ones

    if two_digit in range (10, 100):
        integer_name = integer_name + name_of_digit(hundreds) + ' hundred ' + name_of_two_digits(two_digit)
    elif two_digit in range (1,10):
        integer_name = integer_name + name_of_digit(hundreds) + ' hundred ' + name_of_digit(two_digit)
    elif two_digit == 0:
        integer_name = integer_name + name_of_digit(hundreds) + ' hundred'

    return integer_name

def name_of_integer(n):
    ones = n % 1000
    thousands = int(n / 1000) % 1000
    millions = int(n / 1000000)

    if n == 0:
        integer_name = 'zero'
    
    if millions != 0:
        if millions in range (100, 1000):
            integer_name = (name_of_three_digits(millions) + ' million')
        elif millions in range (10, 100):
            integer_name = (name_of_two_digits(millions) + ' million')
        elif millions in range (1, 10):
            integer_name = (name_of_digit(millions) + ' million')

        if thousands in range (100, 1000):
            integer_name = integer_name + ' ' + (name_of_three_digits(thousands) + ' thousand')
        elif thousands in range (10, 100):
            integer_name = integer_name + ' ' + (name_of_two_digits(thousands) + ' thousand')
        elif thousands in range (1, 10):
            integer_name = integer_name + ' ' + (name_of_digit(thousands) + ' thousand')

        if ones in range (100, 1000):
            integer_name = integer_name + ' ' + (name_of_three_digits(ones))
        elif ones in range (10, 100):
            integer_name = integer_name + ' ' + (name_of_two_digits(ones))
        elif ones in range (1, 10):
            integer_name = integer_name + ' ' + (name_of_digit(ones))
            
    else:
        if thousands != 0:
            if thousands in range (100, 1000):
                integer_name = name_of_three_digits(thousands) + ' thousand'
            elif thousands in range (10, 100):
                integer_name = name_of_two_digits(thousands) + ' thousand'
            elif thousands in range (1, 10):
                integer_name = name_of_digit(thousands) + ' thousand'

            if ones in range (100, 1000):
                integer_name = integer_name + ' ' + (name_of_three_digits(ones))
            elif ones in range (10, 100):
                integer_name = integer_name + ' ' + (name_of_two_digits(ones))
            elif ones in range (1, 10):
                integer_name = integer_name + ' ' + (name_of_digit(ones))

        else:
            if ones in range (100, 1000):
                integer_name = name_of_three_digits(ones)
            elif ones in range (10, 100):
                integer_name = name_of_two_digits(ones)
            elif ones in range (1, 10):
                integer_name = name_of_digit(ones)

    return integer_name


def name_of_fraction(fraction):
    denominator = int(fraction[1])
    nominator = int(fraction[0])
    fraction_name = ''

    if nominator == 0:
        return 'zero'     
    elif nominator >= 100:
        fraction_name = name_of_integer(nominator) + ' thousandths'
    elif nominator in range (10, 100):
        if denominator == 1000:
            fraction_name = name_of_integer(nominator) + ' thousandths'
        elif denominator == 100:
            fraction_name = name_of_integer(nominator) + ' hundredths'
    elif nominator in range (2, 10):
        fraction_name += (name_of_digit(nominator))
        if denominator == 1000:
            fraction_name = name_of_integer(nominator) + ' thousandths'
        elif denominator == 100:
            fraction_name = name_of_integer(nominator) + ' hundredths'
        elif denominator == 10:
            fraction_name = name_of_integer(nominator) + ' tenths'
    elif nominator == 1:
        if denominator == 1000:
            fraction_name = fraction_name + 'one one thousandth'
        elif denominator == 100:
            fraction_name += fraction_name + 'one one hundredth'
        elif denominator == 10:
            fraction_name += fraction_name + 'one tenth'
            
    return fraction_name

def name_of_decimal(n, fraction):
    decimal_name = ''
    if n != 0:
        if name_of_fraction(fraction) == 'zero':
            decimal_name = name_of_integer(n)
        else:
            decimal_name = name_of_integer(n) + ' and ' + name_of_fraction(fraction)
    else:
        if name_of_fraction(fraction) == 'zero':
            decimal_name = 'zero'
        else:
            decimal_name = name_of_fraction(fraction)

    return decimal_name

def name_in_dollars(dollars, cents):
    dollar_name = ''
    
    if dollars == 0:
        if cents == 0:
            return 'zero dollars'
        elif cents == 1:
            return 'one cent'
        else:
            dollar_name += name_of_integer(cents) + ' cents'

    else:
        if cents == 0:
            if dollars == 1:
                return 'one dollar'
            else:
                dollar_name += name_of_integer(dollars) + ' dollars'
        elif cents == 1:
            dollar_name += name_of_integer(dollars) + ' dollars and ' + name_of_integer(cents) + ' cent' 
        else:
            dollar_name += name_of_integer(dollars) + ' dollars and ' + name_of_integer(cents) + ' cents'

    return dollar_name

def name_of_number(input_string):   

    if any(char.isdigit() for char in input_string):
        if '$' in input_string:
            blank, dollar = input_string.split('$')
            if '.' in dollar:
                dollar_ones, dollar_cents = dollar.split('.')
                if int(dollar_cents) == 0:
                    number_name = name_in_dollars(int(dollar_ones), 0)
                else:
                    if len(dollar_cents) == 1:
                        number_name = name_in_dollars(int(dollar_ones), (int(dollar_cents) * 10))
                    elif len(dollar_cents) == 2:
                        number_name = name_in_dollars(int(dollar_ones), int(dollar_cents))
                        if dollar_cents[1] == '0':
                            number_name = name_in_dollars(int(dollar_ones), (int(dollar_cents) * 10))
                        else:
                            number_name = name_in_dollars(int(dollar_ones), int(dollar_cents))
            else:
                number_name = name_in_dollars(int(dollar), 0)
        elif '$' not in input_string:
            if '.' in input_string:
                ones, tenth = input_string.split('.')
                if int(tenth) == 0:
                    number_name = name_of_integer(int(ones))
                else:
                    if tenth[0] == '0':
                        if tenth[1] == '0':
                            number_name = name_of_decimal(int(ones), (tenth, 1000))
                        elif tenth [1] != '0':
                            number_name = name_of_decimal(int(ones), (tenth, 100))
                    elif tenth[0] != '0':
                        if int(tenth) in range (1, 10):
                            number_name = name_of_decimal(int(ones), (tenth, 10))
                        elif int(tenth) in range (10, 100):
                            number_name = name_of_decimal(int(ones), (tenth, 100))
                        elif int(tenth) in range (100, 1000):
                            number_name = name_of_decimal(int(ones), (tenth, 1000))
            else:
                number_name = name_of_integer(int(input_string))
    else:
        return input_string

    return number_name

def get_raw_words(sentence):
    return sentence.split()

def clean_number(raw_word):
    if len(raw_word) == 0:
        return ('')
    else:
        for n in range (0, len(raw_word)):
            if not (raw_word[n].isdigit() or raw_word[n] == '$' or raw_word[n] == '.'):
                return (raw_word[:n], raw_word[n:])
            
    return (raw_word, '')

def named_pairs(pair_list):
    new_list = []
    for n in range (0, len(pair_list)):
        named_word = name_of_number(pair_list[n][0])
        add_punctuation = (named_word, pair_list[n][1])
        new_list.append(add_punctuation)
        
    return new_list

def reassemble(pair_list):
    sentence = ''
    for n in range(0, len(pair_list)):
        if n == (len(pair_list) - 1):
            sentence += pair_list[n][0] + pair_list[n][1]
        else:
            sentence += pair_list[n][0] + pair_list[n][1] + ' '

    return sentence

def replaced_sentence(sentence):
    clean_list = []
    for n in get_raw_words(sentence):
        clean_list.append(clean_number(n))
        
    return reassemble(named_pairs(clean_list))        

def main():
    sentence = input('Please enter your sentence: ')
    print(replaced_sentence(sentence))

if __name__ == "__main__":
    main()
