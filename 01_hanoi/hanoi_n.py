'''towers of hanoi for m towers and n rings'''

from typing import TypeVar, Generic, List, Dict

import argparse

T = TypeVar('T')

# represent tower as a stack
class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = [] 

    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

# generate dict of empty towers 
# m is number of towers
def stack_gen(m: int) -> Dict[int, Stack[int]]:
    assert m > 2, 'at least 3 towers'
    return {k:Stack() for k in range(1, m+1)}

# stack rings on tower 
# n is the number of rings
def stack_init(stack: Stack[int], n: int) -> List[int]:
    assert n > 2, 'at least 3 rings'
    for i in range(1, n+1):
        stack.push(i)

# classic n rings, 3 tower recursion
def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n==1:
        end.push(begin.pop())
        print(f'''{begin} {temp} {end}''')
    else:
        hanoi(begin, temp, end, n-1)
        hanoi(begin, end, temp, 1)
        hanoi(temp, end, begin, n-1)

# for n rings, m towers
def hanoi_n(n: int, m:int) -> Dict[int, Stack[int]]:
    # base case
    if n==3 and m==3:
        hanoi(stacks[1], stacks[3], stacks[2], 3)
    else:
        # put aside rings to towers beyond 3
        for i in range(2, m-1):
            stacks[i].push(stacks[1].pop())
            n-=1
            print(f'{stacks}')
            
        # run recursion for 3 remaining towers
        hanoi(stacks[1], stacks[m], stacks[m-1], n)

        # push set aside rings to end tower
        for i in reversed(range(2, m-1)):
            stacks[m].push(stacks[i].pop())
            print(f'{stacks}')
    return stacks


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='solve hanoi for n rings and m towers')
    parser.add_argument('rings', metavar='n', type=int, help='number of rings')
    parser.add_argument('towers', metavar='m', type=int, help='number of towers')
    args = parser.parse_args()
    stacks = stack_gen(args.towers)
    stack_init(stacks[1],args.rings)
    print(f'{stacks}')
    hanoi_n(args.rings, args.towers)

