SELECT Doctors.Name,Sickness.Name
from Doctors 
INNER JOIN Visits ON Visits.Doctor_id = Doctors.ID
INNER JOIN Patients ON Patients.ID = Visits.Patient_id
INNER JOIN Sickness ON Sickness.ID = Patients.Sickness_id
WHERE Sickness.name='سرماخوردگی'