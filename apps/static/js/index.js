$(function () {
    $(".bar").click(function () {
        $(this).siblings().removeClass("_bar").addClass("bar");
        $(this).addClass("_bar").removeClass("bar");
    });
});