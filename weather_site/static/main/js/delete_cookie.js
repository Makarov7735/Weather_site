function delete_cookie(event) {
    let request = new XMLHttpRequest();
    let city = event.currentTarget.parentElement.children[1].innerHTML;
    let element = event.currentTarget;
    request.open('GET', `http://${document.domain}:8000/api?deletecookie=${city}`);
    request.send();
    request.addEventListener('readystatechange', function () {
        if (request.readyState === 4 && request.status == 200) {
            element.parentElement.parentNode.removeChild(element.parentElement);
            if (!document.querySelectorAll('.last-searched-citys').length) {
                let content = document.querySelector('.content');
                content.innerHTML = '<p id="welcome_text">Welcome to www.weatheranywhere.space.<br>Here you can find out a forecast in your or any other city.</p><img src="/static/main/icons/logo.png" id="logo2">'
            }
        }
    });
    event.preventDefault();
}

//let delete_buttons = document.querySelectorAll('.last-searched-city-delete');

//for (let i of delete_buttons) {
//    i.onclick = delete_cookie;
//}