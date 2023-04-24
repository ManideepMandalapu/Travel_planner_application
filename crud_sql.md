INSERT INTO useraccount (user_account_id,first_name, last_name, email, phone_number, password, created) 
VALUES (1,'abcd','xyz', 'abcd.xyz@gmail.com',6655447788, 'password123', '2023-04-23 10:00:00');

select * from useraccount;

select * from useraccount where user_account_id = 1;

select name, email from useraccount;

UPDATE useraccount SET password = 'password1234' WHERE user_account_id = 1;

DELETE FROM useraccount WHERE  user_account_id= 1;

======================================================================================================================================================================





INSERT INTO trips (trip_id, user_account_id, name, start_date, end_date, created) 
VALUES (1, 1, 'colorado', '2023-05-15', '2023-05-30', '2023-04-23 09:00:00');

SELECT * FROM Trips WHERE start_date > '2023-05-01';

SELECT Trips.id, Trips.name, COUNT(Destinations.id) AS num_destinations FROM Trips;

UPDATE Trips SET name = 'New Trip Name' WHERE trip_id = 1;

UPDATE Trips SET name = 'New Trip Name', start_date = '2023-07-01' WHERE trip_id = 1;

DELETE FROM Trips WHERE start_date > '2023-05-01';


===================================================================================================================================================================




INSERT INTO destination (trip_id, destination_id,name, notes, crated) 
VALUES (1, 2, 'Mountain trecking','Book a motel', '2023-04-23 13:00:00');

SELECT D.destination_id, D.name, D.notes FROM destination as D;

SELECT * FROM destination WHERE trip_id = 2;

UPDATE destination SET city = 'New York' WHERE destination_id = 3;

DELETE FROM destination WHERE destination_id = 3;


====================================================================================================================================================================



INSERT INTO activities (activity_id, destination_id,name,date, notes, created) 
VALUES (1,5,'Visit ', '2023-05-20', '15:00:00', 'Book motels.', '2023-10-23 15:00:00');

UPDATE activities SET name = 'Order food online' WHERE activity_id = 1;

UPDATE activities SET destination_id = 5 WHERE activity_id = 1;

select * from activities;

DELETE from activities WHERE activity_id = 1;




