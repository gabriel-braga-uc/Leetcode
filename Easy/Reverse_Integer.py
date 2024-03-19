class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            s = 1
        elif x < 0:
            s = -1
            x *= -1
        else:
            return(0)
        x_arr = []
        for n in (str(x)):
            x_arr.append(n)
        while(x_arr[len(x_arr)-1] == "0"):
            x_arr.pop(-1)
        final = (s * int(''.join(x_arr[::-1])))
        if(final > 2147483647 or final < -2147483648):
            return(0)
        else:
            return(final)