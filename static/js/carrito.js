document.addEventListener("DOMContentLoaded", function() {
  document.querySelectorAll('a[name="boton_agregar_carrito"]').forEach(boton => {
    boton.addEventListener('click',mostrar_num_carrito);
})
    // Obtener el elemento del carrito
    var carritoElement = document.getElementById("carrito");
  
    // Obtener el carrito del almacenamiento local
    var carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    var limpiarCarritoBtn = document.getElementById("limpiarCarrito");

    limpiarCarritoBtn.addEventListener("click", function() {
      console.log("Se hizo clic en el botón limpiarCarrito");
      carrito = [];
      carritoElement.innerHTML = "Carrito vacío";
      actualizarTotal();
      localStorage.setItem("carrito", JSON.stringify([])); // Eliminar el contenido del carrito en el localStorage
      var numcarrito = localStorage.getItem("carrito");
      var numcarritoJson = JSON.parse(numcarrito);
      document.getElementById("numCarrito").innerHTML=numcarritoJson.length;
    });
  
    // Recorrer los productos en el carrito y agregarlos al DOM
    carrito.forEach(function(producto) {
      // Verificar si el producto ya está en el carrito
      var productoExistente = carritoElement.querySelector(
        '[data-nombre="' + producto.nombre + '"]'
      );
  
      if (productoExistente) {
        // Si el producto ya está en el carrito, actualizar el contador
        var cantidadElement = productoExistente.querySelector(".cantidad");
        producto.cantidad = producto.cantidad || 1;
        cantidadElement.textContent = producto.cantidad;
      } else {
        // Si el producto no está en el carrito, crear un nuevo div con la estructura deseada
        var productoDiv = document.createElement("div");
        productoDiv.classList.add("d-flex","justify-content-center","productos");
  
        // Crear la columna para la imagen del producto
        var imagenColumn = document.createElement("div");
        imagenColumn.innerHTML = '<img class="img-fluid object-fit-contain imgProCar" src="' + producto.imagen + '" alt="">';
  
        // Crear la columna para la información del producto
        var infoColumn = document.createElement("div");
        infoColumn.classList.add("d-lg-flex","d-block","align-items-center");
  
        // Crear el nombre del producto
        var nombre = document.createElement("p");
        nombre.textContent = producto.nombre;
        nombre.classList.add("texto")
  
        // Crear el precio del producto
        var precio = document.createElement("p");
        precio.textContent = "Precio: " + producto.precio.toFixed(2);
        precio.classList.add("texto")
  
        // Crear los botones de cantidad y eliminar
        var cantidadDiv = document.createElement("div");
        cantidadDiv.classList.add("d-flex", "align-items-center");
  
        var aumentarBtn = document.createElement("button");
        aumentarBtn.type = "button";
        aumentarBtn.textContent = "+";
        aumentarBtn.classList.add("btn");

        var cantidad = document.createElement("p");
        cantidad.textContent = producto.cantidad || 1;
        cantidad.classList.add("texto");
  
        var disminuirBtn = document.createElement("button");
        disminuirBtn.type = "button";
        disminuirBtn.textContent = "-";
        disminuirBtn.classList.add("btn")
  
        // Crear el botón de eliminar producto
        var eliminarBtn = document.createElement("button");
        eliminarBtn.type = "button";
        eliminarBtn.classList.add("btnDel");
        var trashIcon = document.createElement("i");
        trashIcon.classList.add("fa-solid", "fa-trash");
        eliminarBtn.appendChild(trashIcon);
  
        // Agregar los elementos al DOM
        cantidadDiv.appendChild(aumentarBtn);
        cantidadDiv.appendChild(cantidad);
        cantidadDiv.appendChild(disminuirBtn);
        cantidadDiv.appendChild(eliminarBtn);
  
        infoColumn.appendChild(nombre);
        infoColumn.appendChild(precio);
        infoColumn.appendChild(cantidadDiv);
  
        productoDiv.appendChild(imagenColumn);
        productoDiv.appendChild(infoColumn);
  
        carritoElement.appendChild(productoDiv);
  
        // Manejar el evento de clic en el botón de aumentar cantidad
        aumentarBtn.addEventListener("click", function() {
          producto.cantidad++;
          cantidad.textContent = producto.cantidad;
          actualizarTotal();
          actualizarCarritoEnLocalStorage();
        });
        
  
        // Manejar el evento de clic en el botón de disminuir cantidad
        disminuirBtn.addEventListener("click", function() {
          if (producto.cantidad > 1) {
            producto.cantidad--;
            cantidad.textContent = producto.cantidad;
            actualizarTotal();
            actualizarCarritoEnLocalStorage();
          }
        });
  
        // Manejar el evento de clic en el botón de eliminar producto
        eliminarBtn.addEventListener("click", function() {
          var index = carrito.findIndex(function(item) {
            return item.nombre === producto.nombre;
          });
          if (index !== -1) {
            carrito.splice(index, 1);
            carritoElement.removeChild(productoDiv);
            actualizarTotal();
            localStorage.setItem("carrito", JSON.stringify(carrito));
          }
        });
      }
    });
  
    // Función para actualizar el total del carrito
    function actualizarTotal() {
      // Calcular el total
      var total = 0;
      carrito.forEach(function(producto) {
        total += producto.precio * producto.cantidad;

      localStorage.setItem("totalCarrito", total.toFixed(2));
      });

      // Actualizar el total en el DOM
      var totalElement = document.getElementById("total");
      var subTotalElement = document.getElementById("subtotal"); 
      subTotalElement.textContent = "S/. " + total.toFixed(2);
      totalElement.textContent = "S/. " + total.toFixed(2);
    }

    function actualizarCarritoEnLocalStorage() {
      localStorage.setItem("carrito", JSON.stringify(carrito));
    }
  
    // Actualizar el total al cargar la página
    actualizarTotal();
  });

  function mostrar_num_carrito(event){
    var numcarrito = localStorage.getItem("carrito");
    var numcarritoJson = JSON.parse(numcarrito);
    document.getElementById("numCarrito").innerHTML=numcarritoJson.length;
}