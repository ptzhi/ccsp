'''
we now have Red, Yellow, Blue, and Green(!) 

% python dd2_vocations_cli.py N [N is number of vocations, in this case 4]
'''

# from typing import TypeVar, Generic, List

import argparse

class Vocations:
    def __init__(self, n:int) -> None:
        self.single(n)
        self.double(n)
        self.hybrid(n)
        self.count()

    def single(self, n:int) -> list[str]:
        self._single = [chr(x) for x in range(65, 65+n)]

    def double(self, n:int) -> list[str]:
        self._double = [[chr(x), chr(x)] for x in range(65, 65+n)]

    def hybrid(self, n: int) -> list[str]:
        self._hybrid = []
        m = n-1
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
    parser = argparse.ArgumentParser(description='Display class vocations')
    parser.add_argument(
            '--classes', 
            metavar='N', 
            type=int,
            default=4,
            help='number of base vocations'
            )
    args = parser.parse_args()
    v = Vocations(args.classes)
    print(f'''
    single ({len(v._single)}) {v._single}
    double ({len(v._double)}) {v._double}
    hybrid ({len(v._hybrid)}) {v._hybrid}
    total count = {v._count}
    ''')

