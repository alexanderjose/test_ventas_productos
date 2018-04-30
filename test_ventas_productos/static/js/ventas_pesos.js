$(document).ready(function(){

  url_pesos = '/ventas/pesos/';

  getPesos(url_pesos);

  var datos_pesos;

  function getPesos(url){
    $.getJSON(url, {})
    .done(function( data ) {
      datos_pesos = data;
      // console.log(datos_pesos);
      graficar(datos_pesos);
      // $.each(data, function(index, element) {
      //   console.log(element);
      //   $('.grafico_ventas_unidades').append($('<div>', {
      //     // value: element.id,
      //     text: element.year + ' - ' + element.month + ' - ' + element.units
      //   }));
      // });
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para unidades: " + err );
    });
    // console.log(datos_pesos);
  }

  function graficar(datos_pesos){
    var ventas_pesos = []
    var categories_pesos = []
    $.each(datos_pesos, function(i, item) {
      // console.log(item.month);
      // console.log(item.units);
      var decimal = parseFloat(item.units);
      ventas_pesos.push(decimal)
      categories_pesos.push(item.month)
    });
    // console.log(ventas_pesos);
    // console.log(categories_pesos);
    options = {
      title: {
        text: 'Ventas por Pesos'
      },
      subtitle: {
          // text: 'Source: thesolarfoundation.com'
      },
      yAxis: {
          title: {
              text: 'MM de CLP'
          }
      },
      xAxis: {
          categories: categories_pesos
      },
      legend: {
          layout: 'vertical',
          align: 'right',
          verticalAlign: 'middle'
      },
      // plotOptions: {
      //     series: {
      //         label: {
      //             connectorAllowed: false
      //         },
      //         pointStart: 2010
      //     }
      // },
      series: [{
          name: 'Ventas por Pesos',
          data: ventas_pesos
          // data: [1.00, 2.00, 3.00, 4, 5, 6, 7, 8, 9, 10, 11, 12]
          // data: [12599760.00, 22999580.00, 22799610.00, 18999650.00, 27799550.00, 23699540.00, 19399650.00, 27499510.00, 18099680.00, 26799540.00, 26999550.00, 20899630.00]
      }],
      responsive: {
        rules: [{
          condition: {
            maxWidth: 500
          },
          chartOptions: {
            legend: {
              layout: 'horizontal',
              align: 'center',
              verticalAlign: 'bottom'
            }
          }
        }]
      }
    }
    Highcharts.chart('container_pesos', options);
  }

});
