'''
Recruitment is underway in many companies. For each candidate we want to
calculate the number of companies they have applied to.

Wa are given two tables, candidates and reports, representing data about an ongoing recruitment process. They have
the following structure:

create table candidates (
    id integer primary key,
    name, varchar (20) not null unique,
    age integer not null
);

create table reports (
    id integer primary key,
    company varchar(20) not null,
    candidate_id integer not null,
    score integer not null
);

Every row of the table candidates contains information about a single candidate: unique id (id), unique name (name)
and age (age). every row of the table reports contains information about a single test session:
unique id (id), name of the company that conducted the test (company), id of a candidate that was tested
(candidate_id) and a final score (score).

Write a SQL query that, for each candidate, calculates the number of distinct companies that he/she applied to.
The table of results ahould contain three solumns: id(id of the candidate), name(name of the candidate) and
campanies (number of distinct companies the candidate allplied to). the rows should be ordered by increasing id of
the candidates.

examples:

1. given tables:
candidates:
id: 25,113,10
name: Taylor, Paul, Lara
age: 30,21,19

reports:
id:1,36,137,2
company: codility, soft, codility, itcompany
candidate_id: 10,113,10,10
score: 20,60,30,99

the query should return:
id: 10,25,113
name: Lara, Taylor, Paul
companies: 2,0,0

2. given tables:
candidates:
ied:30,25
name: Tom, Kate
age: 42,23
reports:
id:
company:
candidate_id:
score:

The query should return:
id:25,30
name: kate, tom
companies: 0,0

3. given tables:
candidates:
id: 25
name:
Jack
age:32

reports:
id: 10,85,50
company cadility, itcompany, codility
candidate_id:
25,25,25
score: 100,90,50

the query should return:
id: 25
name: jack
companies: 2

Assume that:
values of id column in both canididates and reports are integers within the range [1..1000000];
values of the name column in candidates and the company column in reports are strings consisting of lower-and uppercase letters;
values of the age column are integers within the range [18..100];
values of the score column are integers within the range [0..100];
every value in the candidate_id column occurs as a value in the id column in the candidates table.
'''

SELECT c.id, c.name, COUNT(DISTINCT r.company) AS companies
FROM candidates c
LEFT JOIN reports r ON c.id = r.candidate_id
GROUP BY c.id, c.name
ORDER BY c.id;