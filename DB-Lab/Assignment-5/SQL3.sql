SELECT Patients.Name
FROM Patients 
INNER JOIN Visits ON Visits.Patient_id = Patients.ID
INNER JOIN Doctors ON Doctors.ID = Visits.Doctor_id
WHERE Doctors.salary > 1000;
