def solution(bandage, health, attacks):
    answer,a,b_t,time = 0,0,1,0
    max_t=attacks[-1][0]
    max_h=health
    while time<=max_t:
        if time==attacks[a][0]:
            health-=attacks[a][1]
            b_t=1
            time+=1
            a+=1
        else:
            if b_t==bandage[0]:
                health+=(bandage[1]+bandage[2])
                b_t=1
            else:
                health+=bandage[1]
            b_t+=1
            time+=1
        if health>=max_h: health=max_h
        if health<=0: return -1  
    return health