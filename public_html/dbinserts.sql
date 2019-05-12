load data local infile 'enzymedata.txt' into table enzyme fields terminated by ' | ' lines terminated by '\n';
load data local infile 'processdata.txt' into table process fields terminated by ' | ' lines terminated by '\n';
load data local infile 'intermediatedata.txt' into table intermediate fields terminated by ' | ' lines terminated by '\n';
load data local infile 'locationdata.txt' into table location fields terminated by ' | ' lines terminated by '\n';
load data local infile 'conditiondata.txt' into table condition fields terminated by ' | ' lines terminated by '\n';


load data local infile 'located_indata.txt' into table located_in fields terminated by ' | ' lines terminated by '\n';
load data local infile 'convertsdata.txt' into table converts fields terminated by ' | ' lines terminated by '\n';
load data local infile 'usesdata.txt' into table uses fields terminated by ' | ' lines terminated by '\n';
load data local infile 'operates_underdata.txt' into table operates_under fields terminated by ' | ' lines terminated by '\n';
