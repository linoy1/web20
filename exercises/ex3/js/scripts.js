var firstName = "Linoy";
var lastName = "Simantov";
var i;

function doBox() {
    var articles = "";

    for (i = 0; i < firstName.length * lastName.length; i++) {
        articles += "<article></article>";
    }

    document.getElementsByTagName("main")[0].innerHTML = articles;

}