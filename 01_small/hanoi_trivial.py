'''
3 vertical sticks call them A B C, 3 donuts call them x, y, z with decreasing radius

x, y, z are all on A stacked in order (x bottom, z top)

problem: 
    move them from A to C given
    1. only one donut can be moved at any time
    2. only the top donut is available for moving
    3. bigger donut can never set on top of smaller donut

solution:
    if there are n-1 towers for n donuts, the solution is trivial:
    suppose start is n1 and target is nn
    1. place top donut from n1 to nn
    2. place rest of donut to n2...nn-1 (largest still on n1, all towers have on donut)
    3. place nn's donut anywhere n2...nn-1 (nn free)
    4. place n1's final and largest donut on nn (n1 free)
    5. place smallest donut thats on n2...nn-1 to n1
    6. stack in order on nn

    if there are N towers for N+j donuts then it is harder
'''
# n donuts for n-1 towers (trivial)
class TowersTrivial:
    def __init__(self, n: int) -> None:
        self.towers = self.tower_build(n)

    def tower_yield(self, n: int):
        yield [x for x in range(0,n)]
        i = 0
        while i < n:
            i+=1
            yield []

    def tower_build(self, n: int):
        return [l for l in self.tower_yield(n)]

    def push(self, item, destination):
        return destination.append(item)

    def distribute(self, d: list[int]):
        for i in range(0, len(d)-1):
            self.push(d[0].pop(), d[i+1])
            print(d)
        return d

    def stack(self, s: list[int]):
        for i in range(2, len(s)):
            self.push(s[-i].pop(), s[-1])
            print(s)
        return s

# n donuts for n-i towers where i: int, 1 < i < n-2

if __name__ == '__main__':
    t = TowersTrivial(5)
    t_o = str(t.towers[0])
    print(f'original: {t.towers}')
    t_d = t.distribute(t.towers)
    t_s = t.stack(t_d)
    print(f'final: {t_s}')
    print(f'original == final: {t_o==str(t_s[-1])}')

