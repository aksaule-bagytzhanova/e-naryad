--Who will fill in all the data?
Select Person_Who_Gave_Outfit,Position  from Disposal_Journal INNER JOIN Employee ON Disposal_Journal.Employee_id=Employee.Employee_id;