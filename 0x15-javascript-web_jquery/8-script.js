$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', function (body) {
  body.results.forEach(function (movie) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  });
});
