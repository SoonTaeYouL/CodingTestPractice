function solution(bandage, health, attacks) {
    var cnt = 0;
    // 마지막 공격까지의 시간
    for(var i = 0; i < attacks.length; i++){
        var attack = attacks[i];
        if(cnt < attack[0]){
            cnt = attack[0];    
        }console.log(cnt);     
    }
    
    var health_now = health; // 현재 체력
    var bandage_time = 1; // 붕대감기 시간
    var at_t = 0; // 공격할 시간
    
    // 마지막 공격까지의 1초마다의 반복문
    for(var i = 0; i <= cnt; i++){
        console.log("time: ",i);
        if (i == attacks[at_t][0]){ // 공격할 시간
            health_now -= attacks[at_t][1];
            bandage_time = 1;
            at_t++;
        }else{
            if(bandage_time == bandage[0]){ // 붕대감기 시간이 연속 붕대감
                health_now += (bandage[2] + bandage[1]);
                bandage_time = 1;
            }else{
                health_now += bandage[1];
                bandage_time++;
            }
            if(health_now >= health){
                health_now = health;
            } 
        }
        console.log(health_now);
        if(health_now <= 0){
            return -1;
            break;
        }
    } 
    return health_now;
}
