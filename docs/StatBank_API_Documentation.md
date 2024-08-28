# StatBank API Documentation

**URL**: https://api.statbank.dk/v1/tables

## Sample Response
```
[
    {
        "id": "FOLK1A",
        "text": "Befolkningen den 1. i kvartalet",
        "unit": "Antal",
        "updated": "2024-08-12T08:00:00",
        "firstPeriod": "2008K1",
        "latestPeriod": "2024K3",
        "active": true,
        "variables": [
            "område",
            "køn",
            "alder",
            "civilstand",
            "tid"
        ]
    },
    {
        "id": "FOLK1AM",
        "text": "Befolkningen den 1. i måneden",
        "unit": "Antal",
        "updated": "2024-08-12T08:00:00",
        "firstPeriod": "2021M10",
        "latestPeriod": "2024M07",
        "active": true,
        "variables": [
            "område",
            "køn",
            "alder",
            "tid"
        ]
    },
    {
        "id": "BEFOLK1",
        "text": "Befolkningen 1. januar",
        "unit": "Antal",
        "updated": "2024-02-12T08:00:00",
        "firstPeriod": "1971",
        "latestPeriod": "2024",
        "active": true,
        "variables": [
   
```

## Fields
list of dictionaries
  - **id**: String
  - **text**: String
  - **unit**: String
  - **updated**: String
  - **firstPeriod**: String
  - **latestPeriod**: String
  - **active**: Number
  - **variables**: list of String
