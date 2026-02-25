def main():
    listUang = [50, 25, 10, 5, 1]

    uangTarget = int(input())
        
    total_lembar = 0

    for pecahan in listUang:
        if uangTarget == 0:
            break
            
        lembar = uangTarget // pecahan
        total_lembar += lembar
        
        uangTarget %= pecahan
    
    print(total_lembar)

main()