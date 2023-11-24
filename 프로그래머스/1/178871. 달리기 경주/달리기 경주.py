def solution(players, callings):
    dic ={players[i] : i for i in range(len(players))}
    for i in callings:
        id = dic[i]
        players[id] , players[id-1] = players[id-1], players[id]
        dic[i] -=1
        dic[players[id]] +=1
        
    return players