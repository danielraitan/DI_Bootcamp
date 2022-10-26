setTimeout(timeOut, 2000)

function timeOut() {
    alert("hello world")
}

setTimeout(addPara, 2000)

function addPara() {
    const para = document.createElement("p");
    const node = document.createTextNode("Hello World");
    para.appendChild(node);

    const element = document.getElementById("container");
    element.appendChild(para);
}

const interval = setInterval(addParagraphs, 2000)

function addParagraphs() {
    const para = document.createElement("p");
    const node = document.createTextNode("Hello World");
    para.appendChild(node);

    const element = document.getElementById("container");
    element.appendChild(para);
}

const button = document.getElementById("clear")

button.addEventListener("click", stop);

function stop(event){
    console.log(event.target); 
    console.log(event.target.textContent);

    clearInterval(interval);
}
