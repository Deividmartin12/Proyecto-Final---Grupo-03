document.addEventListener("DOMContentLoaded", function() {
    // Obtener el contenedor de los elementos del carrito
    var carritoElementos = document.getElementById("carritoElementos");
  
    // Obtener el carrito del almacenamiento local
    var carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    var total = parseFloat(localStorage.getItem("totalCarrito")) || 0.0;
  
    // Generar el HTML para cada elemento del carrito
    carrito.forEach(function(producto) {
      // Crear el div contenedor para el elemento del carrito
      var elementoDiv = document.createElement("div");
      elementoDiv.classList.add("row");
  
      // Crear la columna para la imagen del producto
      var imagenColumn = document.createElement("div");
      imagenColumn.classList.add("col");
      var imagen = document.createElement("img");
      imagen.src = producto.imagen;
      imagen.classList.add("img-thumbnail");
      imagen.alt = "img";
      imagen.width = 100;
      imagen.height = 100;
      imagenColumn.appendChild(imagen);
  
      // Crear la columna para la información del producto
      var infoColumn = document.createElement("div");
      infoColumn.classList.add("col");
      var nombre = document.createElement("strong");
      nombre.textContent = producto.nombre;
      var cantidad = document.createElement("div");
      cantidad.textContent = "Cantidad: " + producto.cantidad;
      infoColumn.appendChild(nombre);
      infoColumn.appendChild(document.createElement("br"));
      infoColumn.appendChild(cantidad);
  
      // Crear la columna para el precio del producto
      var precioColumn = document.createElement("div");
      precioColumn.classList.add("col");
      precioColumn.textContent = "S/. " + producto.precio.toFixed(2);
  
      // Agregar las columnas al div contenedor
      elementoDiv.appendChild(imagenColumn);
      elementoDiv.appendChild(infoColumn);
      elementoDiv.appendChild(precioColumn);
  
      // Agregar el elemento del carrito al contenedor en el DOM
      carritoElementos.appendChild(elementoDiv);

      // Actualizar el total en el DOM
      var totalElement = document.getElementById("subtotal");
      totalElement.textContent = "S/. " + total.toFixed(2);

      var envio = 15;

      var gastosEnvio = document.getElementById("gastosEnvio");
      gastosEnvio.textContent = "S/. " +  envio;
      
      var totalPago = document.getElementById("totalPago");
      totalPago.textContent = "S/. " +(envio + total);

    });
  });
  