document.getElementById("toggle_header").onclick = toggleClass;

function toggleClass() {
  document.querySelector('header').classList.toggle("red")
  document.querySelector('header').classList.toggle("green")
}
