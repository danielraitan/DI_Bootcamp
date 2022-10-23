let answer = prompt("choose a number")

function song() {
    for (let i = 1; i < answer; i++) {
        let result = answer - i
        let it = "it"
        console.log(`${answer} bottles of beer on the wall ${answer} bottles of beer `);
        console.log(`take ${i} down toss around now theres ${result} bottles of beer on the wall`);

        if (answer > result) {
           answer -= i
        }
    } 
}
song()

let end = "no bottle of beer on the wall"
console.log(end);