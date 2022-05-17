## 🦑 Assignment 1 : PART 3 - SQL
<hr>


### 1. List all Employees whose salary is between 1,000 AND 2,000. Show the Employee Name, Department and Salary. 
**Solution Description:**
* `To Disaply just the Employee Name, Department Name and Salary.`
* `We can use the SELECT statement to choose the columns we want to display.`
* `Then JOIN the EMP and DEPT Tables using the Foregin Key DEPTNO to Link up and reference with the DEPTNO in the DEPT table(Ndungu 2021).`
* `Then we can use the WHERE AND BETWEEN clause to filter the results within the required salary range.`

**SQL Query:**
```sql
SELECT ENAME "Employee Name", DNAME "Department", SAL "Salary" FROM EMP LEFT JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO WHERE SAL BETWEEN 1000 AND 2000;
```

#### Alternative SQL Statement:
* `Alternatively, instead of the BETWEEN clause, we can make use of the greater than or equal to >= and less than or equal to <= operators to filter the results within the required salary range.`

```sql
SELECT ENAME "Employee Name", DNAME "Department", SAL "Salary" FROM EMP LEFT JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO WHERE SAL >= 1000 AND SAL <= 2000;
```

### 2. Count the number of people in department 30 who receive a salary and the number of people who receive a commission.
**Solution Description:**
* `We can use the COUNT function to count the number of rows in the table.`
* `Which means we can use this statement to count the ammount of Rows within SAL and COMM columns where the Salaries and Commissions are greater than Zero AND NOT NULL.`
* `WE can also add custom column names to the COUNT functions to improve the outputted table results clarity.`

**SQL Query:**
```sql
SELECT COUNT(SAL) "Salary", COUNT(COMM) "Commission" FROM EMP WHERE DEPTNO = 30 AND (SAL > 0 OR COMM > 0);
```

### 3. Find the name and salary of employees in Dallas.
**Solution Description:**
* `We can use the SELECT statement to choose the columns we want to display.`
* `Then JOIN the EMP and DEPT Tables using the Foregin Key DEPTNO to Link up and reference with the DEPTNO in the DEPT table.`
* `Then we can use the WHERE clause to filter the results based on the column LOC value.`

**SQL Query:**
```sql
SELECT ENAME "Employee Name", SAL "Salary", LOC "Location" FROM EMP LEFT JOIN DEPT ON EMP.DEPTNO = DEPT.DEPTNO WHERE LOC = "DALLAS";
```

### 4. List all departments that do not have any employees.
**Solution Description:**
* `We can use the SELECT statement to choose the columns we want to display.`
* `Then JOIN the EMP and DEPT Tables using the Foregin Key DEPTNO to Link up and reference with the DEPTNO in the DEPT table.`
* `Then we can use the WHERE clause to filter the results based on the column EMP.EMPNO value.`
* `We check if the EMP.EMPNO value is null or not. If null then the Department is not assigned to any employee.`

**SQL Query:**
```sql
SELECT DNAME "Department Name" FROM DEPT LEFT JOIN EMP ON DEPT.DEPTNO = EMP.DEPTNO WHERE EMP.EMPNO IS NULL;
```

### 5. List the department number and average salary of each department.
**Solution Description:**
* `We can use the SELECT statement to choose the columns we want to display.`
* `THEN We can use the AVG function to calculate the average salary of each department.`
* `We can use the GROUP BY statement to group the results by the DEPTNO column.`

**SQL Query:**
```sql
SELECT DEPTNO, AVG(SAL) "Average Salary" FROM EMP GROUP BY DEPTNO;
```

<hr>

## ✍️ References ##

The following references were used in this project:  

* Using Foreign Keys : 
Ndungu, F. (Aug 17, 2021) How To Use Foreign Keys in SQL. _Digital Ocean_. Available from: [How To Use Foreign Keys in SQL](https://www.digitalocean.com/community/tutorials/how-to-use-foreign-keys-in-sql) [Accessed 17 May 2022]

