$(document).ready(function(){

  url_tiendas = '/ventas/tiendas/';
  url_marcas = '/ventas/marcas/';
  url_categorias = '/ventas/categorias/';
  url_subcategorias = '/ventas/subcategorias/';
  url_unidades = '/ventas/unidades/';

  getTiendas(url_tiendas);
  getMarcas(url_marcas);
  getCategorias(url_categorias);
  getSubCategorias(url_subcategorias);
  // getUnidades(url_unidades);

  $('.actualizar').click(function () {

    url_unidades = '/ventas/unidades';
    url_pesos = '/ventas/pesos';
    url_descuentos = '/ventas/descuentos';
    url_costos = '/ventas/costos';

    tienda_selected = $(".tiendas option:selected").val();
    if(tienda_selected != ''){
      url_unidades = url_unidades + '/tienda/'+tienda_selected;
      url_pesos = url_pesos + '/tienda/'+tienda_selected;
      url_descuentos = url_descuentos + '/tienda/'+tienda_selected;
      url_costos = url_costos + '/tienda/'+tienda_selected;
    }

    marca_selected = $(".marcas option:selected").val();
    if(marca_selected != ''){
      url_unidades = url_unidades + '/marca/'+marca_selected;
      url_pesos = url_pesos + '/marca/'+marca_selected;
      url_descuentos = url_descuentos + '/marca/'+marca_selected;
      url_costos = url_costos + '/marca/'+marca_selected;
    }

    $('#container_unidades').val('');
    getUnidades(url_unidades);
    $('#container_pesos').val('');
    getPesos(url_pesos);
    $('#container_descuentos').val('');
    getDescuentos(url_descuentos);
    $('#container_costos').val('');
    getCostos(url_costos);

  });


  function getTiendas(url){
    $.getJSON(url, {})
    .done(function( data ) {
      $.each(data, function(index, element) {
        // console.log(element.id);
        $('.tiendas').append($('<option>', {
          value: element.id,
          text: element.descripcion
        }));
      });
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para tiendas: " + err );
    });
  }

  function getMarcas(url){
    $.getJSON(url, {})
    .done(function( data ) {
      $.each(data, function(index, element) {
        // console.log(element.id);
        $('.marcas').append($('<option>', {
          value: element.id,
          text: element.descripcion
        }));
      });
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para marcas: " + err );
    });
  }

  function getCategorias(url){
    $.getJSON(url, {})
    .done(function( data ) {
      $.each(data, function(index, element) {
        // console.log(element.id);
        $('.categorias').append($('<option>', {
          value: element.id,
          text: element.descripcion
        }));
      });
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para categorias: " + err );
    });
  }

  function getSubCategorias(url){
    $.getJSON(url, {})
    .done(function( data ) {
      $.each(data, function(index, element) {
        // console.log(element.id);
        $('.subcategorias').append($('<option>', {
          value: element.id,
          text: element.descripcion
        }));
      });
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para subcategorias: " + err );
    });
  }

  function getUnidades(url){
    // console.log(url);
    $.getJSON(url)
    .done(function( data ) {
      datos = data;
      graficar_ventas_unidades(datos);
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para unidades: " + err );
    });
    // console.log(datos);
  }

  function getPesos(url){
    $.getJSON(url)
    .done(function( data ) {
      datos = data;
      graficar_ventas_pesos(datos);
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para unidades: " + err );
    });
    // console.log(datos);
  }

  function getDescuentos(url){
    $.getJSON(url)
    .done(function( data ) {
      datos = data;
      graficar_ventas_descuentos(datos);
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para descuentos: " + err );
    });
    // console.log(datos);
  }

  function getCostos(url){
    $.getJSON(url)
    .done(function( data ) {
      datos = data;
      graficar_ventas_costos(datos);
    })
    .fail(function( jqxhr, textStatus, error ) {
      var err = textStatus + ", " + error;
      console.log( "Peticion fallida para costos: " + err );
    });
    // console.log(datos);
  }

  function graficar_ventas_unidades(datos){
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

  function graficar_ventas_pesos(datos_pesos){
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

  function graficar_ventas_descuentos(datos_descuentos){
    var ventas_descuentos = []
    var categories_descuentos = []
    $.each(datos_descuentos, function(i, item) {
      // console.log(item.month);
      // console.log(item.units);
      var decimal = parseFloat(item.units);
      ventas_descuentos.push(decimal)
      categories_descuentos.push(item.month)
    });
    // console.log(ventas_descuentos);
    // console.log(categories_descuentos);
    options = {
      title: {
        text: 'Ventas por Descuentos'
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
          categories: categories_descuentos
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
          name: 'Ventas por Descuentos',
          data: ventas_descuentos
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
    Highcharts.chart('container_descuentos', options);
  }

  function graficar_ventas_costos(datos_costos){
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
      series: [{
          name: 'Ventas por Costos',
          data: ventas_costos
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
