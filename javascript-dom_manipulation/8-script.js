fetch("https://hellosalut.stefanbohacek.dev/?lang=fr")
  .then(response => response.json())
  .then(data => {
    document.getElementById("hello").innerHTML = data.hello;
  })
  .catch(error => console.log(error));
