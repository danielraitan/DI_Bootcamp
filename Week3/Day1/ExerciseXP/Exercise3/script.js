const navbar = document.getElementById('navBar')
navbar.setAttribute("id", "socialNetworkNavigation") 
console.log(navbar);

const li = document.createElement("li")

const logout = document.createTextNode("logout")
console.log(logout);

li.appendChild(logout)
console.log(li);

const ul = navbar.firstElementChild
ul.appendChild(li)