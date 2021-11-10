def main():
    n = int(input())
    #ar = input()
    #arr = list(set(map(int, ar.strip().split())))
    arr = list(set(map(int, input().strip().split())))[:n]
    
    arr.sort(reverse=True)
    print(arr[1])
        
    


if __name__ == "__main__":
  main()

