drop table if exists entries;
create table entries(
 id int primary key auto_increment,
 title text not null,
 'text' text not null
);