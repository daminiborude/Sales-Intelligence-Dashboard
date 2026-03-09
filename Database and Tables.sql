CREATE DATABASE sales_analysis;
USE sales_analysis;

-- Create Product Table
CREATE TABLE Products(
product varchar(50),
series varchar(50),
sales_price int
);

-- Create Account Table
CREATE TABLE Accounts(
account varchar(100),
sector varchar(50),
year_established year,
revenue decimal,
employees int,
office_location varchar(50),
subsidiary_of varchar(50)
);


-- Create Sales_Team Table
CREATE TABLE Sales_Team(
sales_agent varchar(100),
manager varchar(100),
regional_office varchar(50)
);


-- Create Sales_Pipeline Table
CREATE TABLE Sales_Pipeline(
opportunity_id varchar(50),
sales_agent varchar(100),
product varchar(50),
account varchar(100),
deal_stage varchar(50),
engage_date varchar(50),
close_date varchar(50),
close_value decimal
);




