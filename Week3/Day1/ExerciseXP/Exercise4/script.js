const allBooks = []

const book1 = {
    title: "lorem ipsum",
    author: "lorem ipsum",
    image : "https://picsum.photos/200",
    alreadyRead : true 

}

const book2 = {
    title: "lorem ipsum",
    author: "lorem ipsum",
    image : "https://picsum.photos/200",
    alreadyRead : false
    
}

allBooks.push(book1)
allBooks.push(book2)

console.log("allBooks", allBooks);

const table = document.createElement("table")
table.innerHTML = `
<thread>
    <tr>
      <th colspan="3">my book list</th>
    </tr>
</thread>
    <tbody>
    <tr>
        <td>${book1.title} written by ${book1.author}</td>
        <td>
        <img src="${book1.image}"/>
        </td>
        <td class="read" >already read: ${book1.alreadyRead}</td>
    <tr/>
    <tr>
    <td>${book2.title} written by ${book2.author}</td>
    <td>
    <img src="${book2.image}"/>
    </td>
    <td>already read: ${book2.alreadyRead}</td>
<tr/>
    </tbody>
`

const bookListDiv = document.querySelector(".listbooks")
console.log(bookListDiv);
bookListDiv.appendChild(table)