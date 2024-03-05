create table tb_usuario(
	cod_usuario serial primary key,
	login varchar (200) not null,
	senha varchar(200) not null
);

insert into tb_usuario(login,senha) values 
('admin', 'admin'),
('joao', '123456');

select * from tb_usuario;