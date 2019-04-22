function init() {
    var h1s = document.getElementsByName('h1');
    console.log(h1s.length);
    if (h1s.length != 1) {
        console.error("Number of h1 tags is: " + h1s.length);
    } else {
        var title = h1s[0].innerHTML;
        console.log(title);
        h1s[0].innerHTML = '<a href="/">' + title + '</a>';
    }
}

init();
