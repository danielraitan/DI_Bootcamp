
function changeEnough(itemPrice, amountOfChange) {
    console.log("the price is", itemPrice);
    const sum = calculateSum(amountOfChange)
    return (sum > itemPrice)
}
 function calculateSum(arr) {
    let sum = 0

    for (let i = 0; i < arr.length; i++) {
        let coinValue
        const numberOfCoins = arr[i]
        if(i === 0){coinValue = 0.25}
        if(i === 1){coinValue = 0.10}
        if(i === 2){coinValue = 0.05}
        if(i === 3){coinValue = 0.01}
        console.log("we have ", numberOfCoins, "coins that have a value of ", coinValue);
        sum = sum + numberOfCoins * coinValue
    }
    console.log("you own ", sum);

    return sum
 }

changeEnough(4, 3) 
changeEnough(4.25, [25, 20, 5, 0])