(() => {
    'use strict'
  
    const forms = document.querySelectorAll('.needs-validation')
  
    Array.from(forms).forEach(form => {
      form.addEventListener('submit', event => {
        if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
        }
  
        form.classList.add('was-validated')
      }, false)
    })
  })()

  $(document).ready(function(){
    $(".prueba").blur(function(){
      $("#prue").hide();
    });

    $(".prueba").focus(function(){
      $("#prue").show();
    });
    
    $("#envio").click(function(){
      alert("Se estan enviando los datos. ");
    });
  });
  
  $(document).ready(function(){
    $("#boton").click(function convertir(){
      /*
        var myHeaders = new Headers();
        myHeaders.append("apikey", "aLrg0fHteOAuBGetI72VtEgn7QEfBbgW");
    
        var requestOptions = {
          method: 'GET',
          redirect: 'follow',
          headers: myHeaders
        };
    
        fetch("https://api.apilayer.com/fixer/convert?to="+hacia+"&from="+desde+"&amount="+cantidad+"", requestOptions)
        .then(response => response.text())
        .then(result => console.log(result))
        .catch(error => console.log('error', error));
        var resultado = result
        
      });*/
      var ha = document.getElementById("ha");
      var de = document.getElementById("de");
      var ca = document.getElementById("ca");
      
      var cantidad = ca.value;
      var desde = de.value;
      var hacia = ha.value;

      var settings = {
          "url": "https://api.apilayer.com/fixer/convert?from="+desde+"&amount="+cantidad+"&apikey=aLrg0fHteOAuBGetI72VtEgn7QEfBbgW&to="+hacia+"",
            "method": "GET",
            "timeout": 0,
          };
          
        $.ajax(settings).done(function (response) {
          console.log(response);
          var numero_con_decimales = response.result;
          var respuesta = Math.floor(numero_con_decimales);
          $("#resultado").append("La cantidad de " +cantidad+ " en " +desde+ " hacia " +hacia+ " es de " +respuesta+ "");
      });
  });
});

