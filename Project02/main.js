var dark_mode = false;
var evil_mode = false;
var evil_feature = -1;
//blue

function enable_light_mode() {
    $(document).ready(function() {
        $("p, h1, h2, h3, h4, h5, h6").css("color", "#212529");
        $("a").css("color", "#007bff");
        $(".bg-main").css("background", "#e1e1e1");
        $(".bg-main-2").css("background", "#cccccc");
        $(".bg-footer").css("background", "#bbbbbb");
        $(".bg-right-1").css("background", "#eeeeee");
        $(".bg-right-2").css("background", "#d8d8d8");
        $("#left-section").css("background", "#f6f6f6");
        $("img").css("filter", "brightness(100%)");
        $("#color-mode-toggler").html("Dark Mode");
    });
}

function enable_dark_mode() {
    $(document).ready(function() {
        $("p, h1, h2, h3, h4, h5, h6").css("color", "#CCCCCC");
        $("a").css("color", "#5cf264");
        $(".bg-main").css("background", "#444444");
        $(".bg-main-2").css("background", "#333333");
        $(".bg-footer").css("background", "#111111");
        $(".bg-right-1").css("background", "#222222");
        $(".bg-right-2").css("background", "#3A3A3A");
        $("#left-section").css("background", "#222222");
        $("img").css("filter", "brightness(40%)");
        $("#color-mode-toggler").html("Light Mode");
    });
}

function toggle_color_mode(event) {
    event.preventDefault();
    if(dark_mode) {
        enable_light_mode();
        dark_mode = 0;
    } else {
        enable_dark_mode();
        dark_mode = 1;
    }
}

function joe_hover() {
    $(document).ready(function() {
        if(evil_mode)
            good_joe();
        else
            evil_joe();
    });
}

function normal_joe() {
    $(document).ready(function() {
        $("img").attr("src", "me.png");
    });
}

function evil_joe() {
    $("img").attr("src", "badme.png");
}

function good_joe() {
    $("img").attr("src", "goodme.png");
}

function rand_int(max) {
    return (Math.floor(Math.random() * max));
}

function rand_hex_color() {
    let stuff = "0123456789ABCDEF";
    let color = "#";
    for(var i = 0; i < 6; i++)
        color += stuff[rand_int(stuff.length)];
    return color;
}

function flip_screen() {
    document.body.setAttribute("style", "-webkit-transform: rotate(180deg);");
    $("img").css("-webkit-transform", "rotate(180deg)");
}

function flip_screen_undo() {
    document.body.setAttribute("style", "-webkit-transform: rotate(0deg);");
    $("img").css("-webkit-transform", "rotate(0deg)");
}

function rand_scheme() {
    $("p, h1, h2, h3, h4, h5, h6").css("color", rand_hex_color());
    $("a").css("color", rand_hex_color());
    $(".bg-main").css("background", rand_hex_color());
    $(".bg-main-2").css("background", rand_hex_color());
    $(".bg-footer").css("background", rand_hex_color());
    $(".bg-right-1").css("background", rand_hex_color());
    $(".bg-right-2").css("background", rand_hex_color());
    $("#left-section").css("background", rand_hex_color());
    $("img").css("filter", "brightness(100%) hue-rotate(" + rand_int(360) + "deg)");
}

function rand_scheme_undo() {
    if(dark_mode)
        enable_dark_mode();
    else
        enable_light_mode();
}

function tilt() {
    document.body.setAttribute("style", "-webkit-transform: rotate(-3deg);");
}

function tilt_undo() {
    document.body.setAttribute("style", "-webkit-transform: rotate(0deg);");
}

function no_text() {
    $("p, h2, h3, h4, h5, h6, a, #links").hide();
}

function no_text_undo() {
    $("p, h2, h3, h4, h5, h6, a, #links").show();
}

function header_to_footer() {
    let header_html = $("#header").html();
    $("#header").html($("#footer").html());
    $("#footer").html(header_html);
}

function text_flip() {
    $("p, h1, h2, h3, h4, h5, h6").css("-webkit-transform", "rotate(180deg)");
}

function text_flip_undo() {
    $("p, h1, h2, h3, h4, h5, h6").css("-webkit-transform", "rotate(0deg)");
}

var fun_things = [tilt, no_text, rand_scheme, flip_screen, header_to_footer, text_flip];
var fun_things_undo = [tilt_undo, no_text_undo, rand_scheme_undo, flip_screen_undo, header_to_footer, text_flip_undo];

function do_mischief() {
    $(document).ready(function() {
        if(!evil_mode) {
            evil_mode = true;
            good_joe();
            evil_feature = rand_int(fun_things.length);
            fun_things[evil_feature]();
        } else {
            evil_mode = false;
            evil_joe();
            fun_things_undo[evil_feature]();
            evil_feature = -1;
        }
    });
}
