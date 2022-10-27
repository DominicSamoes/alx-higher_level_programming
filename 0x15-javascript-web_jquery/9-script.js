$('document').ready(function () {
  $.get('https://stefanbohacek.com/hellosalut/?lang=es', function (data) {
    $('DIV#hello').text(data.hello);
  });
});
