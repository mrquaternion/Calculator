class Input:
    def __init__(self, operation):
        self.operation = operation

    def removeSpaces(self):
        return self.operation.replace(' ', '')

    def evaluateSymbols(self):
        updatedOperation = self.removeSpaces()
        result = self.evaluateTerm(updatedOperation)
        return result

    def evaluateTerm(self, operation):
        symbols = '+-*/'
        parts = []
        startIndex = 0

        if not any(c in symbols for c in operation):
            raise ValueError(
                "Expected an operation, received only letters or numbers.")

        for i in range(len(operation)):
            if operation[i] in symbols:
                parts.append(float(operation[startIndex:i]))
                startIndex = i+1
                parts.append(operation[i])
        parts.append(float(operation[startIndex:]))

        i = 0
        while i < len(parts):
            if parts[i] == '*':
                parts[i-1:i+2] = [float(parts[i-1]) * float(parts[i+1])]
            elif parts[i] == '/':
                parts[i-1:i+2] = [float(parts[i-1]) / float(parts[i+1])]
            else:
                i += 1

        result = float(parts[0])
        for i in range(1, len(parts), 2):
            if parts[i] == '+':
                result += float(parts[i+1])
            elif parts[i] == '-':
                result -= float(parts[i+1])
        return result


end = False
while not end:
    try:
        end_input = input('Enter an operation: ')
        if end_input.lower() == 'q':
            end = True
        else:
            result = Input(end_input).evaluateSymbols()
            print(result)
    except ValueError as e:
        print(e)
