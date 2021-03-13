--5.What data will be in the admin panel?
Select Name,Position,employee_hours_at_work	 from Employee INNER JOIN Employee_time ON Employee_time.Employee_id=Employee.Employee_Id;