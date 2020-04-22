import sys
# sys.stdin = open('input.txt', 'rt')

if __name__ == "__main__":
    n = int(input())
    line = [0] * (n+1)
    line[0] = 0
    line[1] = 1
    line[2] = 2

    for i in range(3, n+1):
        line[i] = line[i-1] + line[i-2]
    print(line[n])
