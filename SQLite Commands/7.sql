--What kind of tables are there?
select name,position,Category_Of_work	,Technical_Activities 
from employees 
join Create_E_Naryad_Table_1
on Create_E_Naryad_Table_1.Employee_id=Employee.Employee_id
join Disposal_Journal
on Disposal_Journal.Employee_id=Employee.Employee_id
where Employee_id=1;