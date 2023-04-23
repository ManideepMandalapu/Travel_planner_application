INSERT INTO useraccount (first_name, last_name,email, phone_number,password, created) 
VALUES ('Sample', 'last name', 'sample.lastname@gmail.com', '2023-04-23 09:00:00');

INSERT INTO useraccount (first_name, last_name,email, phone_number,password, created) 
VALUES ('Sample', 'last name', 'sample.lastname@gmail.com', '2023-04-23 09:00:00');

INSERT INTO useraccount (first_name, last_name,email, phone_number,password, created) 
VALUES ('Sample', 'last name', 'sample.lastname@gmail.com', '2023-04-23 09:00:00');

INSERT INTO useraccount (first_name, last_name,email, phone_number,password, created) 
VALUES ('Sample', 'last name', 'sample.lastname@gmail.com', '2023-04-23 09:00:00');



INSERT INTO trips (user_account_id,name, start_date, end_date, created) 
VALUES (1, 'Kansas City', '2023-05-15', '2023-05-30', '2023-04-23 09:00:00');

INSERT INTO trips (user_account_id,name, start_date, end_date, created) 
VALUES (2, 'Dallas', '2023-04-15', '2023-04-20', '2023-03-23 09:00:00');

INSERT INTO trips (user_account_id,name, start_date, end_date, created) 
VALUES (3, 'Beach Vacation', '2023-06-15', '2023-06-20', '2023-03-23 09:00:00');

INSERT INTO trips (user_account_id,name, start_date, end_date, created) 
VALUES (4, 'Family Reunion', '2023-09-15', '2023-09-20', '2023-03-23 09:00:00');

INSERT INTO trips (user_account_id,name, start_date, end_date, created) 
VALUES (5, 'Business Trip', '2023-112-15', '2023-12-20', '2023-03-23 09:00:00');



INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (1,'Down Town','Sample notes', '2023-04-23 13:00:00');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (2,'Shopping malls','buy clothes', '2023-04-23 13:00:00');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (3,'Amsterdam','Take a canal cruise', '2023-04-23 13:00:00');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (4,'Bowling Alley','Have a family picnic', '2023-04-23 13:00:00');

INSERT INTO destination (trip_id,name, notes, crated) 
VALUES (5,'London','Attend conference', '2023-04-23 13:00:00');



INSERT INTO activities (destination_id,name,date, time, notes, created) 
VALUES (1,'Visit Eiffel Tower', '2023-05-16', '16:00:00', 'Don''t forget to buy tickets in advance!', '2023-04-23 10:00:00');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (2,'Canal Cruise', '2023-10-20', '15:00:00', 'Book tickets online to skip the line.', '2023-10-23 15:00:00');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (3,'Visit water falls', '2023-05-20', '15:00:00', 'Book motels.', '2023-10-23 15:00:00');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (4,'Visit water parks', '2023-05-20', '15:00:00', 'Book motels.', '2023-10-23 15:00:00');

INSERT INTO activities (destination_id,name,date,time, notes, created) 
VALUES (5,'Visit ', '2023-05-20', '15:00:00', 'Book motels.', '2023-10-23 15:00:00');


