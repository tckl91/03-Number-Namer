import unittest
from number_namer import *

class testNumberNamer(unittest.TestCase):

    def test_name_of_digit(self):
        self.assertEqual(name_of_digit(0), 'zero')
        self.assertEqual(name_of_digit(1), 'one')
        self.assertEqual(name_of_digit(2), 'two')
        self.assertEqual(name_of_digit(3), 'three')
        self.assertEqual(name_of_digit(4), 'four')
        self.assertEqual(name_of_digit(5), 'five')
        self.assertEqual(name_of_digit(6), 'six')
        self.assertEqual(name_of_digit(7), 'seven')
        self.assertEqual(name_of_digit(8), 'eight')
        self.assertEqual(name_of_digit(9), 'nine')

    def test_name_of_tens(self):
        self.assertEqual(name_of_tens(1), 'ten')
        self.assertEqual(name_of_tens(2), 'twenty')
        self.assertEqual(name_of_tens(3), 'thirty')
        self.assertEqual(name_of_tens(4), 'forty')
        self.assertEqual(name_of_tens(5), 'fifty')
        self.assertEqual(name_of_tens(6), 'sixty')
        self.assertEqual(name_of_tens(7), 'seventy')
        self.assertEqual(name_of_tens(8), 'eighty')
        self.assertEqual(name_of_tens(9), 'ninety')

    def test_name_of_teens(self):
        self.assertEqual(name_of_teens(10), 'ten')
        self.assertEqual(name_of_teens(11), 'eleven')
        self.assertEqual(name_of_teens(12), 'twelve')
        self.assertEqual(name_of_teens(13), 'thirteen')
        self.assertEqual(name_of_teens(14), 'fourteen')
        self.assertEqual(name_of_teens(15), 'fifteen')
        self.assertEqual(name_of_teens(16), 'sixteen')
        self.assertEqual(name_of_teens(17), 'seventeen')
        self.assertEqual(name_of_teens(18), 'eighteen')
        self.assertEqual(name_of_teens(19), 'nineteen')

    def test_name_of_two_digit(self):
        self.assertEqual(name_of_two_digits(10), 'ten')
        self.assertEqual(name_of_two_digits(12), 'twelve')
        self.assertEqual(name_of_two_digits(79), 'seventy nine')
        self.assertEqual(name_of_two_digits(99), 'ninety nine')

    def test_name_of_three_digit(self):
        self.assertEqual(name_of_three_digits(100), 'one hundred')
        self.assertEqual(name_of_three_digits(108), 'one hundred eight')
        self.assertEqual(name_of_three_digits(112), 'one hundred twelve')
        self.assertEqual(name_of_three_digits(223), 'two hundred twenty three')
        self.assertEqual(name_of_three_digits(700), 'seven hundred')
        self.assertEqual(name_of_three_digits(999), 'nine hundred ninety nine')

    def test_name_of_integer(self):
        self.assertEqual(name_of_integer(0), 'zero')
        self.assertEqual(name_of_integer(3), 'three')
        self.assertEqual(name_of_integer(10), 'ten')
        self.assertEqual(name_of_integer(13), 'thirteen')
        self.assertEqual(name_of_integer(62), 'sixty two')
        self.assertEqual(name_of_integer(111), 'one hundred eleven')
        self.assertEqual(name_of_integer(2222), 'two thousand two hundred twenty two')
        self.assertEqual(name_of_integer(33319), 'thirty three thousand three hundred nineteen')
        self.assertEqual(name_of_integer(414444), 'four hundred fourteen thousand four hundred forty four')
        self.assertEqual(name_of_integer(1000), 'one thousand')
        self.assertEqual(name_of_integer(1000000), 'one million')
        self.assertEqual(name_of_integer(5555555), 'five million five hundred fifty five thousand five hundred fifty five')
        self.assertEqual(name_of_integer(66666666), 'sixty six million six hundred sixty six thousand six hundred sixty six')
        self.assertEqual(name_of_integer(777777777), 'seven hundred seventy seven million seven hundred seventy seven thousand seven hundred seventy seven')

    def test_name_of_fraction(self):
        self.assertEqual(name_of_fraction((1, 10)), 'one tenth')
        self.assertEqual(name_of_fraction((1, 100)), 'one one hundredth')
        self.assertEqual(name_of_fraction((1, 1000)), 'one one thousandth')
        self.assertEqual(name_of_fraction((4, 10)), 'four tenths')
        self.assertEqual(name_of_fraction((6, 100)), 'six hundredths')
        self.assertEqual(name_of_fraction((36, 100)), 'thirty six hundredths')
        self.assertEqual(name_of_fraction((8, 1000)), 'eight thousandths')
        self.assertEqual(name_of_fraction((98, 1000)), 'ninety eight thousandths')
        self.assertEqual(name_of_fraction((711, 1000)), 'seven hundred eleven thousandths')
        self.assertEqual(name_of_fraction((0, 1000)), 'zero')
        
    def test_name_in_dollar(self):
        self.assertEqual(name_in_dollars(0, 1), 'one cent')
        self.assertEqual(name_in_dollars(0, 17), 'seventeen cents')
        self.assertEqual(name_in_dollars(0, 39), 'thirty nine cents')
        self.assertEqual(name_in_dollars(1, 0), 'one dollar')
        self.assertEqual(name_in_dollars(11, 0), 'eleven dollars')
        self.assertEqual(name_in_dollars(32, 0), 'thirty two dollars')
        self.assertEqual(name_in_dollars(18, 43), 'eighteen dollars and forty three cents')
        self.assertEqual(name_in_dollars(10000, 98), 'ten thousand dollars and ninety eight cents')
        
    def test_name_of_decimal(self):
        self.assertEqual(name_of_decimal(0, (1,10)), 'one tenth')
        self.assertEqual(name_of_decimal(3, (1,100)), 'three and one one hundredth')
        self.assertEqual(name_of_decimal(11, (1,1000)), 'eleven and one one thousandth')
        self.assertEqual(name_of_decimal(121, (4, 10)), 'one hundred twenty one and four tenths')
        self.assertEqual(name_of_decimal(2345, (6, 100)), 'two thousand three hundred forty five and six hundredths')
        self.assertEqual(name_of_decimal(1000000, (36, 100)), 'one million and thirty six hundredths')
        self.assertEqual(name_of_decimal(31999999, (8, 1000)), 'thirty one million nine hundred ninety nine thousand nine hundred ninety nine and eight thousandths')
        self.assertEqual(name_of_decimal(99, (98, 1000)), 'ninety nine and ninety eight thousandths')
        self.assertEqual(name_of_decimal(999999, (711, 1000)), 'nine hundred ninety nine thousand nine hundred ninety nine and seven hundred eleven thousandths')
        self.assertEqual(name_of_decimal(999999, (0, 1000)), 'nine hundred ninety nine thousand nine hundred ninety nine')
        self.assertEqual(name_of_decimal(999999, (0, 0)), 'nine hundred ninety nine thousand nine hundred ninety nine')

    def test_name_of_number(self):
        self.assertEqual(name_of_number('$0.75'), 'seventy five cents')
        self.assertEqual(name_of_number('$3.99'), 'three dollars and ninety nine cents')
        self.assertEqual(name_of_number('$8.00'), 'eight dollars')
        self.assertEqual(name_of_number('$1000000.00'), 'one million dollars')
        self.assertEqual(name_of_number('$28'), 'twenty eight dollars')
        self.assertEqual(name_of_number('0.75'), 'seventy five hundredths')
        self.assertEqual(name_of_number('3.99'), 'three and ninety nine hundredths')
        self.assertEqual(name_of_number('8.00'), 'eight')
        self.assertEqual(name_of_number('18'), 'eighteen')
        self.assertEqual(name_of_number('1000000.1'), 'one million and one tenth')
        self.assertEqual(name_of_number('28.127'), 'twenty eight and one hundred twenty seven thousandths')

    def test_clean_number(self):
        self.assertEqual(clean_number('12!'), ('12', '!'))
        self.assertEqual(clean_number('1000'), ('1000', ''))
        self.assertEqual(clean_number('10.01'), ('10.01', ''))

    def test_get_raw_words(self):
        self.assertEqual(get_raw_words('GO BLUE 2015!'), (['GO', 'BLUE', '2015!']))
        self.assertEqual(get_raw_words('Michigan! Wolverines!'), (['Michigan!', 'Wolverines!']))
        self.assertEqual(get_raw_words('? ! #'), (['?', '!', '#']))

    def test_named_pairs(self):
        self.assertEqual(named_pairs([('12', ''), ("Monkeys", '!')]), ([('twelve', ''), ('Monkeys', '!')]))
        self.assertEqual(named_pairs([('I', ''), ('am', ''), ('25', ''), ('years', ''), ('old', '!')]), ([('I', ''), ('am', ''),('twenty five', ''), ('years', ''), ('old','!')]))
        self.assertEqual(named_pairs([('I', ''), ('have', ''), ('$25.68', '!')]), ([('I', ''), ('have', ''),('twenty five dollars and sixty eight cents', '!')]))
        self.assertEqual(named_pairs([('12', '!')]), ([('twelve', '!')]))       

    def test_reassemble(self):
        self.assertEqual(reassemble([('2015', ''), ('UPenn', '!')]),('2015 UPenn!'))
        self.assertEqual(reassemble([('two thousand fifteen', ','), ('UPenn', '!')]),('two thousand fifteen, UPenn!'))
        self.assertEqual(reassemble([('two thousand fifteen', '!')]),('two thousand fifteen!'))
        

    def test_replaced_sentence(self):
        self.assertEqual(replaced_sentence('I am 25 years old!'), ('I am twenty five years old!'))
        self.assertEqual(replaced_sentence('I have $25.68'), ('I have twenty five dollars and sixty eight cents'))
        self.assertEqual(replaced_sentence('xxxxx $300 xxxxx'), ('xxxxx three hundred dollars xxxxx'))
        self.assertEqual(replaced_sentence("September 16, 2015"), ('September sixteen, two thousand fifteen'))
        self.assertEqual(replaced_sentence('I need $21.00 and a 64'), ('I need twenty one dollars and a sixty four'))

unittest.main()
