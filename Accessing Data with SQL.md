1. Check which city of Taiwan is included in the database.
```sql
SELECT *
FROM city_list
WHERE country LIKE '%Tai%'
```
> Kaohsiung, Taichung, Taipei

2. Access the data of Taipei City in the city_data tables.
```sql
SELECT *
FROM city_data
Where city = 'Taipei';
```
> Please check the Taipei.csv

3. Access the gobal_data.
```sql


```
