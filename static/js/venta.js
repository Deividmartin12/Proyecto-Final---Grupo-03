

var carritoJSON = localStorage.getItem("carrito");

if (carritoJSON) {
  var carrito = JSON.parse(carritoJSON);

    fetch('/metodo_venta', {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(carrito),
    });

} else {
  console.log("No hay elementos en el carrito");
}

var miBoton = document.getElementById("realizar_venta");

function miFuncion() {
  console.log("¡El botón ha sido presionado!");
}

miBoton.addEventListener("click", miFuncion);