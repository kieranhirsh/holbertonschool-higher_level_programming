document.getElementById("add_item").onclick = addItem;

function addItem() {
  let ul = document.querySelector("ul.my_list");
  let li = document.createElement("li");
  li.appendChild(document.createTextNode("Item"));
  ul.appendChild(li);
}
