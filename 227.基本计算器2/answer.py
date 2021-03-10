class Solution(object):
    def calculate(self, s):
        numbers,opts,i= [],[],0 #分别存数字列表,运算符列表和索引
        while i < len(s):
            if s[i] == " ": #忽略空格
                i += 1
            elif s[i] == "+" or s[i] == "-" or s[i] == "*" or s[i] == "/": #加减乘除加入运算符列表
                opts.append(s[i])
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num  * 10 + int(s[i])
                    i += 1
                numbers.append(num)  #提取数字 提取完数字判断如果他要执行的操作是乘或除则直接计算，如果是加或者减则留到最后计算
                if opts and (opts[-1] == "*" or opts[-1] == "/"):
                    num2 = numbers.pop()
                    num1 = numbers.pop()
                    if opts[-1] == "*":
                        numbers.append(num1 * num2)
                    else:
                        numbers.append(num1 // num2)
                    opts.pop()
        num = numbers[0] # 数字列表长度应该比运算符列表长度长1,按从左往右顺序计算加法/减法
        for i in range(len(opts)):
            if opts[i] == "+":
                num += numbers[i+1]
            else:
                num -= numbers[i+1]
        return num