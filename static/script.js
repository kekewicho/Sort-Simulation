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
                simulation(response.states, response.time_elapsed)
            }
    });
}

function simulation(states, time) {
    const area = document.getElementById('results');
    const areaform = document.getElementById('formContainer');
    const chart = document.getElementById('chart');
    const algoSelector = document.getElementById('algoritmoSelector');
    const timeText = document.getElementById('timeElapsed');

    timeText.style.display=''
    timeText.innerHTML=`Tiempo de ejecución: ${time} segundos`

    algoSelector.style.display='none';
    area.style.display = '';
    areaform.style.display = 'none';

    const config = {
        type: 'bar',
        data: {
            labels: states[0],
            datasets: [{
                data: states[0]
            }]
        },
        options:{
            plugins:{
                legend:{
                    display:false
                },
                tooltip:{
                    enabled:false
                }
            },
            scales:{
                x: {
                    ticks: {
                      font: {
                        size: 15,
                        weight:'bold'
                      }
                    }
                  }
            }
        }
    };

    var chartvar = new Chart(chart, config);
    chartvar.update();

    states.slice(1).forEach((state, index) => {
        setTimeout(() => {
    
            // Actualización de datos del gráfico
            chartvar.data.datasets[0].data = state;
            chartvar.data.labels = state;
            chartvar.update();
        }, index==0?3000:1000 * (index + 1)); // Se aplica un retraso progresivo a cada alerta
    });
    
}