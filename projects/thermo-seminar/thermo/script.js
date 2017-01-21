
document.addEventListener("DOMContentLoaded", function() {
    var xmlhttp = new XMLHttpRequest();
    var url = "http://localhost:5000/entries";

    xmlhttp.onreadystatechange = function() {
        if (this.readyState == 4 && this.status == 200) {
            response = JSON.parse(this.responseText);            
            renderData(response.data);
        }
    };
    xmlhttp.open("GET", url, true);
    xmlhttp.send();
});

function renderData(data) {
    
    var temp = document.getElementById('temp');    

    data.forEach(function(item) {
        console.log(item)
        
        var celsius = document.createElement('p');
        var fahrenheit = document.createElement('p');
        var datetime = document.createElement('p');

        celsius.textContent = item.celsius;
        fahrenheit.textContent = item.fahrenheit;
        datetime.textContent = item.datetime;
        
        temp.append(celsius)
        temp.append(fahrenheit)
        temp.append(datetime)
    })
}
