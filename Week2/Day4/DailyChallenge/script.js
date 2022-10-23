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

////////////////////*****************************CHECKER

SAMPLE CODE TRY THIS

const promptInput = prompt("Enter comma separated words");
const words = promptInput.split(",");
function findLongestWord() {
    //find the longest word
    let max = 0;
    for (let i = 0; i < words.length; i++) {
        if (words[i].length > max) {
            max = words[i].length;
        }
    }
    return max;
}
function printWords(words,max) {
    firstAndLast(max);
    for (let word of words) {
        console.log(`* ${word + ' '.repeat(max - word.length)} *`);
    }
    firstAndLast(max);

}
function firstAndLast(max) {
    console.log('*'.repeat(max + 4));
}
printWords(words,findLongestWord());






********************////////////////////////
 WHEN i Ran your code I got errors

