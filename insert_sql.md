INSERT INTO useraccount (user_account_id,first_name, last_name,email, phone_number, created) 
VALUES (	1, 'abcd',	'xyz', 'abcd.xyz@gmail.com', 99999999, '01/04/2023');

INSERT INTO useraccount (user_account_id,first_name, last_name,email, phone_number, created) 
VALUES (2,	'xyz', 'abcd', 'xyz.abcd@gmail.com', 55512457, '01/05/2023');

INSERT INTO useraccount (user_account_id,first_name, last_name,email, phone_number, created) 
VALUES (3,	'max', 'adam', 'adam.max@gmail.com', 78526520, '02/07/2023');

INSERT INTO useraccount (user_account_id,first_name, last_name,email, phone_number, created) 
VALUES (4, 'jeni', 'james', 'jeni.james@gmail.com',	00001112,	'05/07/2023');

INSERT INTO useraccount (user_account_id,first_name, last_name,email, phone_number, created)
VALUES (5, 'jack', 'bord',  'jack.bord@gmail.com',  789954252,  '08/07/2023')






INSERT INTO trips (trip_id, user_account_id,name, start_date, end_date, created) 
VALUES (1, 1, 'colorado', '2023-05-15', '2023-05-30', '2023-04-23 09:00:00');

INSERT INTO trips (trip_id, user_account_id,name, start_date, end_date, created) 
VALUES (2, 2, 'Oklohoma', '2023-04-15', '2023-04-20', '2023-03-23 09:00:00');

INSERT INTO trips (trip_id, user_account_id,name, start_date, end_date, created) 
VALUES (3, 3, 'Texas', '2023-06-15', '2023-06-20', '2023-03-23 09:00:00');

INSERT INTO trips (trip_id, user_account_id,name, start_date, end_date, created) 
VALUES (4, 4, 'Virginia', '2023-09-15', '2023-09-20', '2023-03-23 09:00:00');

INSERT INTO trips (trip_id, user_account_id,name, start_date, end_date, created) 
VALUES (5, 5, 'Denver', '2023-112-15', '2023-12-20', '2023-03-23 09:00:00');



INSERT INTO destination (trip_id,destination_id,name, notes, crated) 
VALUES (1, 1,'Mountain treking','Reserve tickets online', '03/04/2023 10:00:00');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (2, 5,'Visit du university','schedule campus tour', '01/04/2023 13:41:52');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (3, 4,'Virginia beach','Book motel near by', '04/04/2023 14:47:15');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (4, 1,'Mountain trecking','spring visit', '02/04/2023 15:15:10');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (5, 2,'waterfalls visit','Book tickets for visit', '04/04/2023 11:23:35');





INSERT INTO activities (activity_id,destination_id,date, notes, created) 
VALUES (1, 1, '04/24/2023', 'Make Dinner reservations', '23/04/2023 10:00:00');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (2, 2, '04/21/2023', 'order food on campus', '24/04/2023 11:15:00');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (3, 3, '04/28/2023',  'book a ride to motel', '04/04/2023 13:52:00');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (4, 4,'04/23/2023', 'Book a parking lot', '03/04/2023 21:45:12');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (5, 5,'04/20/2023', 'reserve a motel', '07/04/2023 22:15:00');




