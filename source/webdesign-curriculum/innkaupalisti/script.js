var innkaupalisti = document.getElementById('innkaupalisti');
var form = document.querySelector('form');
var textabox = form.querySelector('input');
    

form.addEventListener('submit', function(ev){
    //"use strict";
    var vara = textabox.value;

    if (!(vara == "")) {
        innkaupalisti.innerHTML += '<li>' + vara + '</li>';
        localStorage.geymsla = innkaupalisti.innerHTML;
    }

});



innkaupalisti.addEventListener('click', function(ev){
    "use strict";
    var t = ev.target;
    console.log(t)

    if (!t.classList.contains('buid')) {
        t.classList.add('buid');
    } else {
        t.parentNode.removeChild(t);
    }
    localStorage.geymsla = innkaupalisti.innerHTML;
});

if (localStorage.geymsla !== undefined) {
    innkaupalisti.innerHTML = localStorage.geymsla;
}

textabox.focus();
textabox.select();