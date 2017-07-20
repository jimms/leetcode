class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = [0] * n
        for n in range(1, n + 1):
            if n % 15 == 0:
                ret[n - 1] = 'FizzBuzz'
            elif n % 5 == 0:
                ret[n - 1] = 'Buzz'
            elif n % 3 == 0:
                ret[n - 1] = 'Fizz'
            else:
                ret[n - 1] = str(n)

        return ret
