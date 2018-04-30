$(document).ready(function(){

  url_costos = '/ventas/costos/';

  getCostos(url_costos);

  var datos_costos;

  function getCostos(url){
    $.getJSON(url, {})
    .done(function( data ) {
      datos_costos = data;
      // console.log(datos_costos);
      graficar(datos_costos);
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
    // console.log(datos_costos);
  }

  function graficar(datos_costos){
    var ventas_costos = []
    var categories_costos = []
    $.each(datos_costos, function(i, item) {
      // console.log(item.month);
      // console.log(item.units);
      var decimal = parseFloat(item.units);
      ventas_costos.push(decimal)
      categories_costos.push(item.month)
    });
    // console.log(ventas_costos);
    // console.log(categories_costos);
    options = {
      title: {
        text: 'Ventas por Costos'
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
          categories: categories_costos
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
          name: 'Ventas por Costos',
          data: ventas_costos
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
    Highcharts.chart('container_costos', options);
  }

});
