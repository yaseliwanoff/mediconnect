$('.form-input input').on('focus', function() {
    $(this).addClass('active');
});

$('.form-input input').on('blur', function() {
    if (!$(this).val()) {
        $(this).removeClass('active');
    }
});
