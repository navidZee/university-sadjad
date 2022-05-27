SELECT Nurses.Name FROM Nurses 
INNER JOIN Visits ON Visits.Nurse_id = Nurses.ID
INNER JOIN Doctors ON Doctors.ID= Visits.Doctor_id
where Doctors.name = 'مهدی صادقی'