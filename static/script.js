var numberField='<input type="number" class="form-control inputNum" style="width:70px; margin-right: 10px;">'

function setNumberQty(Qty) {
    area=document.getElementById('numbersWrapper');

    area.innerHTML='';

    fields=numberField.repeat(Qty)

    area.innerHTML=fields
}

function getOrdenamiento(random) {
    algoritmo=document.getElementById('algoritmoSelector').value
    numbers=[]

    if (!random) {
        const num=document.getElementsByClassName('inputNum')
        Array.from(num).forEach(element => {
            numbers.push(element.value)
        });   
    }

    $.ajax({
        url: '/ordenar',
            type: 'POST',
            contentType: 'application/json',
            data: JSON.stringify({
                'algoritmo': algoritmo,
                'randomState':random,
                'numbers':numbers
            }),
            success: function (response) {
                console.debug(response.states)
                simulation(response.states)
            }
    });
}

function simulation(states) {
    const area=document.getElementById('results');
    const areaform=document.getElementById('formContainer');
    const chart=document.getElementById('chart');

    area.style.display=''
    areaform.style.display='none'

    const config = {
        type: 'bar',
        data: {
            datasets: [{
                barThickness: 6,
                maxBarThickness: 8,
                minBarLength: 2,
                data: states[0]
            }]
        },
        options: {
          scales: {
            y: {
              beginAtZero: true
            }
          }
        },
      };

    var chartvar=new Chart(chart,config);
    chartvar.update()
}