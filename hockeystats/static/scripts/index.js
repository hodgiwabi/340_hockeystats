$(document).ready(function() {
    var pathname = window.location.pathname;
    var pages = ['games', 'teams', 'players','penalties', 'infractions'];

    $('.nav-item').each(function(i) {
        var nav_item = $(this);
        if (pathname.includes(pages[i])) {
            nav_item.addClass('active');
        }
        else if (nav_item.hasClass('active')) {
            nav_item.removeClass('active');
        }
    });
});