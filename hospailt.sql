create database hospital;
use hospital;
 
create table signuppeople(
Name varchar(21),
Father_name varchar(24),
Mother_name varchar(24),
dob varchar(21),
gender varchar(25),
email varchar(34), 
marital_status varchar(24), 
address varchar(50), 
city varchar(25), 
pincode varchar(20), 
state varchar(25)
);
create table patient(
patient_name varchar(21),
patient_lastname varchar(23),
patient_Age varchar(26),
patient_D.O.B varchar(21),
patient_gender varchar(10),
partient_number varchar(13),
partient_bulding varchar(32),
partient_staute varchar(27),
partient_wellstable varchar(27),
partientP_bedroom varchar(10)
);
create table doctors (
doctors_id varchar(23),
doctors_name varchar(26),
doctors_dob varchar(21),
doctors_Age varchar(26),
doctors_gender varchar(25),
doctor_deperment varchar(30),
doctors_types varchar(23),
doctors_staute varchar(23),
doctors_bulding varchar(32),
doctors_phone varchar(15),
doctors_room.n varchar(10),
doctors_attendance.n varchar(16)
);
create table nurses(
nurses_id varchar(23),
nurses_Name varchar(27),
nurses_gender varchar(25),
nurses_dob varchar(21),
nurses_Age varchar(26),
nurses_typer varchar(37),
nurses_staute varchar(23),
nurses_depermnt varchar(33),
nurses_phone varchar(10),
nurses_attendance varchar(16)
);
create table staff(
staff_id varchar (23),
staff_name varchar(30),
staff_gender varchar(8),
staff_staute varchar(23),
staff_depermnt varchar(33),
staff_phone.n  varchar(10),
staff_attendance.n varchar(16)
);
create table Macconcate(
acconcateId varchar (23),
acconcate_name varchar(30),
acconcate_phone varchar(10),
acconcate_staute varchar(27),
acconcate_attendance varchar(16)
); 
   