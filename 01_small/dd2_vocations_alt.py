'''
we now have Red, Yellow, Blue, and Green(!)
'''

# from typing import TypeVar, Generic, List

import argparse

class Vocations:
    def __init__(self, base: list[int]) -> None:
        self.single(base)
        self.double(base)
        self.hybrid(base)
        self.count()

    def single(self, base:list[int]) -> list[str]:
        self._single = base

    def double(self, base:list[int]) -> list[str]:
        self._double = [[x, x] for x in base]

    def hybrid(self, base: list[int]) -> list[str]:
        self._hybrid = []
        m = len(base)-1
        for i in range(0, m):
            self._hybrid.extend(list(
                    zip(
                        [self._single[i] for _ in range(i, m)],
                        self._single[-(m-i)::]
                        )
                    ))

    def count(self) -> int:
        self._count = len(self._single) + len(self._double) + len(self._hybrid)
        return self._count

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='dd2 vocation combos')
    parser.add_argument(
            '--classes',
            nargs='*',
            type=str,
            metavar='C',
            default=['Fighter','Archer','Thief','Mage'],
            help="List of class separated by white space e.g. Fighter Mage ... "
            )
    args = parser.parse_args() 
    # base = ['Fighter','Archer','Thief','Mage']
    v = Vocations(args.classes)
    print(f'''
    single ({len(v._single)}) {v._single}
    double ({len(v._double)}) {v._double}
    hybrid ({len(v._hybrid)}) {v._hybrid}
    total count = {v._count}
    ''')
