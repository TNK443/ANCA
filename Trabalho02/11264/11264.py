if __name__ == '__main__':
    T = int(input())

    for _ in range(T):
        n = int(input())
        valores = input().split()

        sum =int(valores[0])

        if (n > 1):
              nMoedas = 2 # normalmente começamos com pelo menos 2 moedas 
        else: nMoedas = 1 #caso de teste para 1 única moeda
        
        # Para obter o maior números de moedas começamos com as moedas de valores menores.
        for i in range(n-1):
            if  (sum < int(valores[i])) and (sum + int(valores[i]) < int(valores[i + 1])):
                sum += int(valores[i]);
                nMoedas+=1
        print(nMoedas, end='\n')
    exit(0)