# ===== CODIGO COM CACHE BIB CACHE =====
# ===== ABORDAGEM DE CIMA PRA BAIXO
import sys
from functools import lru_cache

sys.setrecursionlimit(100000)

MAX_N = 1001
MAX_W = 31

N = 0
V = [0] * MAX_N
W = [0] * MAX_N

@lru_cache(maxsize=None)
def dinamicProg(id, w):
  if (id == N) or (w == 0): return 0
  if W[id] > w:
     return dinamicProg(id+1, w)
  return max(dinamicProg(id+1, w), V[id]+dinamicProg(id+1, w-W[id]))


if __name__ == '__main__':
  T = int(input())
  for _ in range(T):
    dinamicProg.cache_clear()
    N = int(input())
    for i in range(N):
      V[i], W[i] = map(int, input().split())
    ans = 0
    G = int(input())
    for _ in range(G):
      MW = int(input())
      ans += dinamicProg(0, MW)
    print(ans)