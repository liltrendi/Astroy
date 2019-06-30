$('#password, #confirmPassword').on('keyup', function () {
  if ($('#password').val() == $('#confirmPassword').val()) {
    $('#message').html('Your passwords currently match!').css('color', 'green');
  } else 
    $('#message').html('Your passwords do not match!').css('color', 'red');
});
