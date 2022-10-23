function playTheGame() {
    let answer = prompt("would you like to play the game?")
    if (answer === "false") {
        alert("No problem, Goodbye")
    }
    if (answer === "true") {
        trueAnswer()
    }
    
}

function trueAnswer() {
    let userNumber = prompt("enter number between 0-10")
    
    let numberCheck = isNaN(userNumber);
        
        if (numberCheck == true){
            alert("Not a number, goodbye")
        }
   
        else if (userNumber < 0 || userNumber > 10){
            alert("Sorry its not a good number, Goodbye")
        }
       
        if (userNumber >= 0 && userNumber <= 10) {
        
        let computerNumber = Math.floor((Math.random() * 10))
         compareNumbers(userNumber, computerNumber)
        
        }
        
} 

function compareNumbers(user, computer) {
    console.log(user, computer);
    let index = 0;
    while (index < 3) {
        
    if (user == computer) {
        alert("WINNER")
        return
    }
    else if (user > computer) {
         alert("Your number is bigger than the computers, guess again")
        user = prompt ("choose new number")
    }
    else if(user < computer){
        alert("Your number is smaller than the computers, guess again")
        user = prompt ("choose new number")
    }
   
    if(index === 2){
        alert("too many attempts the answer is: " + computer)
    }
    index ++
}
}