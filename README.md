# DBMS Assignment 2

## Query 1

```sql
SELECT COUNT(*) AS num_flights
FROM flight f
JOIN airport a_src ON f.from = a_src.airport_id
JOIN airport a_dest ON f.to = a_dest.airport_id
WHERE a_src.name = 'BORG EL ARAB INTL'
AND a_dest.name = 'LABUAN';
```

![Result](./Results/Screenshot%20from%202024-01-26%2017-05-46.png)

## Query 2

```sql
SELECT seat, AVG(price) AS AveragePricePerSeat  
FROM booking  
WHERE flight_id = 3863 AND seat IS NOT NULL  
GROUP BY seat;
```
| seat | AveragePricePerSeat |
|------|---------------------|
| 10B  |          116.88     |
| 10C  |          291.85     |
| 10D  |          340.28     |
| 10E  |          325.60     |
| 11C  |          239.53     |
| 11E  |          314.09     |
| 12A  |          115.98     |
| 12B  |          400.12     |
| 13H  |          366.26     |
| 14A  |          130.23     |
| 14B  |            9.42     |
| 14C  |          344.20     |
| 14D  |          259.62     |
| 14E  |          291.60     |
| 15B  |           33.72     |
| 15E  |          204.19     |
| 16A  |           26.42     |
| 16B  |            9.42     |
| 16G  |          388.23     |
| 16H  |          306.92     |
| 17C  |           62.05     |
| 17F  |          181.57     |
| 17H  |          324.69     |
| 18A  |          451.65     |
| 18B  |           75.91     |
| 18D  |          428.49     |
| 18G  |          274.71     |
| 19A  |          319.06     |
| 19B  |           17.47     |
| 19D  |          334.33     |
| 19H  |          500.63     |
| 1B   |          288.89     |
| 1D   |          164.70     |
| 1E   |          396.21     |
| 1G   |           91.86     |
| 20A  |          216.94     |
| 20D  |           10.46     |
| 20G  |          413.03     |
| 20H  |           21.15     |
| 21A  |          131.94     |
| 21F  |            6.23     |
| 21G  |          411.34     |
| 22C  |          264.82     |
| 22F  |          221.48     |
| 23E  |          170.03     |
| 24D  |          445.85     |
| 24F  |          275.88     |
| 24G  |          198.32     |
| 25E  |          323.15     |
| 25F  |          173.10     |
| 2D   |          479.65     |
| 2E   |          345.30     |
| 2F   |          321.60     |
| 3C   |          104.90     |
| 3G   |           31.96     |
| 3H   |          233.66     |
| 4B   |          166.44     |
| 5A   |          437.98     |
| 5D   |          197.80     |
| 5G   |          229.01     |
| 6B   |          108.49     |
| 6C   |          109.55     |
| 6E   |          466.79     |
| 6F   |          462.32     |
| 7A   |           83.04     |
| 7C   |          435.00     |
| 7E   |          211.65     |
| 7G   |          423.36     |
| 7H   |          346.47     |
| 8A   |          346.27     |
| 8B   |          328.66     |
| 8F   |          251.86     |
| 8G   |          184.47     |
| 8H   |          276.07     |
| 9C   |          329.42     |
| 9E   |          461.97     |
| 9H   |           66.52     |
77 rows in set (0.00 sec)

## Query 3

```sql
SELECT COUNT(DISTINCT t.identifier) AS airline_type_number 
FROM booking b 
JOIN flight f ON b.flight_id = f.flight_id 
JOIN airplane a ON f.airplane_id = a.airplane_id 
JOIN airplane_type t ON a.type_id = t.type_id 
WHERE b.passenger_id = 16678;
```

```sql
SELECT DISTINCT t.identifier AS airline_type 
FROM booking b 
JOIN flight f ON b.flight_id = f.flight_id 
JOIN airplane a ON f.airplane_id = a.airplane_id 
JOIN airplane_type t ON a.type_id = t.type_id 
WHERE b.passenger_id = 16678;
```
![Result](./Results/image.png)

## Query 4

### Assuming there has to be flight on that day
```sql
SELECT COUNT(DISTINCT DATE(f.departure)) AS total_dates
FROM flight f
JOIN weatherdata w ON DATE(f.departure) = w.log_date
WHERE w.humidity >= 98
AND w.airpressure > 1015;
```

![Result](./Results/Screenshot%20from%202024-01-26%2016-34-43.png)

```sql
SELECT DISTINCT DATE(f.departure) AS flight_date
FROM flight f
JOIN weatherdata w ON DATE(f.departure) = w.log_date
WHERE w.humidity >= 98
AND w.airpressure > 1015;
```

![Result](./Results/Screenshot%20from%202024-01-26%2016-37-18.png)

### Assuming it is not compulsory to have flight on that day
```sql
SELECT COUNT(DISTINCT DATE(log_date)) AS total_dates 
FROM weatherdata
WHERE humidity >= 98
AND airpressure > 1015;
```
![Result](./Results/image2.png)


## Query 5

```sql
SELECT a.airlinename, SUM(b.price) AS total_revenue
FROM flight f
JOIN booking b ON f.flight_id = b.flight_id
JOIN airline a ON f.airline_id = a.airline_id
GROUP BY f.airline_id, a.airlinename
ORDER BY total_revenue DESC;
```

