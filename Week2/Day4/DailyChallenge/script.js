const answer = prompt("type words separated by commas");

const words = answer.split(",")
 
const lengthOfLongestWord = getLengthOfLongestword();

displayRows();

function displayRows() {
    const delimiterRow = createDelimiterRow();
    console.log(delimiterRow);
    for (const word of words){
        displayWord(word);
    }
    console.log(delimiterRow);
}

function displayWord(word) {
    const numberOfSpacesToAdd = lengthOfLongestWord - word.length + 1;
    const emptySpaces = " ".repeat(numberOfSpacesToAdd);
    console.log("* " + word + emptySpaces + "*");
}
 
function getLengthOfLongestword() {
    for (const word of words) {
        const wordLength = word.length;
        if (wordLength > lengthOfLongestWord) {
            lengthOfLongestWord = wordLength;
        }
    }
    return lengthOfLongestWord;
}
function createDelimiterRow() {
    const numberOfStarsOnFirstRow = lengthOfLongestWord + 4;

    let row = "";
    for (let i = 0; i < numberOfStarsOnFirstRow; i++) {
        row = row + "*";
    }
    return row;
}



