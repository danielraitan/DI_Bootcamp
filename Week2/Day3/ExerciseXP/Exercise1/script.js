const people = ["Greg", "Mary", "Devon", "James"];

people.shift(); 

people.splice(2,1,"Jason")

people.push("Daniel")
console.log(people);

let index = people.indexOf("Mary");
console.log(index);

console.log(people.slice(1,3));

let index2 = people.indexOf("foo");
console.log(index2);

let last = people[3]
console.log(last);

for (const friend of people) {
   console.log("this is" , friend);
   if (friend === "Devon") { break }
   
}




