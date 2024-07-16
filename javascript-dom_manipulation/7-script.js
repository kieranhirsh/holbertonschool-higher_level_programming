let list_movies = document.querySelector("ul#list_movies");

fetch("https://swapi-api.hbtn.io/api/films/?format=json")
  .then(response => response.json())
  .then(data => {
    for (let movie of data.results) {
      console.log(movie.title);
      let li = document.createElement("li");
      // the next line could be replaced by ...
      li.appendChild(document.createTextNode(movie.title));
      // li.textContent = movie.title;
      // ... the previous line
      list_movies.appendChild(li);
    }
  })
  .catch(error => console.log(error));