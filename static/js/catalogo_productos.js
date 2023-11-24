var productos = []

fetch('/lista_productos')
.then(resp => resp.json())
.then(data => {

    productos=data;

    mostrar_productos();

    document.querySelectorAll('a[name="boton_agregar_carrito"]').forEach(boton => {
        boton.addEventListener('click',mostrar_num_carrito);
    })
})


document.getElementById("buscador").addEventListener("keyup", function () {
    let texto_ingresado = document.getElementById("buscador").value;

    filtro_busqueda = productos.filter(function (a) {
        if (a.nombre.toUpperCase().includes(texto_ingresado.toUpperCase())) {
            document.getElementById(a.id).style.display = "block";

        }else{
            document.getElementById(a.id).style.display = "none";
        }
    })

});

function mostrar_productos() {

    for (var i = 0; i < productos.length; i++) {

        document.getElementById('catalogo_productos').innerHTML += `
        <div class="col pb-3 carta_producto" id="${productos[i].id}" data-mascota= ${productos[i].mascota} data-categoria= ${productos[i].categoria}>
                <div class="card h-100 text-center shadow">
                    <a href="datos_producto/${productos[i].id}">
                        <img src="/static/img/${productos[i].imagen}" class="card-img-top img-thumbnail mx-auto d-block object-fit-contain" style="height: 300px;width: 300px;" alt=${productos[i].nombre}>
                    </a>
                    <div class="card-body">
                        <h5 class="card-title fs-3 mb-4">${productos[i].nombre}</h5>
                        <p class="card-text d-none">${productos[i].descripcion}</p>
                        <p class="card-text text-primary fw-bold fs-4">
                            <span>S/. </span>
                            <span>${productos[i].precio}</span>
                        </p>
                        <a class="btn btn-primary rounded-5 w-75" name="boton_agregar_carrito" onclick="agregar_carrito(${productos[i].id});">Agregar al carrito</a>
                    </div>
                </div>
            </div>
        `
    }
}


function filtrar_productos_mascota() {

    var checkboxes_mascota = document.querySelectorAll('input[name="check_mascota"]');
    var todos_seleccionados = true;

    checkboxes_mascota.forEach(checkbox => {
        var mascota = checkbox.id;
        var checked = checkbox.checked;

        if(checked){
            todos_seleccionados = false;
        }

        var cartas_productos = document.querySelectorAll('.carta_producto[data-mascota="'+ mascota +'"]');

        cartas_productos.forEach(div => {
            if (checked==false){
                div.style.display = "none";
            }else{
                div.style.display = "block";
            }
        });
    });

    if (todos_seleccionados){
        var a = document.querySelectorAll('.carta_producto');

        a.forEach(div => {
            div.style.display = 'block';
        });
    }

}


function filtrar_productos_categoria() {
    var checkboxes_categoria = document.querySelectorAll('input[name="check_categoria"]');
    var todos_seleccionados = true;

    checkboxes_categoria.forEach(checkbox => {
        var categoria = checkbox.id;
        var checked = checkbox.checked;

        if(checked){
            todos_seleccionados = false;
        }

        var cartas_productos = document.querySelectorAll('.carta_producto[data-categoria="'+ categoria +'"]');

        cartas_productos.forEach(div => {
            if (checked==false){
                div.style.display = "none";
            }else{
                div.style.display = "block";
            }
        });
    });

    if (todos_seleccionados){
        var a = document.querySelectorAll('.carta_producto');

        a.forEach(div => {
            div.style.display = 'block';
        });
    }
}


function limpiar(){
    var checkboxes = document.querySelectorAll('.form-check-input');
    checkboxes.forEach(checkbox =>{
        checkbox.checked = false;
    });
    var cartas = document.querySelectorAll('.carta_producto');
    cartas.forEach(cart =>{
        cart.style.display = 'block';
    });

}

function agregar_carrito(id){
    for (var i=0; i<productos.length; i++){
        datos_producto = productos[i];
        if (id==datos_producto.id){
            // Obtener la información del producto que se desea agregar al carrito
            var imagenProducto = `./static/img/${datos_producto.imagen}`;
            var nombreProducto = datos_producto.nombre;
            var precioProducto = parseFloat(datos_producto.precio);
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
            /* var numcarrito = localStorage.getItem("carrito");
            var numcarritoJson = JSON.parse(numcarrito);
            document.getElementById("numCarrito").innerHTML=numcarritoJson.length; */

                }
    }

}

function mostrar_num_carrito(event){
    var numcarrito = localStorage.getItem("carrito");
    var numcarritoJson = JSON.parse(numcarrito);
    document.getElementById("numCarrito").innerHTML=numcarritoJson.length;
}


