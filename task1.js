let readline = require('readline')
process.stdin.setEncoding('utf-8')

const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
    terminal:false
  });

let inputCount = null;
let numbers = []

rl.on('line',(line)=>{
    line = line.trim()
    if(inputCount===null){
        inputCount = parseInt(line,10)


        if(isNaN(inputCount) || inputCount<=0){
            console.log('null')
            process.exit()
        } 
    } else {
        numbers = line.split(' ').map(num=>parseInt(num,10)).filter(num=>!isNaN(num))
        if(numbers.length!=inputCount){
            console.log('null')
            process.exit()
        } else {
            
            let maxProduct = maxProductPairwise(numbers)
            console.log(maxProduct)
            process.exit()
        }
    } 
})

const maxProductPairwise =(num)=>{
    let max2= -Infinity
    let max1= -Infinity
    for(let i =0;i<inputCount;i++){
        if(num[i]>max2){
            max1=max2
            max2=numbers[i]
        } else if(num[i]>max1){
            max1=numbers[i]
        }
    }
   return max1*max2

}