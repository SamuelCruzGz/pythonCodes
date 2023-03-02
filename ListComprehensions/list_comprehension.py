if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    listFinal = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                sumIJK = i+j+k
                if (sumIJK!=n):
                   listFinal.extend([i, j, k])
    output=[listFinal[i:i + 3] for i in range(0, len(listFinal), 3)]
    print(output)
