const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];

let sentence = ""

 for (const name of names.sort()) {
    console.log(name)
    sentence = sentence + name[0]
 }
 
 console.log(sentence);