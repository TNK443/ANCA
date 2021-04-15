# ===== CODIGO SEM RECUSIVIDADE COM MATRIZ MEMO
# ===== ABORDAGEM DE BAIXO PRA CIMA
MAX_N = 1001
MAX_W = 31

N = 0

if __name__ == '__main__':
  T = int(input())  

  for _ in range(T):
    N = int(input())
    V = [0] * (N+1)
    W = [0] * (N+1)
    for i in range(1,N+1):
      V[i], W[i] = map(int, input().split())

    memo=[]
    for i in range(N+1):
        memo.append([0]*(max(W)+1))

    ans = 0
    G = int(input())

    for _ in range(G):
      MW = int(input())

      for i in range(1, N+1):
        for w in range(1, MW+1):
          if (W[i] > w): memo[i][w] = memo[i-1][w]
          else:          memo[i][w] = max(memo[i-1][w], V[i] + memo[i-1][w-W[i]])

      ans += memo[N][MW];

    print(ans)