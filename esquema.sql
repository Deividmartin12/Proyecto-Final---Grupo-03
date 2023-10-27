create table cliente(
	cliente_id bigint unsigned not null auto_increment primary key,
    nombre varchar(255) not null,
    email varchar(255) not null,
    telefono varchar(20) not null,
    direccion varchar(255) not null,
    cliente_dni char(8) unique not null,
    password varchar(255) not null
);


--CAMBIOS CABALLERO
create table categoria(
	categoria_id bigint unsigned not null auto_increment primary key,
    nombre varchar(255) not null,
    descripcion varchar(255) not null
);

create table mascota(
    mascota_id bigint unsigned not null auto_increment primary key,
    nombre varchar(255) not null
); 

create table producto(
	producto_id bigint unsigned not null auto_increment primary key,
    nombre varchar(255) not null,
    descripcion varchar(255) not null,
    precio numeric(8,2) not null,
    stock integer not null,
    estado boolean not null,
    categoria_id bigint unsigned not null,
    mascota_id bigint unsigned not null,
    link_imagen varchar(255) not null,
    constraint fk_categoria foreign key (categoria_id) references categoria(categoria_id),
    constraint fk_mascota foreign key (mascota_id) references mascota(mascota_id)
);

INSERT INTO mascota(nombre) VALUES ('Genérico');
INSERT INTO mascota(nombre) VALUES ('Perro');
INSERT INTO mascota(nombre) VALUES ('Gato');

INSERT INTO categoria(nombre, descripcion) VALUES ('Alimento','Productos para el consumo animal');
INSERT INTO categoria(nombre, descripcion) VALUES ('Limpieza','Productos para el aseo animal');
INSERT INTO categoria(nombre, descripcion) VALUES ('Juguete','Productos para el entretenimiento animal');

--CAMBIOS CABALLERO FIN

create table pedido(
	pedido_id bigint unsigned not null auto_increment primary key,
    fecha_pedido date not null,
    estado_pedido char(1) not null,
    cliente_id bigint unsigned not null,
    constraint fk_cliente foreign key (cliente_id) references cliente(cliente_id)
);

create table detalle_pedido(
	pedido_id bigint unsigned not null,
    producto_id bigint unsigned not null,
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

CREATE TABLE comprobante(
    numero_boleta BIGINT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
    fecha_hora_emision TIMESTAMP NOT NULL,
    monto_total NUMERIC(8,2) NOT NULL,
    tipo_comprobante CHAR(1) NOT NULL,
    pedido_id BIGINT UNSIGNED NOT NULL,
    metodo_id BIGINT UNSIGNED NOT NULL,
    FOREIGN KEY (pedido_id) REFERENCES pedido(pedido_id),
    FOREIGN KEY (metodo_id) REFERENCES metodo_pago(metodo_id)
);


