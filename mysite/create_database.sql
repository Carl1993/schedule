drop database if exists mysite;
create database mysite;
use mysite;

# drop tables if exists attendence, on_duty, usr;
create table usr (
	usr_id		varchar(32)		not null,
	usr_type	integer(4)		not null,
	usr_name	varchar(40),
	primary key	(usr_id)
);
# 0 admin, 1 doctor, 2 nurse, 3 patient, >=4 visitor
/*
insert into usr values
('ming', 0, 'liuming'),
('doctor1', 1, 'zhaojishuang1'),
('doctor2', 1, 'zhaojishuang2'),
('nurse1', 2, 'zhangfan1'),
('nurse2', 2, 'zhangfan2');
*/
create table attendence(
	usr_id		varchar(32)		not null,
	foreign key (usr_id) references usr(usr_id),
    op_date		date			not null,
    op_time		time			not null,
    in_out		bool			not null
);
/*
insert into attendence values
	('doctor1', current_date(), current_time(), true),
    ('doctor1', current_date(), '7:3:2', false);
*/
create table on_duty(
	usr_id		varchar(32)		not null,
	foreign key (usr_id) references usr(usr_id),
    od_date		date			not null,
    start_time	time			not null,
    end_time	time			not null
);
/*usr
insert into on_duty values
	('doctor1', current_date(), '08:00:00', '17:00:00');
*/
use mysite;