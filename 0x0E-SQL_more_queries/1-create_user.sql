-- script that creates the MySQL server user

CREATE USER IF NOT EXISTS user_0d_1@localhost IDENTIFIED BY user_0d_1_pwd;
GRANT ALL PRIVILEDGES ON MySQL.* user_0d_1@localhost; 
