
class StringCalculator:
    def add(self,inputNumbers):
        if len(inputNumbers) == 0:
            return 0
        numbers = self.splitter(inputNumbers)
        print(numbers)
        for i in range(0,len(numbers)):
            numbers[i] = int(numbers[i])
        return sum(numbers)  

    def sum(self,numbers):
        sum = 0
        for i in numbers:
            sum += i
        return sum

    def splitter(self,numbers):
        return numbers.split(",")
        
s = StringCalculator()  
print(s.add(""))
