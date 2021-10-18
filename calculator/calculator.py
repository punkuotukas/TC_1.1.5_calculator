import time


class Calculator:

    def __init__(self):
        self.memory = 0

    def add(self, num_to_add):
        memory = self.memory
        memory = float(memory) + float(num_to_add)
        self.memory = memory
        return print(memory)

    def subtract(self, num_to_subtract):
        memory = self.memory
        memory = float(self.memory) - float(num_to_subtract)
        self.memory = memory
        return print(memory)

    def multiply(self, num_to_multiply_by):
        memory = self.memory
        memory = float(memory) * float(num_to_multiply_by)
        self.memory = memory
        return print(memory)

    def divide(self, num_to_divide_by):
        try:
            memory = self.memory
            memory = round(float(memory) / float(num_to_divide_by), 4)
            self.memory = memory
        except ZeroDivisionError:
            print('What\'s the point of dividing something by zero?')
        return print(memory)

    def take_root(self, power_of_root: float):
        memory = float(self.memory)
        if memory < 0:
            return print('Negative root makes no sense. Give it another try.')
        elif power_of_root == 0:
            print('There is no realistic reason to take 0th root.')
        else:
            memory = round(float(memory) ** (1/float(power_of_root)), 4)
            return print(memory)

    def reset_memory(self):
        self.memory = 0
        memory = self.memory
        print('Memory reset\n0')
        return memory

    def operation(self, operation_input):
        if operation_input == '+':
            num_to_add = input('Number to add?\n')
            return self.add(num_to_add)
        elif operation_input == '-':
            num_to_subtract = input('Number to subtract?\n')
            return self.subtract(num_to_subtract)
        elif operation_input == '/':
            num_to_divide_by = input('Number to divide by?\n')
            return self.divide(num_to_divide_by)
        elif operation_input == '*':
            num_to_multiply_by = input('Number to multiply by?\n')
            return self.multiply(num_to_multiply_by)
        elif operation_input == 'R':
            power_of_root = float(input('Power of root?\n'))
            return self.take_root(power_of_root)
        elif operation_input == '0':
            return self.reset_memory()
        else:
            print('Invalid operator')


if __name__ == '__main__':
    print('Welcome')
    time.sleep(1)
    print('This program does basic math calculations.')
    time.sleep(2)
    message = '''\
    Type \'exit\' or press \'Ctrl+c\' at any moment to close the program
    and \'0\' for operation to reset calculator\'s memory.\
    '''
    print(message)
    time.sleep(2)
    calculator = Calculator()
    num_to_operate_on = input('What\'s the number to operate on?\n')
    calculator.memory = num_to_operate_on
    while True:
        if num_to_operate_on != 'exit':
            operator = input('Operator:\n[+, -, *, /, R, 0]?\n')
        if operator == 'exit':
            break
        elif operator == 0:
            calculator.reset_memory()
        else:
            calculator.operation(operator)
            if Exception():
                continue
