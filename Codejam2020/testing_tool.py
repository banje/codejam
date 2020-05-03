import random

b = 20
t = 1

def quantum_twist(array, num):
    rand = random.randrange(4)
    sys.stderr.write("twisting {} with {}\n".format(num, rand))
    if rand >= 2:
        array = array[::-1]
        sys.stderr.write("flipped axis\n")
    if rand % 2:
        array = [1-i for i in array]
        sys.stderr.write("reverted bit\n")
    sys.stderr.write(str(array)+'\n')
    return array

import sys
if len(sys.argv) >= 2:
    b = int(sys.argv[-1])
if len(sys.argv) == 3:
    t = int(sys.argv[-2])
input = sys.stdin.readline

print(t, b)
sys.stdout.flush()
for case in range(t):
    sys.stderr.write("Case started\n")
    ans = [random.randrange(2) for i in range(b)]
    original = ''.join(map(str, ans))

    num_query = 0
    y = [2] * b
    while num_query < 151:
        query = input().rstrip()
        if len(query) == b:
            y = [*map(int, query)]
            break
        else:
            if num_query % 10 == 0:
                ans = quantum_twist(ans, num_query)
            k = int(query)
            assert 0 < k <= b
            print(ans[k - 1])
            sys.stdout.flush()
            num_query += 1
    
    for i, j, idx in zip(ans, y, range(b)):
        if i != j:
            print('N')
            sys.stdout.flush()
            sys.stderr.write("wrong at t = {}, b = {}, initial_state = {}\n".format(case + 1, b, original))
            sys.stderr.write("ans = {} wrong index = {}\n".format(ans, idx))
            sys.stderr.write("you = {},\n".format(y))
            sys.stderr.write("you = {}, {}\n".format(y[::-1], y[::-1] == ans))
            sys.exit(0)
    else:
        print('Y')
        sys.stdout.flush()