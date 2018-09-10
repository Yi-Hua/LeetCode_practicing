# 38. Count and Say  (Easy)  ✓
# The count-and-say sequence is the sequence of integers with the first five terms as following:
''' 1.     1        1個1: 11           count-and-say sequence: 1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...
    2.     11       2個1: 21           敘述上一個的數字個數 
    3.     21       1個2,1個1: 1211   
    4.     1211     1個1,1個2,2個1:111221
    5.     111221   ...
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.  '''
# Given an integer n, generate the nth term of the count-and-say sequence. 
# Note: Each term of the sequence of integers will be represented as a string. 
''' Example 1: 
    Input: 1        Input: 4
    Output: "1"     Output: "1211"  '''

class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        dic = {1:'1'}
        result = str(1)
        for i in range(2,n+1):
            s = ''
            count = 1
            for j in range(1,len(result)):
                if result[j] == result[j-1]:
                    count += 1
                else:
                    s = s + str(count*10 + int(result[j-1]))
                    count = 1
            
            s = s + str(count*10 + int(result[len(result)-1]))
            dic[i] = s
            result = s
        return result
        

        

if __name__ == '__main__':
    a = int(input())
    sol = Solution()
    print(sol.countAndSay(a))
