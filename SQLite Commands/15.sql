--How to see messages from meneger
SELECT *
FROM Messages
where Sent_From=(select name from employees where position="Main manager");	