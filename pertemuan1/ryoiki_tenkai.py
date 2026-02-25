def main():
    stat = list(map(int, input().split()))
    enemy = list(map(int, input().split()))
    duration = int(input())

    final_attack = stat[0] + stat[1] * duration

    for i in range(stat[3]) :
        if final_attack > enemy[i] - stat[2] * duration : 
            print("LOSE")
            break

    else :
        print("WIN")
    
main()