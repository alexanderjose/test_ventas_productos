$(document).ready(function(){

  url_unidades = '/ventas/unidades/';

  getUnidades(url_unidades);

  var datos;

  function getUnidades(url){
    $.getJSON(url, {})
    .done(function( data ) {
      datos = data;
      graficar(datos);
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
    // console.log(datos);
  }

  function graficar(datos){
    var ventas = []
    var categories = []
    $.each(datos, function(i, item) {
      ventas.push(item.units)
      categories.push(item.month)
    });
    // console.log(ventas);
    options = {
      title: {
        text: 'Ventas por Unidades'
      },
      subtitle: {
          // text: 'Source: thesolarfoundation.com'
      },
      yAxis: {
          title: {
              text: 'Unidades'
          }
      },
      xAxis: {
          categories: categories
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
          name: 'Ventas por Unidades',
          data: ventas
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
    Highcharts.chart('container_unidades', options);
  }

});
