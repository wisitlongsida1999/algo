class myqueue(object):

    def __init__(self):
        self.myqueue = []
    def push(self, x):
        """
        :type x: int
        :rtype: none
        """
        self.myqueue.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        return self.myqueue.pop(0)
        

    def peek(self):
        """
        :rtype: int
        """
        return self.myqueue[0]
        

    def empty(self):
        """
        :rtype: bool
        """
        return self.myqueue == []
        
        


# your myqueue object will be instantiated and called as such:
# obj = myqueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()