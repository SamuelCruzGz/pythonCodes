if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    arrSorted = sorted(arr, reverse= True)
    for i in range(len(arrSorted)):
        if arrSorted[i]!= arrSorted[0]:
            print(arrSorted[i])
            break


