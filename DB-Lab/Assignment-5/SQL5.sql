SELECT Sickness.name,Nurses.salary as nurse_Salary,Doctors.salary as doctor_Salary
FROM Sickness 
inner join Patients ON Sickness.ID = Patients.Sickness_id
inner join Visits ON Visits.Patient_id = Patients.ID
INNER JOIN Nurses ON Visits.Nurse_id = Nurses.ID
INNER JOIN Doctors ON Visits.Doctor_id = Doctors.ID
WHERE Nurses.salary > 2000 AND Doctors.salary > 5000