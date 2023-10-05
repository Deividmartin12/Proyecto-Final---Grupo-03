var eliminarTodo = document.getElementById("comprarAhora");

eliminarTodo.addEventListener("click", function() {
  carrito = [];
  localStorage.setItem("carrito", JSON.stringify([])); // Eliminar el contenido del carrito en el localStorage
  localStorage.setItem("totalCarrito", "0.0"); // Establecer el total en 0.0 en el localStorage
});
