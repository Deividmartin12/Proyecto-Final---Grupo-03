create table cliente(
	cliente_id bigint unsigned not null auto_increment primary key,
    nombre varchar(255) not null,
    email varchar(255) not null,
    telefono varchar(20) not null,
    direccion varchar(255) not null,
    cliente_dni char(8) unique not null,
    password varchar(255) not null,
    token varchar(255)
);


--CAMBIOS CABALLERO
create table usuario(
	id bigint unsigned not null auto_increment primary key,
    nombres varchar(255) not null,
    apellidos varchar(255) not null,
    email varchar(255),
    telefono varchar(20),
    direccion varchar(255),
    dni char(8) unique not null,
    username varchar(100),
    password varchar(255),
    token varchar(255),
    tipo_usuario bigint unsigned not null,
    vigencia boolean not null,
    FOREIGN KEY (tipo_usuario) REFERENCES tipo_usuario(id)
);

INSERT INTO usuario(nombres,apellidos,email,telefono,direccion,dni,username,password,token,tipo_usuario)
VALUES
('Elton','Tito Ramirez',null,null,null,'98567423','admin','8c6976e5b5410415bde908bd4dee15dfb167a9c873fc4bb8a81f6f2ab448a918',null,1),
('Juan','Pérez Rodríguez','juanpr@gmail.com','658321475','Calle Chichuan #254','12345678',null,'ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f',null,2);


create table categoria(
	categoria_id bigint unsigned not null auto_increment primary key,
    nombre varchar(255) not null,
    descripcion varchar(255) not null,
    estado boolean not null
);

create table mascota(
    mascota_id bigint unsigned not null auto_increment primary key,
    nombre varchar(255) not null,
    estado boolean not null
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


