from sys import argv


class SchoolMult:

    def __init__(self, multiplicador: str = '0', multiplicando: str = '0'):
        self.multiplicador = multiplicador
        self.multiplicando = multiplicando
        self.mid_numbers = list()
        self.result_signal = 1
        self.potence = 0
        self.mid_sum = '0'
        self.result = '0'

    @property
    def higher_number(self):
        if self.multiplicando > self.multiplicador:
            return self.multiplicando
        else:
            return self.multiplicador

    @property
    def lower_number(self):
        if self.multiplicando > self.multiplicador:
            return self.multiplicador
        else:
            return self.multiplicando

    @staticmethod
    def potence_format(number: str):
        number = number.replace('-', '')
        number = number.replace('+', '')
        point_location = number.find('.')

        if point_location == -1:
            potence = 0
        else:
            number = number.rstrip('0')
            number = number.replace('.', '')
            potence = len(number) - point_location

        return number, potence

    def signal(self):
        if self.multiplicador != '0' and self.multiplicando != '0':
            self.result_signal = float(self.multiplicador)
            self.result_signal *= float(self.multiplicando)
            self.result_signal /= abs(self.result_signal)
            self.result_signal = int(self.result_signal)
        else:
            self.result_signal = 1

    def ten_potence(self):
        self.potence = 0
        self.potence += self.potence_format(self.multiplicando)[1]
        self.potence += self.potence_format(self.multiplicador)[1]

    def mid_operation(self):

        lower, _ = self.potence_format(self.lower_number)
        lower = str(lower)
        higher, _ = self.potence_format(self.higher_number)
        higher = str(higher)
        for index in range(len(lower)-1, -1, -1):
            parsial_result = 0
            for mult_place, mult_index in enumerate(range(len(higher)-1, -1, -1)):
                parsial_mult = int(lower[index]) * int(higher[mult_index])
                parsial_mult *= 10**mult_place
                parsial_result += parsial_mult
            parsial_result = str(parsial_result)
            self.mid_numbers.append(parsial_result)

        return self.mid_numbers

    def final_sum(self):
        self.mid_sum = [int(number)*(10**index) for index, number in enumerate(self.mid_numbers)]
        self.mid_sum = sum(self.mid_sum)
        self.mid_sum = str(self.mid_sum)
        self.result = self.include_decimal(self.mid_sum, 0)
        self.result = '+'+self.result if self.result_signal > 0 else '-'+self.result
        try:
            self.result = '+0'+self.result[1:] if self.result[1] == '.' else self.result
        except IndexError:
            pass

    def include_decimal(self, number, spaces):
        if self.potence <= spaces:
            if self.potence > 0:
                number += ' '*(spaces+1)
            else:
                number += ' '*(spaces)
        elif self.potence >= len(number) + spaces:
            number = '0.' + '0'*(self.potence-(len(number)+spaces)) + number
            number += ' '*spaces
        else:
            number = number + ' '*(spaces)
            number = number[:-self.potence] + '.' + number[-self.potence:]
        return number

    def include_signal(self, number):
        if number.find('-') != -1 or number.find('+') != -1:
            number = number
        elif self.result_signal < 0:
            number = '-'+number
        else:
            number = '+'+number
        return number

    def format_number_str(self, number, spaces):
        number = self.include_decimal(number, spaces)
        number = self.include_signal(number)
        number = ' '*(len(self)-len(number))+number
        return number

    def __len__(self):
        return len(str(self.result))

    def __str__(self):
        elements = ['  '+' '*(len(self)-len(self.higher_number))+self.higher_number,
                    'x '+' '*(len(self)-len(self.lower_number))+self.lower_number,
                    '---'+'-'*len(self)]
        elements += ['  '+self.format_number_str(number, index)
                     for index, number in enumerate(self.mid_numbers)]

        elements += ['---'+'-'*len(self), '  '+self.result]

        return '\n'.join(elements)

    def __repr__(self):
        return f"SchoolMult('{self.multiplicador}', '{self.multiplicando}')"


if __name__ == '__main__':

    if len(argv) == 3:
        Multiplication = SchoolMult(argv[1], argv[2])
        Multiplication.signal()
        Multiplication.ten_potence()
        Multiplication.mid_operation()
        Multiplication.final_sum()
        print(str(Multiplication))
