var botonLeerMas = document.getElementById("botonLeerMas");
var textoOculto = document.getElementById("oculto");

textoOculto.addEventListener("show.bs.collapse", function () {
    botonLeerMas.innerHTML = "Leer menos";
});

textoOculto.addEventListener("hide.bs.collapse", function () {
    botonLeerMas.innerHTML = "Leer más";
});