let stars = ["*", "* *", "* * *", "* * * *", "* * * * *", "* * * * * *"];
// console.log(stars[0]);
// console.log(stars[1]);
// console.log(stars[2]);
// console.log(stars[3]);
// console.log(stars[4]);
// console.log(stars[5]);

for (let i = 0; i <= 5; i++) {
    console.log(stars[i]);
  }


  
  const max = 6

for (let r = 0;r < max; r++){
    const number = r + 1
    let line = ""
 for (let t = 0;t < number;t++) {
    line = line + " * "; 
}
   console.log(line); 
}



