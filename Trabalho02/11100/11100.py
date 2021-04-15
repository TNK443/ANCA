if __name__ == '__main__':
    try:
      while True:
        n = int(input())
        if n == 0: break

        aux = list(map(int, input().split()))
        aux.sort()
        bags = aux

        maxPecas = 1
        cursor = 1
        
        # Verificar qual o maior numero de bags repetidas
        for i in range(1,len(bags)):
            if (bags[i] == bags[i-1]):cursor+=1
            else: cursor = 1
            maxPecas = max(cursor, maxPecas)
        print(maxPecas)

        for i in range(maxPecas):
            out = ''
            out = str(bags[i])
            # print(bags[i])
            for j in range(i+maxPecas, n, maxPecas):
                if j!=i: out += ' '
                out += str(bags[j])
                # print(bags[j])           
            print(out)
        print('')
    
    except EOFError:
      pass

    finally:
      exit(0)
    exit(0)