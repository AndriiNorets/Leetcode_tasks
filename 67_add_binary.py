class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a == '0' and b == '0':
            return '0'
            
        a = a[::-1]
        b= b[::-1]
        a = [int(a[item]) * (2**item) for item in range(len(a))]
        b = [int(b[item]) * (2**item) for item in range(len(b))]

        sume = sum(a) + sum(b)

        squere_array = []
        item = 0
        while sum(squere_array) < sume:
            squere_array.append(2**item)
            item+=1

        squere_array = squere_array[::-1]
        result = ""
        for item in squere_array:
            if item <= sume:
                result += '1'
                sume -= item
            else:
                result += '0'


        return result