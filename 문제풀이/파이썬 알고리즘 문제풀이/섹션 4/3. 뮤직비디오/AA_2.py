import sys
# sys.stdin = open('input.txt', 'rt')


def get_count(x):
    global songs
    cnt = 1
    tot = 0
    for song in songs:
        if tot + song > x:
            cnt += 1
            tot = song
        else:
            tot += song
    return cnt


if __name__ == "__main__":
    n, m = map(int, input().split())
    songs = list(map(int, input().split()))

    s = 1
    e = sum(songs)
    ans = e

    while s <= e:
        mid = (s+e) // 2
        if get_count(mid) <= m:
            ans = min(ans, mid)
            e = mid - 1
        else:
            s = mid + 1

    print(ans)
