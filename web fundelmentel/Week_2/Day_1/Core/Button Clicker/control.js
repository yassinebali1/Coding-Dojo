function change(element){
    if ( element.innerText == "Login") {
        element.innerText = "logout";
    } else {
        element.innerText = "Login";
    }
}
function remove(element){
    element.remove()
}