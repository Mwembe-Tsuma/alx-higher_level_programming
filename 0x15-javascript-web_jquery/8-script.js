$(document).ready(function () {
  // Make an AJAX GET request to the URL
  $.ajax({
    type: 'GET',
    url: 'https://swapi-api.alx-tools.com/api/films/?format=json',
    success: function (data) {
      let movieTitles = data.results;

      let listElement = $('#list_movies');

      $.each(movieTitles, function (index, movie) {
        listElement.append('<li>' + movie.title + '</li>');
      });
    },
    error: function () {
      $('#list_movies').text("Error fetching movie titles");
    }
  });
});
