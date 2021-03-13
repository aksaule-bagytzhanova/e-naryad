--  DDL for Table Employee

DROP TABLE IF EXISTS Employee;
CREATE TABLE IF NOT EXISTS Employee(
    Employee_id INTEGER PRIMARY KEY AUTOINCREMENT,
	Name VARCHAR NOT NULL,
	Surname VARCHAR NOT NULL,
	Position VARCHAR NOT NULL ,
	Password VARCHAR NOT NULL 
);

--------------------------------------------------------
--  DDL for Table Employee_time

DROP TABLE IF EXISTS Employee_time;
CREATE TABLE IF NOT EXISTS Employee_time(
    Employee_Hours_At_Work INTEGER NOT NULL,
	Employee_id INTEGER NOT NULL,
    Holiday_Hours INTEGER NOT NULL,
    Sick_Hours INTEGER NOT NULL,
    FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 
);

--------------------------------------------------------
--  DDL for Table System_Time_In_Month

DROP TABLE IF EXISTS System_Time_In_Month;
CREATE TABLE IF NOT EXISTS System_Time_In_Month(
	Employee_id INTEGER NOT NULL,
    Time_At_Work INTEGER NOT NULL,
    Holiday_time INTEGER NOT NULL,
    Vacation_Time INTEGER NOT NULL,
    FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 

);

--------------------------------------------------------
--  DDL for Table Create_E_Naryad_Table_1

DROP TABLE IF EXISTS Create_E_Naryad_Table_1;
CREATE TABLE IF NOT EXISTS Create_E_Naryad_Table_1(
    Table_One_id INTEGER PRIMARY KEY AUTOINCREMENT,
    	Employee_id INTEGER NOT NULL,
        Organization VARCHAR NOT NULL,
        Plot VARCHAR NOT NULL,
        Admitting VARCHAR NOT NULL,
        Team_Members VARCHAR NOT NULL,
        Category_Of_Work VARCHAR NOT NULL,
        Employee_Prepardness_Time DATETIME DEFAULT current_timestamp,
        An_Object VARCHAR NOT NULL,
        Finish_Work_Date DATETIME DEFAULT current_date,
        Subdivision VARCHAR NOT NULL,
        Work_Manager VARCHAR NOT NULL,
        Observer  VARCHAR NOT NULL,
        Open_Single_Line_Diagram  VARCHAR NOT NULL,
        Is_Entrusted  VARCHAR NOT NULL,
        Start_Work DATETIME DEFAULT current_timestamp,
        Names_Electrical_Installations TEXT DEFAULT NULL,
        Separate_Instructions TEXT DEFAULT NULL,
        Signature TEXT DEFAULT NULL,
        Be_Disconnected TEXT DEFAULT NULL,
        Outfit_Issued VARCHAR NOT NULL,
        Surname VARCHAR NOT NULL,
        FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 
);

--------------------------------------------------------
--  DDL for Table Messages

DROP TABLE IF EXISTS Messages;
CREATE TABLE IF NOT EXISTS Messages(
    Messages_id INTEGER PRIMARY KEY AUTOINCREMENT,
	Employee_id INTEGER NOT NULL,
    Subject VARCHAR NOT NULL,
    Date_sent DATETIME DEFAULT current_timestamp,
    Sent_From VARCHAR NOT NULL,
    Messages_Text TEXT DEFAULT NULL,
    FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 

);

--------------------------------------------------------
--  DDL for Table Create_E_Naryad_Table_2

DROP TABLE IF EXISTS Create_E_Naryad_Table_2;
CREATE TABLE IF NOT EXISTS Create_E_Naryad_Table_2(
    Table_Two_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Employee_id INTEGER NOT NULL,
    Person_Issued_Outfit VARCHAR NOT NULL,
    Signature_Outfit VARCHAR NOT NULL,
    Responsible_Work_Manager VARCHAR NOT NULL,
    Signature_W_Manager VARCHAR NOT NULL,
    FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 
);

--------------------------------------------------------
--  DDL for Table Create_E_Naryad_Table_3

DROP TABLE IF EXISTS Create_E_Naryad_Table_3;
CREATE TABLE IF NOT EXISTS Create_E_Naryad_Table_3(
    Table_Three_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Employee_id INTEGER NOT NULL,
    Outfit_gave VARCHAR NOT NULL,
    Signature VARCHAR NOT NULL,
    Date_time DATETIME DEFAULT current_timestamp,
    Workplaces_Prepared TEXT DEFAULT NULL,
    Surname VARCHAR NOT NULL,
    Agreed VARCHAR NOT NULL,
    Admitting VARCHAR NOT NULL,
    Responsible_Performance_Manager VARCHAR NOT NULL,
    FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 
); 

--------------------------------------------------------
--  DDL for Table Create_E_Naryad_Table_4

DROP TABLE IF EXISTS Create_E_Naryad_Table_4;
CREATE TABLE IF NOT EXISTS Create_E_Naryad_Table_4(
    Table_Four_id INTEGER PRIMARY KEY AUTOINCREMENT,
    Employee_id INTEGER NOT NULL,
    Number INTEGER NOT NULL,
    Hazards_Risks_Ident VARCHAR NOT NULL,
    Date DATETIME DEFAULT current_date,
    Company VARCHAR NOT NULL,
    Job_Tasks VARCHAR NOT NULL,
    Members_Group VARCHAR NOT NULL,
    Stages_of_Work TEXT DEFAULT NULL,
    Possible_Potential_Accidents TEXT DEFAULT NULL,
    Control_Measures TEXT DEFAULT NULL,
    Responsible_Performance_Manager VARCHAR NOT NULL,
    Are_There_Control_Measures TEXT DEFAULT NULL,
    FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 
);
 
--------------------------------------------------------
--  DDL for Table Disposal_Journal

DROP TABLE IF EXISTS Disposal_Journal;
CREATE TABLE IF NOT EXISTS Disposal_Journal(
    Dis_Journal_Id INTEGER PRIMARY KEY AUTOINCREMENT,
    Employee_id INTEGER NOT NULL,
    Technical_Activities VARCHAR NOT NULL,
    Place_Name_Of_Work VARCHAR NOT NULL,
    Supervising VARCHAR NOT NULL,
    Team_Members_Working_On_Orders VARCHAR NOT NULL,
    Person_Who_Gave_Outfit VARCHAR NOT NULL,
    Started_Work DATETIME DEFAULT current_timestamp,
    Work_Done DATETIME DEFAULT current_timestamp,
    FOREIGN KEY (Employee_id)
       REFERENCES  Employee(Employee_id) 
);


