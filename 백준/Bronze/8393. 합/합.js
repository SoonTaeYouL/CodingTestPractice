const fs = require('fs');
const n = parseInt(fs.readFileSync("/dev/stdin").toString().trim());
var sum=0;
for(let i=1; i<=n; i++){
    sum+=i
};
console.log(sum);