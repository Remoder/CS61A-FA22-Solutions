-- Data --
CREATE TABLE records AS
  SELECT 'Ben Bitdiddle' AS Name, 'Computer' AS Division, 'Wizard' AS Title, 60000 AS Salary, 'Oliver Warbucks' AS Supervisor UNION
  SELECT 'Alyssa P Hacker', 'Computer', 'Programmer', 40000, 'Ben Bitdiddle' UNION
  SELECT 'Cy D Fect', 'Computer', 'Programmer', 35000, 'Ben Bitdiddle' UNION
  SELECT 'Lem E Tweakit', 'Computer', 'Technician', 25000, 'Ben Bitdiddle' UNION
  SELECT 'Louis Reasoner', 'Computer', 'Programmer Trainee', 30000, 'Alyssa P Hacker' UNION
  SELECT 'Oliver Warbucks', 'Administration', 'Big Wheel', 150000, 'Oliver Warbucks' UNION
  SELECT 'Eben Scrooge', 'Accounting', 'Chief Accountant', 75000, 'Oliver Warbucks' UNION
  SELECT 'Robert Cratchet', 'Accounting', 'Scrivener', 18000, 'Eben Scrooge';

CREATE TABLE meetings AS
  SELECT 'Accounting' AS Division, 'Monday' AS Day, '9am' AS Time UNION
  SELECT 'Computer', 'Wednesday', '4pm' UNION
  SELECT 'Administration', 'Monday', '11am' UNION
  SELECT 'Administration', 'Wednesday', '4pm';



-- * Question 9: Oliver Employee Meetings *
SELECT mt.Day AS day, mt.Time AS time
       FROM records AS rc, meetings AS mt
       WHERE rc.Division = mt.Division AND rc.Supervisor = "Oliver Warbucks";



-- * Question 10: Different Division *
SELECT a.Name AS name FROM records AS a, records AS b
       WHERE a.Supervisor = b.Name and a.Division <> b.Division;

