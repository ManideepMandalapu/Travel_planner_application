# Database description

We designed this database to store and manage the trips, destinations and activities of each destination. 

This database mainly has 4 tables `useraccount`,`trips`,`Destination` and `Activities` and we created those tables in
simple sqlite3 database. 

useraccount table is used for storing the registered customers / users of this application and this table contains
the first_name,last_name, email, phone_number and created as fields. user_account_id as primary key for this table.

trips table is used for storing the planned trips information , registered users can plan their trips and we are 
saving those information in this table, this table has foreign key to reference useraccount table and other fields like start_date,
end_date, name is using for trips information.

Destination table stores the information about each individual trip, this table foreign key relationship with
trips table and other fields for storing about the destinations.

activities table stores the information about each activity that needs to be done in each destination and customer can note each 
activity information using this table.

Each table has unique identifier called primary key and we are using created field in each table for identifying
when each record of table created. We added the foreign key for better data integrity.






CREATE TABLE IF NOT EXISTS "useraccount" 
(
"user_account_id" integer PRIMARY KEY AUTOINCREMENT, 
"first_name" varchar(60) NOT NULL, 
"last_name" varchar(60) NOT NULL, 
"email" varchar(100) NOT NULL, 
"phone_number" varchar(10) NOT NULL, 
"password" varchar(128) NOT NULL,
"created" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "trips" (
"trip_id" integer PRIMARY KEY AUTOINCREMENT, 
"name" varchar(100) NOT NULL, 
"start_date" date NOT NULL, 
"end_date" date NOT NULL, 
"created" datetime NOT NULL, 
"user_account_id" integer NOT NULL REFERENCES "useraccount" ("user_account_id") ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "destination" (
"destination_id" integer PRIMARY KEY AUTOINCREMENT, 
"name" varchar(100) NOT NULL, 
"notes" varchar(200) NULL, 
"created" datetime NOT NULL, 
"trip_id" integer NOT NULL REFERENCES "trips" ("trip_id") ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "activities" (
"activity_id" integer PRIMARY KEY AUTOINCREMENT, 
"date" date NOT NULL, "time" time NOT NULL, 
"notes" varchar(200) NULL, "created" datetime NOT NULL, 
"destination_id" integer NOT NULL REFERENCES "destination" ("destination_id") ON DELETE CASCADE
);





# Primary keys of each table

`useraccount` table: user_account_id
`trips` table: trip_id
`destination` table: destination_id
`activities` table: activity_id




# Foreign key of each table

`trips` table has foreign key relationship with `user_account_id` of useraccount table.

`destination` table has foreign key relationship with `trip_id` of trips table.

`activities` table has foreign key relationship with `destination_id` of destination table.




# Functional dependencies of each table

useraccount table.

user_account_id -> first_name,last_name,email,phone_number,created.

trips table

trip_id -> name, start_date, end_date,created,user_account_id

user_account_id -> trip_id, name, start_date, end_date, created

destination table

destination_id -> trip_id, name, notes, created
trip_id -> destination_id, name, notes,created

activities table

activity_id -> destination_id, name,date, time, notes, created

destination_id -> activity_id, name,date, time, date, created





# whether in 3NF

Yes, all above tables are in 3NF form.

in this database, each table has a single primary key and each non-key column in table is dependent only on primary 
key of the table.








# Sample data of each table.

useraccount:

SELECT * 
FROM useraccount
LIMIT 5


user_account_id       first_name        last_name  		   email   			    phone_number         created

	1			abcd			xyz			abcd.xyz@gmail.com		99999999		01/04/2023
	2			xyz			abcd			xyz.abcd@gmail.com		55512457		01/05/2023
	3			max			adam			adam.max@gmail.com		78526520		02/07/2023
	4			jeni			james			jeni.james@gmail.com		00001112		05/07/2023
	5			jack			bord			jack.bord@gmail.com		789954252		08/07/2023


trips :

SELECT *
FROM trips
LIMIT 5



trip_id	user_account_id		name		start_date		end_date 		created
   
   1			1		    Colorado	03/04/2023		05/04/2023		02/04/2023
   2			2		    oklahoma	06/04/2023		07/04/2023		04/04/2023
   3			3		    Texas		06/04/2023		07/04/2023		03/04/2023
   4			4		    virgenia	05/04/2023		08/04/2023		04/04/2023
   5			5		    Denver		06/04/2023		09/04/2023		01/04/2023


Destination :

SELECT *
FROM destination
LIMIT 5


destination_id	trip_id		name				notes					created
	
	1		  3		Mountain treking		Reserve tickets online		03/04/2023 10:00:00
	2		  5		Visit du university	schedule campus tour		01/04/2023 13:41:52
	3		  4		Virginia beach		Book motel near by		04/04/2023 14:47:15
	4		  1		Mountain trecking		spring visit			02/04/2023 15:15:10
	5		  2		waterfalls visit		Book tickets for visit		04/04/2023 11:23:35	  


activities :

SELECT *
FROM activities
LIMIT 5

activity_id		destination_id	  date			notes					created

	1			1		04/24/2023		Make Dinner reservations	23/04/2023 10:00:00
	2			2		04/21/2023		order food on campus		24/04/2023 11:15:00
	3			3		04/28/2023		book a ride to motel		04/04/2023 13:52:00
	4			4		04/23/2023		Book a parking lot		03/04/2023 21:45:12
	5			5		04/20/2023		reserve a motel			07/04/2023 22:15:00
	
