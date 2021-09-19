def main():
    #write your code below this line
    count = 0
    
    while True:
        num = int(input('Give a number:'))
        
        if num == 0:
            break
        
        count += 1
   print('Number of numbers: ' + str(count))
if __name__ == '__main__':
    main()
