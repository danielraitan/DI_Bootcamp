hotelCost()

function hotelCost() {
    let answer

    while (!isOnlyNumber(answer)) {
        answer = prompt("how many would you like to stay?")
    }
    const numberOfNights = Number(answer)
    const costPerNight = 140
    const totalPrice = numberOfNights * costPerNight
    console.log('totalPrice:',  totalPrice);
    return totalPrice
    
}

function isOnlyNumber(str) {
    const regex = new RegExp(/^[0-9]*$/)
    return regex.test(str)
}
function includesNumbers(str) {
    const regex = new RegExp(/\d/)
    return regex.test(str)
}



function planeRideCost() {
    let destination = ""

    while (destination == null || includesNumbers(destination)){
    destination = prompt("where are you going?")
}
console.log("your destinaition is", destination);
if (destination === "london") return "183$"
if (destination === "paris") return "220$"
return "300$"
}
rentalCarCost() 
function rentalCarCost() {
    let answer

    while(!isOnlyNumber(answer)){
        answer = prompt("how many days would you like to rent a car?")
    }
    const dailyPrice = 40
    const numberOfDays = Number(answer)
    let discount = 0
    if (numberOfDays >= 10) discount = 0.05

    const totalPrice = dailyPrice * numberOfDays * (1 - discount)
    console.log("total price", totalPrice)
    return totalPrice
}

function totalVacationCost() {
    const carPrice = rentalCarCost()
    const hotelPrice = hotelCost()
    const planePrice = planeRideCost()

    console.log("hotelPrice", hotelPrice);
    console.log("carPrice", carPrice);
    console.log("planePrice", planePrice);

    const totalPrice = carPrice + hotelPrice + planePrice

    console.log("totalPrice", totalPrice);
}
totalVacationCost()