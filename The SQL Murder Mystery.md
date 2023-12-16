# The SQL Murder Mystery solution by me (CaldeCrack)

## Contents

- [The SQL Murder Mystery](#the-sql-murder-mystery-solution-by-me-caldecrack)
  - [Contents](#contents)
  - [Description](#description)
  - [Starting Point](#starting-point)
    - [Initial info](#initial-info)
    - [Tables](#tables)
    - [Structure of the tables](#structure-of-the-tables)
      - [crime_scene_report](#crime_scene_report)
      - [drivers_license](#drivers_license)
      - [facebook_event_checkin](#facebook_event_checkin)
      - [interview](#interview)
      - [get_fit_now_member](#get_fit_now_member)
      - [get_fit_now_check_in](#get_fit_now_check_in)
      - [income](#income)
      - [person](#person)
  - [Solution](#solution)
    - [Get the description of the crime](#get-the-description-of-the-crime)
    - [Find the first witness](#find-the-first-witness)
    - [Find the second witness](#find-the-second-witness)
    - [Get interviews of the witnesses](#get-interviews-of-the-witnesses)
      - [First witness](#first-witness)
      - [Second witness](#second-witness)
    - [Investigate the transcripts](#investigate-the-transcripts)
      - [First witness' transcript gym info](#first-witness-transcript-gym-info)
      - [Second witness' transcript gym info](#second-witness-transcript-gym-info)
      - [First witness' transcript car info](#first-witness-transcript-car-info)
    - [Get drivers license from the suspects](#get-drivers-license-from-the-suspects)
      - [First suspect license id](#first-suspect-license-id)
      - [Second suspect license id](#second-suspect-license-id)
    - [The culprit](#the-culprit)
    - [Checking the solution](#checking-the-solution)
  - [The Real Villain Solution](#the-real-villain-solution)
    - [Interview of the Murderer](#interview-of-the-murderer)
    - [Search for the women in the drivers license registers](#search-for-the-women-in-the-drivers-license-registers)
    - [Search for the women in the event](#search-for-the-women-in-the-event)
    - [The true villain](#the-true-villain)
    - [Checking the true villain](#checking-the-true-villain)

## Description

[The SQL Murder Misytery](https://mystery.knightlab.com) is an interactive page designed to learn SQL concepts through a fun game. It is built in [SQLite](https://www.sqlite.org/index.html).

## Starting Point

### Initial info

- The crime was a **murder**.
- Occurred sometime on **​Jan.15, 2018**.​
- It took place in ​**SQL City**.

### Tables

```sql
SELECT name
FROM sqlite_master
WHERE type = 'table'
```

| name                   |
|------------------------|
| crime_scene_report     |
| drivers_license        |
| facebook_event_checkin |
| interview              |
| get_fit_now_member     |
| get_fit_now_check_in   |
| solution               |
| income                 |
| person                 |

### Structure of the tables

#### crime_scene_report

```sql
SELECT sql 
FROM sqlite_master
WHERE name = 'crime_scene_report'
```

| **sql** |
|----------------|
| CREATE TABLE crime_scene_report ( date integer, type text, description text, city text ) |

#### drivers_license

```sql
SELECT sql 
FROM sqlite_master
WHERE name = 'drivers_license'
```

| **sql** |
|----------------|
| CREATE TABLE drivers_license ( id integer PRIMARY KEY, age integer, height integer, eye_color text, hair_color text, gender text, plate_number text, car_make text, car_model text ) |

#### facebook_event_checkin

```sql
SELECT sql 
FROM sqlite_master
WHERE name = 'facebook_event_checkin'
```

| **sql** |
|----------------|
| CREATE TABLE facebook_event_checkin ( person_id integer, event_id integer, event_name text, date integer, FOREIGN KEY (person_id) REFERENCES person(id) ) |

#### interview

```sql
SELECT sql 
FROM sqlite_master
WHERE name = 'interview'
```

| **sql** |
|------------------------------------------|
| CREATE TABLE interview ( person_id integer, transcript text, FOREIGN KEY (person_id) REFERENCES person(id) ) |

#### get_fit_now_member

```sql
SELECT sql 
FROM sqlite_master
WHERE name = 'get_fit_now_member'
```

| **sql** |
|------------------------------------------|
| CREATE TABLE get_fit_now_member ( id text PRIMARY KEY, person_id integer, name text, membership_start_date integer, membership_status text, FOREIGN KEY (person_id) REFERENCES person(id) ) |

#### get_fit_now_check_in

```sql
SELECT sql 
FROM sqlite_master
WHERE name = 'get_fit_now_check_in'
```

| **sql** |
|------------------------------------------|
| CREATE TABLE get_fit_now_check_in ( membership_id text, check_in_date integer, check_in_time integer, check_out_time integer, FOREIGN KEY (membership_id) REFERENCES get_fit_now_member(id) ) |

#### income

```sql
SELECT sql 
FROM sqlite_master
WHERE name = 'income'
```

| **sql** |
|------------------------------------------|
| CREATE TABLE income (ssn CHAR PRIMARY KEY, annual_income integer) |

#### person

```sql
SELECT sql
FROM sqlite_master
WHERE name = 'person'
```

| **sql** |
|--------------------|
| CREATE TABLE person (id integer PRIMARY KEY, name text, license_id integer, address_number integer, address_street_name text, ssn CHAR REFERENCES income (ssn), FOREIGN KEY (license_id) REFERENCES drivers_license (id)) |

## Solution

### Get the description of the crime

```sql
SELECT description
FROM crime_scene_report
WHERE "date" = 20180115
  AND type = 'murder'
  AND city = 'SQL City'
```

| **Description** |
|-----------------------|
| Security footage shows that there were 2 witnesses. The first witness lives at the last house on "Northwestern Dr". The second witness, named Annabel, lives somewhere on "Franklin Ave". |

### Find the first witness

```sql
SELECT *
FROM person
WHERE address_street_name='Northwestern Dr'
ORDER BY address_number DESC
LIMIT 1
```

| id    | name           | license_id | address_number | address_street_name | ssn       |
|-------|----------------|------------|----------------|---------------------|-----------|
| 14887 | Morty Schapiro | 118009     | 4919           | Northwestern Dr     | 111564949 |

### Find the second witness

```sql
SELECT * FROM person
WHERE name LIKE '%Annabel%'
  AND address_street_name = 'Franklin Ave'
```

| id    | name           | license_id | address_number | address_street_name | ssn       |
|-------|----------------|------------|----------------|---------------------|-----------|
| 16371 | Annabel Miller | 490173     | 103            | Franklin Ave        | 318771143 |

### Get interviews of the witnesses

#### First witness:

```sql
SELECT transcript
FROM interview
WHERE person_id = 14887
```

| **transcript** |
|----------------------|
| I heard a gunshot and then saw a man run out. He had a "Get Fit Now Gym" bag. The membership number on the bag started with "48Z". Only gold members have those bags. The man got into a car with a plate that included "H42W". |

#### Second witness:

```sql
SELECT transcript
FROM interview
WHERE person_id = 16371
```

| **transcript** |
|--------------------|
| I saw the murder happen, and I recognized the killer from my gym when I was working out last week on January the 9th. |

### Investigate the transcripts

#### First witness' transcript gym info

```sql
SELECT id, person_id, name, membership_start_date
FROM get_fit_now_member
WHERE id LIKE '48Z%'
  AND membership_status = 'gold'
```

| id    | person_id | name          | membership_start_date |
|-------|-----------|---------------|-----------------------|
| 48Z7A | 28819     | Joe Germuska  | 20160305              |
| 48Z55 | 67318     | Jeremy Bowers | 20160101              |

#### Second witness' transcript gym info

```sql
SELECT membership_id, check_in_time, check_out_time
FROM get_fit_now_check_in
WHERE membership_id LIKE '48Z%'
  AND check_in_date = 20180109
```

| membership_id | check_in_time | check_out_time |
|---------------|---------------|----------------|
| 48Z7A         | 1600          | 1730           |
| 48Z55         | 1530          | 1700           |

#### First witness' transcript car info

```sql
SELECT id, age, height, eye_color, plate_number, car_make, car_model
FROM drivers_license
WHERE plate_number LIKE '%H42W%'
  AND gender = 'male'
```

| id     | age | height | eye_color | plate_number | car_make  | car_model|
|--------|-----|--------|-----------|--------------|-----------|-----|
| 423327 | 30  | 70     | brown     | 0H42W2       | Chevrolet | Spark LS |
| 664760 | 21  | 71     | black     | 4H42WR       | Nissan    | Altima    |

### Get drivers license from the suspects

#### First suspect license id

```sql
SELECT license_id
FROM person
WHERE id = 28819
```

| license_id |
|------------|
| 173289     |

#### Second suspect license id

```sql
SELECT license_id
FROM person
WHERE id = 67318
```

| license_id |
|------------|
| 423327     |

### The culprit

With the transcript provided by Morty we got that the culprit is a male with a membership id from 'Get Fit Now Gym' that starts with '48Z', and after the murder went to a car with a plate number that contains 'H42W'.

The first fact got us two suspects: 'Joe Germuska' and 'Jeremy Bowers', we can confirm that they are the only suspects because of the transcript of Annabel, she saw the crime and confirmed that the guy who commited the murder was in the gym with her on January the 9th, by looking at the check-in information of the gym we got that these two were present in the gym that day.

And with the second fact we got only two possible cars, so then by searching for the license id of the two suspects, the first one did not correspond to any of those, but the second one matched with a car.

So in conclusion **Jeremy Bowers** is the murderer.

### Checking the solution

```sql
INSERT INTO solution VALUES (1, 'Jeremy Bowers');
SELECT value FROM solution;
```

| value |
|---|
| Congrats, you found the murderer! But wait, there's more... If you think you're up for a challenge, try querying the interview transcript of the murderer to find the real villain behind this crime. If you feel especially confident in your SQL skills, try to complete this final step with no more than 2 queries. Use this same INSERT statement with your new suspect to check your answer. |

So there's more.

![Sisyphus-e1557869810488](https://github.com/CaldeCrack/Little-Projects/assets/65932888/81f4830b-a8d1-4a2f-af85-790c24da1d49)

## The Real Villain Solution

### Interview of the Murderer

```sql
SELECT transcript
FROM interview
WHERE person_id = 67318
```

| transcript |
|---|
| I was hired by a woman with a lot of money. I don't know her name but I know she's around 5'5" (65") or 5'7" (67"). She has red hair and she drives a Tesla Model S. I know that she attended the SQL Symphony Concert 3 times in December 2017. |

### Search for the women in the drivers license registers

```sql
SELECT name
FROM person
WHERE license_id IN
  (SELECT id
  FROM drivers_license
  WHERE height BETWEEN 65 AND 67
  AND gender = 'female'
  AND hair_color = 'red'
  AND car_make = 'Tesla'
  AND car_model = 'Model S')
```

| name |
|---|
| Red Korb |
| Regina George |
| Miranda Priestly |

### Search for the women in the event

```sql
SELECT name
FROM person
WHERE id IN
  (SELECT person_id
  FROM facebook_event_checkin
  WHERE event_name = 'SQL Symphony Concert'
    AND "date" BETWEEN 20171201 AND 20171231
  GROUP BY person_id
  HAVING COUNT(person_id) = 3)
```

| name |
|---|
| Bryan Pardo |
| Miranda Priestly |

With just this query alone we got the real culprit (technically two because of the anidation but who cares this is possible in just one query).

### The true villain

Using the info of the women given by the murderer we found out that the true villain of this story is **Miranda Priestly**, since just with her three attendances at the event we got two suspects, but one of them is male so the other one is the culprit.

With the first query we couldn't do the same since we got three culprits and two were female, but it is useful to confirm the result of the second query.

### Checking the true villain

```sql
INSERT INTO solution VALUES (1, 'Miranda Priestly');
SELECT value FROM solution;
```

| value |
|---|
| Congrats, you found the brains behind the murder! Everyone in SQL City hails you as the greatest SQL detective of all time. Time to break out the champagne! |

Yayyy :D

![yippee-happy](https://github.com/CaldeCrack/Little-Projects/assets/65932888/020fede3-3e60-49e9-b1b1-d1923508641e)

