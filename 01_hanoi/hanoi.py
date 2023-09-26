from typing import TypeVar, Generic, List

T = TypeVar('T') # donut can be represented by any type

# create stack as a class with generic (list) of T
class Stack(Generic[T]):

    # initialize empty list as our stack
    def __init__(self) -> None:
        self._container: List[T] = []

    # push an item to our stack
    def push(self, item: T) -> None:
        self._container.append(item)

    # remove item at end of stack and return it
    def pop(self) -> T:
        return self._container.pop()

    # allows print to show stack
    def __repr__(self) -> str:
        return repr(self._container)

# push rings to stack1
def rings_int(num_rings: T) -> List[T]:
    num_rings: int = 3 #if not int, need to be wary of order
    for n in range(1, num_rings+1):
        stack1.push(n)
    
# movement logic with recursion
def hanoi(begin: Stack[int], end: Stack[int], temp:Stack[int], n: int) -> None:
    '''
    1. move n-1 items from begin tower to temp tower
    2. move the remaining item from begin tower to end tower
    3. move n-1 items from temp tower to end tower
    '''

    if n == 1:
        end.push(begin.pop())
        print(f'''
        begin: {begin}
        temp: {temp}
        end: {end}
        ''')
   
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)
    

#def move(A, B, C, n):
#
#    if n%2==0:
#        #pattern 12 112 112 112
#       
#    else:
#        
#        #pattern  2 112 112 112
#        #n and n-2 cannot be ever stacked consecutively
#        #2. do not move same number consecutively
#        #cannot move from empty tower
#        #to move on top, must be greater
           
           

if __name__ == '__main__':
    # create empty stacks
    stack1: Stack[int] = Stack()
    stack2: Stack[int] = Stack()
    stack3: Stack[int] = Stack() 
    n=3
    rings_int(n)
    print(f'''
        begin: {stack1}
        temp: {stack2}
        end: {stack3}
        ''')
    hanoi(stack1, stack2, stack3, n)

