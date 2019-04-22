function init() {
    var elements = document.getElementsByClassName('project-name');
    console.log(elements.length);
    if (elements.length != 1) {
        console.error("Number of elements is: " + elements.length);
    } else {
        var title = elements[0].innerHTML;
        console.log(title);
        elements[0].innerHTML = '<a href="/">' + title + '</a>';
    }
}

setTimeout(init, 1000);
