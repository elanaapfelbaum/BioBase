create table enzyme(
       enzyme_name	varchar(100),
       ligand_mechanism varchar(100),
       primary key(enzyme_name));

create table intermediate(
       intermediate_name varchar(100),
       concenration	 varchar(100),
       primary key(intermediate_name));

create table location(
       organelle        varchar(100),
       substructure     varchar(100),
       primary key(organelle, substructure)); 

create table process(
       process_name varchar(100),
       goal_product varchar(100),
       primary key(process_name),
       foreign key(goal_product) references intermediate(intermediate_name));

create table condition(
       concentration	varchar(50),
       compound	        varchar(100),
       prime_location	varchar(100),
       primary key(concentration, compound),
       foreign key(compound) references intermediate(intermediate_name));

create table operates_under(
       process_name	varchar(100),
       concentration 	varchar(100),
       compound		varchar(100),
       primary key(process_name, concentration, compound),
       foreign key(process_name) references process(process_name),
       foreign key(concentration) references condition(concentration),
       foreign key(compound) references condition(compound)); 
       
create table uses(
       process_name varchar(100),
       enzyme_name  varchar(100),
       primary key(process_name, enzyme_name),
       foreign key(process_name) references process(process_name),
       foreign key(enzyme_name) references enzyme(enzyme_name));

create table located_in(
       enzyme_name varchar(100),
       organelle   varchar(100),
       substructure varchar(100),
       primary key(enzyme_name, organelle, substructure),
       foreign key(enzyme_name) references enzyme(enzyme_name),
       foreign key(organelle) references location(organelle));

create table converts(
       enzyme_name varchar(100),
       reactant_name varchar(100),
       product_name varchar(100),
       energy_compounds varchar(100),
       deltaG varchar(100),
       primary key(enzyme_name, reactant_name),
       foreign key(enzyme_name) references enzyme(enzyme_name),
       foreign key(reactant_name) references intermediate(intermediate_name),
       foreign key(product_name) references intermediate(intermediate_name));


load data local infile 'enzymedata.txt' into table enzyme fields terminated by ' | ' lines terminated by '\n';
load data local infile 'processdata.txt' into table process fields terminated by ' | ' lines terminated by '\n';
load data local infile 'intermediatedata.txt' into table intermediate fields terminated by ' | ' lines terminated by '\n';
load data local infile 'locationdata.txt' into table location fields terminated by ' | ' lines terminated by '\n';
load data local infile 'conditiondata.txt' into table condition fields terminated by ' | ' lines terminated by '\n';


load data local infile 'located_indata.txt' into table located_in fields terminated by ' | ' lines terminated by '\n';
load data local infile 'convertsdata.txt' into table converts fields terminated by ' | ' lines terminated by '\n';
load data local infile 'usesdata.txt' into table uses fields terminated by ' | ' lines terminated by '\n';
load data local infile 'operates_underdata.txt' into table operates_under fields terminated by ' | ' lines terminated by '\n';

