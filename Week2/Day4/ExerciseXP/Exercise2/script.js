function calculateTip() {
    let answer = prompt("how much is the bill")
    console.log(answer);

    if (answer < 50 ) {
        tip = 0.2
        
    }
    else if (answer > 50 && answer < 200){
        tip = 0.15
    }
    else if (answer > 200){
        tip = 0.1
    }

    let total = answer * (1 + tip)
    console.log(total);

}
calculateTip()