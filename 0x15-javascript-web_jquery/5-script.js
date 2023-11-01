$(document).ready(function () {
  $('#add_item').click(function () {
     let newListItem = $('<li>Item</li>');

     $('.my_list').append(newListItem);
  });
});
