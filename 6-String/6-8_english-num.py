#!usrbinenv python
class numtool():
    zero_to_nine = ['zero','one','two','three','four','five','six','seven','eight','nine']
    ten_to_nineteen = ['ten','eleven','twelve','thirdteen','fourteen','fifteen','sixteen','eighteen','nineteen']
    twenty_to_ninety = ['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
    hundred = 'hundred'
    _and = ' and '
    space = ' '

    def num2en_0_to_100(self, num):
        if not 0 <= num < 100:
            return        

        elif num < 10:
            return self.zero_to_nine[num]
        elif num < 20:        
            return self.ten_to_nineteen[num-10]
        elif num < 100:
            if num % 10 == 0:
                return self.twenty_to_ninety[num/10 - 2]
            else:
                left = self.twenty_to_ninety[num/10 - 2]
                right = self.zero_to_nine[num % 10]
                return left + self.space + right

    def num2en(self, num):
        if not 0 <= num <= 1000:
            return        

        if num < 100:
            return self.num2en_0_to_100(num)
        else:
            if num == 1000:
                return 'one thousand'
            elif num % 100 == 0:
                return self.zero_to_nine[num / 100] + self.space + self.hundred
            else:                
                left = self.zero_to_nine[num / 100]
                right = self.num2en_0_to_100(num % 100)
                return left + self.space + self.hundred + self._and + right

tool = numtool()
while True:
    num = raw_input('input a number: ')
    print tool.num2en(int(num))