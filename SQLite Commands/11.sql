--What data will be visible if the employee clicks on create a clearance order?
SELECT Dis_Journal_Id FROM Disposal_Journal LEFT JOIN Create_E_Naryad_Table_4
CASE
        WHEN Create_E_Naryad_Table_4.Employee_id == Dis_Journal_Id.Employee_id  THEN
      'Done'
ELSE
      'it is impossible'
    END Dis_Journal_Id;