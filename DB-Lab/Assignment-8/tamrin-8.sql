CREATE DATABASE Assets
ON (FILENAME = 'D:\SQL\Assets.mdf'),
(FILENAME = 'D:\SQL\Assets_log.ldf')
FOR ATTACH ;

BACKUP DATABASE Assets
TO DISK = 'D:\SQL\Assets.bak' ;

EXEC sp_detach_db 'Assets' , true;

RESTORE DATABASE Assets
FROM DISK = 'D:\SQL\Assets.bak ';