create table cliente(
	cliente_id serial primary key,
    nombre varchar(255) not null,
    email varchar(255) not null,
    telefono varchar(20) not null,
    direccion varchar(255) not null,
    cliente_dni char(8) unique not null,
    password varchar(255) not null
);

create table categoria(
	categoria_id serial primary key,
    nombre varchar(255) not null,
    descripcion varchar(255) not null
);

create table producto(
	producto_id serial primary key,
    nombre varchar(255) not null,
    descipcion varchar(255) not null,
    precio numeric(8,2) not null,
    stock integer not null,
    estado boolean not null,
    categoria_id integer not null,
    constraint fk_categoria foreign key (categoria_id) references categoria(categoria_id)
);
 

create table pedido(
	pedido_id serial primary key,
    fecha_pedido date not null,
    estado_pedido char(1) not null,
    cliente_id integer not null,
    constraint fk_cliente foreign key (cliente_id) references cliente(cliente_id)
);

create table detalle_pedido(
	pedido_id integer not null,
    producto_id integer not null,
    cantidad integer not null,
    precio_unitario numeric(8,2) not null,
    primary key (pedido_id, producto_id),
    constraint fk_pedido foreign key(pedido_id) references pedido(pedido_id),
    constraint fk_producto foreign key(producto_id) references producto(producto_id)
);

create table metodo_pago(
	metodo_id serial not null primary key,
    nombre varchar(255) not null unique,
    descripcion varchar(255) not null
);

create table comprobante(
	numero_boleta integer primary key,
    fecha_hora_emision timestamp not null,
    monto_total numeric(8,2) not null,
    tipo_comprobante char(1) not null,
    pedido_id integer not null,
    metodo_id integer not null,
    constraint fk_pedido foreign key (pedido_id) references pedido(pedido_id),
    constraint fk_metodo foreign key (metodo_id) references metodo_pago(metodo_id)
);