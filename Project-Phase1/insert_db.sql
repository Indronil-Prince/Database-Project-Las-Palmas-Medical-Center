INSERT INTO Physician VALUES (1, 'Jude Bellingham', 'Surgeon', 11111111);
INSERT INTO Physician VALUES (2, 'Rodrygo Goes', 'Intern', 22222222);
INSERT INTO Physician VALUES (3, 'Luka Modric', 'Chief of Medicine', 33333333);
INSERT INTO Physician VALUES (4, 'Toni Kross', 'Psychiatrist', 44444444);
INSERT INTO Physician VALUES (5, 'Vinicius Junior', 'Senior', 55555555);

INSERT INTO Department VALUES (1, 'Surgery', 1);
INSERT INTO Department VALUES (2, 'General Medicine', 3);
INSERT INTO Department VALUES (3, 'Psychiatry', 4);

INSERT INTO AffiliatedWith VALUES (1, 1);
INSERT INTO AffiliatedWith VALUES (2, 2);
INSERT INTO AffiliatedWith VALUES (3, 2);
INSERT INTO AffiliatedWith VALUES (4, 3);
INSERT INTO AffiliatedWith VALUES (5, 2);

INSERT INTO `Procedure` VALUES (1, 'Proc A', 1500.0);
INSERT INTO `Procedure` VALUES (2, 'Proc B', 1200.0);
INSERT INTO `Procedure` VALUES (3, 'Proc C', 2000.0);
INSERT INTO `Procedure` VALUES (4, 'Proc D', 1800.0);
INSERT INTO `Procedure` VALUES (5, 'Proc E', 2500.0);

INSERT INTO Patient VALUES (1, 100001, 'Antonio Rudiger', '12 Abc Drive', '1980-01-01', '575-123-1234', 123454, 1);
INSERT INTO Patient VALUES (2, 100002, 'Nacho Fernandez', '34 Def Street', '1990-05-15', '575-456-7890', 567890, 3);
INSERT INTO Patient VALUES (3, 100003, 'Dani Carvajal', '56 Ghi Avenue', '1975-08-20', '575-789-5678', 789012, 5);
INSERT INTO Patient VALUES (4, 100004, 'Ferland Mendy', '78 Jkl Road', '1988-03-10', '575-234-6789', 345678, 2);
INSERT INTO Patient VALUES (5, 100005, 'Fran Garcia', '90 Mno Lane', '1995-11-05', '575-890-1234', 901234, 4);

INSERT INTO Nurse VALUES (1, 'Joselu Mato', 'Head Nurse', 333333);
INSERT INTO Nurse VALUES (2, 'Brahim Diaz', 'Nurse', 444444);
INSERT INTO Nurse VALUES (3, 'Andrey Lunin', 'Nurse', 555555);
INSERT INTO Nurse VALUES (4, 'Eder Militao', 'Head Nurse', 666666);
INSERT INTO Nurse VALUES (5, 'Federico Valverde', 'Nurse', 777777);

INSERT INTO Medication VALUES (1, 'Med A');
INSERT INTO Medication VALUES (2, 'Med B');
INSERT INTO Medication VALUES (3, 'Med C');
INSERT INTO Medication VALUES (4, 'Med D');
INSERT INTO Medication VALUES (5, 'Med E');

INSERT INTO Prescribes VALUES (1, 1, 1, '2022-01-15', '5/day');
INSERT INTO Prescribes VALUES (2, 2, 2, '2022-01-20', '3/day');
INSERT INTO Prescribes VALUES (3, 3, 3, '2022-02-01', '2/day');
INSERT INTO Prescribes VALUES (4, 4, 4, '2022-02-15', '1/day');
INSERT INTO Prescribes VALUES (5, 5, 5, '2022-03-01', '4/day');

INSERT INTO Room VALUES (1, 'Single');
INSERT INTO Room VALUES (2, 'Double');
INSERT INTO Room VALUES (3, 'Single');
INSERT INTO Room VALUES (4, 'Double');
INSERT INTO Room VALUES (5, 'Single');

INSERT INTO Stay VALUES (1, 1, 1, '2022-01-07', '2022-01-20');
INSERT INTO Stay VALUES (2, 2, 2, '2022-02-01', '2022-02-15');
INSERT INTO Stay VALUES (3, 3, 3, '2022-03-01', '2022-03-10');
INSERT INTO Stay VALUES (4, 4, 4, '2022-04-01', '2022-04-15');
INSERT INTO Stay VALUES (5, 5, 5, '2022-05-01', '2022-05-10');

INSERT INTO Undergoes VALUES (1, 1, 1, '2022-01-10', 1, 1);
INSERT INTO Undergoes VALUES (2, 2, 2, '2022-02-05', 2, 2);
INSERT INTO Undergoes VALUES (3, 3, 3, '2022-03-05', 3, 3);
INSERT INTO Undergoes VALUES (4, 4, 4, '2022-04-10', 4, 4);
INSERT INTO Undergoes VALUES (5, 5, 5, '2022-05-05', 5, 5);

INSERT INTO OnCall VALUES (1, '2022-01-01', '2022-02-01');
INSERT INTO OnCall VALUES (2, '2022-02-01', '2022-03-01');
INSERT INTO OnCall VALUES (3, '2022-03-01', '2022-04-01');
INSERT INTO OnCall VALUES (4, '2022-04-01', '2022-05-01');
INSERT INTO OnCall VALUES (5, '2022-05-01', '2022-06-01');

INSERT INTO Appointment VALUES (1, 1, 1, 5, '2021-12-05 14:00', '2021-12-05 15:00');
INSERT INTO Appointment VALUES (2, 2, 3, 2, '2021-12-10 10:00', '2021-12-10 11:00');
INSERT INTO Appointment VALUES (3, 3, 2, 4, '2021-12-15 16:00', '2021-12-15 17:00');
INSERT INTO Appointment VALUES (4, 4, 5, 3, '2021-12-20 12:00', '2021-12-20 13:00');
INSERT INTO Appointment VALUES (5, 5, 4, 1, '2021-12-25 18:00', '2021-12-25 19:00');