| airlinename          | total_revenue |
| -------------------- | ------------- |
| Vanuatu Airlines     | 186500605.02  |
| Peru Airlines        | 176842893.21  |
| Micronesia Airlines  | 176068563.83  |
| Yugoslavia Airlines  | 174960066.71  |
| Hungary Airlines     | 174053899.30  |
| Falkland Is Airlines | 167390905.07  |
| Ethiopia Airlines    | 165680147.74  |
| Tunisia Airlines     | 160359282.37  |
| Swaziland Airlines   | 151318261.13  |
| Puerto Rico Airlines | 150947014.61  |
| Russia Airlines      | 150279679.86  |
| Cyprus Airlines      | 146508965.92  |
| India Airlines       | 146416627.60  |
| Oman Airlines        | 145843753.72  |
| Togo Airlines        | 143349695.41  |
| Brazil Airlines      | 141773200.30  |
| Croatia Airlines     | 141003939.45  |
| Namibia Airlines     | 140973701.12  |
| Yemen Airlines       | 140860452.14  |
| Western Samoa Airlin | 140825693.96  |
| Melilla Airlines     | 140028435.28  |
| Poland Airlines      | 140000337.86  |
| Sudan Airlines       | 139691865.53  |
| Haiti Airlines       | 138808619.05  |
| Equatorial Guinea Ai | 137961862.40  |
| Taiwan Airlines      | 135212119.27  |
| Bhutan Airlines      | 134488123.87  |
| Kenya Airlines       | 134181462.37  |
| Isla De Pascua Airli | 134065099.16  |
| Wake I Airlines      | 133768038.81  |
| Italy Airlines       | 133295673.19  |
| Senegal Airlines     | 133236899.71  |
| Rwanda Airlines      | 132296241.75  |
| Reunion Airlines     | 131913540.29  |
| Bahamas Airlines     | 131601031.04  |
| Estonia Airlines     | 131293607.82  |
| Solomon Is Airlines  | 129310786.07  |
| Kazakhstan Airlines  | 129253732.35  |
| Georgia Airlines     | 128345695.57  |
| Luxembourg Airlines  | 128330514.15  |
| Moldova Airlines     | 127824632.09  |
| Albania Airlines     | 127811208.54  |
| Central African Rep  | 127543511.38  |
| Myanmar Airlines     | 126558015.93  |
| Iran Airlines        | 126364527.04  |
| Ukraine Airlines     | 126143934.13  |
| Eritrea Airlines     | 125832429.24  |
| Romania Airlines     | 124695023.51  |
| Syria Airlines       | 124145094.39  |
| Argentina Airlines   | 123978697.58  |
| Nicaragua Airlines   | 123553266.05  |
| Ecuador Airlines     | 122487734.68  |
| France Airlines      | 121908463.45  |
| Afghanistan Airlines | 121861845.24  |
| Iceland Airlines     | 120956993.50  |
| El Salvador Airlines | 120304584.03  |
| Uganda Airlines      | 119936583.45  |
| Liberia Airlines     | 119815086.99  |
| Northern Mariana Is  | 119657281.98  |
| Egypt Airlines       | 118659186.28  |
| Johnston Atoll Airli | 117742313.30  |
| Australia Airlines   | 117269962.26  |
| Uzbekistan Airlines  | 117174769.97  |
| Laos Airlines        | 116812133.54  |
| Kuwait Airlines      | 116401407.92  |
| Czech Airlines       | 115332895.43  |
| Djibouti Airlines    | 115283956.51  |
| Thailand Airlines    | 114614640.31  |
| Macau Airlines       | 112856368.57  |
| Dakhla And Laayoune  | 112796811.73  |
| Jamaica Airlines     | 112733074.70  |
| Bulgaria Airlines    | 111891959.19  |
| Cuba Airlines        | 111819681.78  |
| Ghana Airlines       | 111456784.60  |
| Uruguay Airlines     | 111345245.52  |
| Kiribati Airlines    | 109765895.78  |
| Gibraltar Airlines   | 109134519.42  |
| Zimbabwe Airlines    | 108881025.77  |
| Ivory Coast Airlines | 108797004.42  |
| Chad Airlines        | 108342383.80  |
| Angola Airlines      | 108270955.88  |
| Gabon Airlines       | 108115205.99  |
| Colombia Airlines    | 108046920.34  |
| Guadeloupe Airlines  | 107847547.09  |
| St Kitts Airlines    | 107637645.57  |
| Zambia Airlines      | 107025215.36  |
| Venezuela Airlines   | 106999196.60  |
| Qatar Airlines       | 106959948.33  |
| Belarus Airlines     | 106694129.85  |
| Greece Airlines      | 105972086.48  |
| Vietnam Airlines     | 105322846.88  |
| Caicos Is Airlines   | 105113560.63  |
| Fiji Is Airlines     | 104780227.15  |
| Nepal Airlines       | 104662635.73  |
| San Andres Airlines  | 100438539.48  |
| Denmark Airlines     | 99846345.92   |
| United Arab Emirates | 98466939.36   |
| Honduras Airlines    | 96861862.82   |
| Jerusalem Airlines   | 96524586.96   |
| Kyrgyzstan Airlines  | 95394332.98   |
| Azerbaijan Airlines  | 93437435.89   |
| Trinidad Airlines    | 92151164.74   |
| American Samoa Airli | 90272244.63   |
| Dominica Airlines    | 90011042.95   |
| Sierra Leone Airline | 89710725.02   |
| Spain Airlines       | 88407522.66   |
| Lebanon Airlines     | 85505124.30   |
| Sri Lanka Airlines   | 80677455.80   |
| Korea Airlines       | 79315606.21   |
| Bolivia Airlines     | 78216416.93   |
| Slovakia Airlines    | 53111779.36   |
| Pakistan Airlines    | 52233889.18   |
| Philippines Airlines | 46027452.10   |
