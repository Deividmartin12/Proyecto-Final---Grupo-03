document.addEventListener("DOMContentLoaded", function() {
  // Obtener el botón "Agregar al Carrito"
  var addCarritoBtn = document.getElementById("addCarrito");
  var comprarAhora = document.getElementById("comprarAhoraID");

  // Agregar un evento de clic al botón
  addCarritoBtn.addEventListener("click", function() {
    // Obtener la información del producto que se desea agregar al carrito
    var imagenProducto = document.getElementById("imgProducto").getAttribute("src");
    var nombreProducto = document.getElementById("proTitle").textContent;
    var precioProducto = parseFloat(document.getElementById("precioPro").textContent);
    // Crear un objeto para representar el producto
    var producto = {
      imagen: imagenProducto,
      nombre: nombreProducto,
      precio: precioProducto
    };

    // Obtener el carrito del almacenamiento local o crear uno nuevo si no existe
    var carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    // Verificar si el producto ya está en el carrito
    var productoExistente = carrito.find(function(item) {
      return item.nombre === producto.nombre;
    });

    if (productoExistente) {
      // Si el producto ya está en el carrito, incrementar la cantidad
      productoExistente.cantidad++;
    } else {
      // Si el producto no está en el carrito, agregarlo con una cantidad de 1
      producto.cantidad = 1;
      carrito.push(producto);
    }

    // Guardar el carrito actualizado en el almacenamiento local
    localStorage.setItem("carrito", JSON.stringify(carrito));

  });

  comprarAhora.addEventListener("click", function() {
    // Obtener la información del producto que se desea agregar al carrito
    var imagenProducto = document.getElementById("imgProducto").getAttribute("src");
    var nombreProducto = document.getElementById("proTitle").textContent;
    var precioProducto = parseFloat(document.getElementById("precioPro").textContent);
    // Crear un objeto para representar el producto
    var producto = {
      imagen: imagenProducto,
      nombre: nombreProducto,
      precio: precioProducto
    };

    // Obtener el carrito del almacenamiento local o crear uno nuevo si no existe
    var carrito = JSON.parse(localStorage.getItem("carrito")) || [];

    // Verificar si el producto ya está en el carrito
    var productoExistente = carrito.find(function(item) {
      return item.nombre === producto.nombre;
    });

    if (productoExistente) {
      // Si el producto ya está en el carrito, incrementar la cantidad
      productoExistente.cantidad++;
    } else {
      // Si el producto no está en el carrito, agregarlo con una cantidad de 1
      producto.cantidad = 1;
      carrito.push(producto);
    }

    // Guardar el carrito actualizado en el almacenamiento local
    localStorage.setItem("carrito", JSON.stringify(carrito));

  });
});
