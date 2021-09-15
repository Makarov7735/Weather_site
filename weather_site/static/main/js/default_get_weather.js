
function getWeather(city, ell) {
    let request = new XMLHttpRequest();
    request.open('GET', `http://${document.domain}:8000/api?city=${city}`);
    request.send();
    request.addEventListener('readystatechange', function () {
        if (request.readyState === 4 && request.status == 200) {
            let data = JSON.parse(request.response);
            let block = ell.parentElement;
            block.firstElementChild.setAttribute('src', data.icon);
            block.children[2].innerHTML = `${data.temp}°`;
        }
    });
}

function main() {
    let citys = document.querySelectorAll('.last-searched-city-name');

    for (let i of citys) {
        getWeather(i.innerHTML, i);
    }
}

main();
// let reloadData = setInterval(main, 60000);