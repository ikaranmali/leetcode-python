class Solution:

    def compute(self, x) -> int:
        temp_x = str(x)
        temp_list = []
        for num in temp_x:
            temp_list.append(num)
        temp_list.reverse()
        strings = [str(integer) for integer in temp_list]
        a_string = "".join(strings)
        x =  int(a_string)
        if (x <=2147483647):
            return x 
        else:
            return 0
        
    def reverse(self, x: int) -> int:

        to_return_value = 0
        sign = False
        # check integer is in range or not.
        if (x >= -2147483648) and (x <=2147483647):
            if (x >= -2147483648 and x < 0):
                x = abs(x)
                sign = True
                return -(self.compute(x))
            else:
                sign = False
            return self.compute(x)
        else:
            return to_return_value
