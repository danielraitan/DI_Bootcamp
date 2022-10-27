const userInput = document.querySelector("input")
const allowedChars = /[A-Za-z]/;
userInput.addEventListener("keypress", checkKey)

function checkKey(event) {
    if (!allowedChars.test(event.key)) {
        event.preventDefault();
        
    }
    
}
