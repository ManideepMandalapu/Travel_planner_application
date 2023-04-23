CREATE TABLE IF NOT EXISTS "useraccount" 
(
"user_account_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"first_name" varchar(60) NOT NULL, 
"last_name" varchar(60) NOT NULL, 
"email" varchar(100) NOT NULL, 
"phone_number" varchar(10) NOT NULL, 
"password" varchar(128) NOT NULL,
"created" datetime NOT NULL
);

CREATE TABLE IF NOT EXISTS "trips" (
"trip_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(100) NOT NULL, 
"start_date" date NOT NULL, 
"end_date" date NOT NULL, 
"created" datetime NOT NULL, 
"user_account_id" integer NOT NULL REFERENCES "useraccount" ("user_account_id") ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "destination" (
"destination_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"name" varchar(100) NOT NULL, 
"notes" varchar(200) NULL, 
"created" datetime NOT NULL, 
"trip_id" integer NOT NULL REFERENCES "trips" ("trip_id") ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS "activities" (
"activity_id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
"date" date NOT NULL, "time" time NOT NULL, 
"notes" varchar(200) NULL, "created" datetime NOT NULL, 
"destination_id" integer NOT NULL REFERENCES "destination" ("destination_id") ON DELETE CASCADE
);