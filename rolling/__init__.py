import sys
from matplotlib.cbook import Null
from pdb import post_mortem



class Window(object):

    def __init__(self):
        self.list = ""

        
    def size(self, number):
        list = [None] * number
        return list  
    
    def max(self, alist):
        max = alist[0]
        for large in alist:
            if max < large:
                max = large       
        return max
    
    def getAverage(self, alist, size):
        sum = 0
        for number in alist:
            if isinstance(number, int):
                sum += number
        return sum/size
    
    def changeToTupe(self, alist):
        return tuple(alist)
    
    
def main():
    position = 0
    smallWindow = Window()
    smallList = smallWindow.size(3)
    
   
    for arg in sys.argv[1:]:
        if isinstance(int(arg), int):
            smallList.pop(position)
            smallList.insert(position, int(arg))
            print smallWindow.changeToTupe(smallList)
            print smallWindow.max(smallList)
            position+=1 
            if position  == 3:
                position = 0
            print smallWindow.getAverage(smallList, 3);
        
        
        
    position = 0
    largeWindow = Window()
    largeList = largeWindow.size(20)


    for arg in sys.argv[1:]:
        if isinstance(int(arg), int):
            largeList.pop(position)
            largeList.insert(position, int(arg))
            print largeWindow.changeToTupe(largeList)
            print largeWindow.max(largeList)
            position+=1
            if position  == 20:
                position = 0
            print largeWindow.getAverage(largeList, 20);

if __name__ == "__main__":
    main()