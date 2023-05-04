CREATE TABLE taxi_clone LIKE taxi;

--clone table definition & data
CREATE TABLE taxi_clone
  SHALLOW CLONE taxi