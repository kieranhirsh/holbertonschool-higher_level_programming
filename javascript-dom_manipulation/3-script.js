document.getElementById("toggle_header").onclick = toggleClass;

function toggleClass() {
  if (document.querySelector('header').classList.contains("red")) {
    document.querySelector('header').classList.replace("red", "green")
  } else if (document.querySelector('header').classList.contains("green")) {
    document.querySelector('header').classList.replace("green", "red")
  }
}
