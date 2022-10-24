const div = document.getElementById("container")
console.log(div);

document.querySelector(".list").children[1].textContent = "richard"

const lists = document.querySelectorAll(".list")
lists.forEach(list => list.firstElementChild.textContent = "daniel")

lists[1].children[1].remove()