# tables API Documentation

**URL**: https://api.statbank.dk/v1/tables

## Fields
list of dictionaries
  - **id**: value
  - **text**: value
  - **unit**: value
  - **updated**: value
  - **firstPeriod**: value
  - **latestPeriod**: value
  - **active**: value
  - **variables**: list of value
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
            "køn",
            "alder",
            "civilstand",
            "tid"
        ]
    },
    {
        "id": "BEFOLK2",
        "text": "Befolkningen 1. januar",
        "unit": "Antal",
        "updated": "2024-02-12T08:00:00",
        "firstPeriod": "1901",
        "latestPeriod": "2024",
        "active": true,
        "variables": [
            "køn",
            "alder",
            "tid"
        ]
    },
    {
        "id": "FOLK3",
        "text": "Befolkningen 1. januar",
        "unit": "Antal",
        "updated": "2024-02-12T08:00:00",
        "firstPeriod": "2008",
        "latestPeriod": "2024",
        "active": true,
        "variables": [
            "fødselsdag",
            "fødselsmåned",
            "fødselsår",
            "tid"
        ]
    },
    {
        "id": "FOLK3FOD",
        "text": "Befolkningen 1. januar",
        "unit": "Antal",
        "updated": "2024-02-12T08:00:00",
        "firstPeriod": "2008",
        "latestPeriod": "2024",
        "active": true,
        "variables": [
            "fødselsdag",
            "fødselsmåned",
            "fødeland",
            "tid"
        ]
    },
    {
        "id": "BEF5",
        "text": "Befolkningen 1. januar",
        "unit": "Antal",
        "updated": "2024-02-12T08:00:00",
        "firstPeriod": "1990",
        "latestPeriod": "2024",
        "active": true,
        "variables": [
            "køn",
            "alder",
            "fødeland",
            "tid"
        ]
    },
    {
        "id": "FT",
        "text": "Befolkningen (summariske tal fra folketællinger)",
        "unit": "Antal",
        "updated": "2024-02-12T08:00:00",
        "firstPeriod": "1769",
        "latestPeriod": "2024",
        "active": true,
        "variables": [
            "hovedlandsdele",
            "tid"
        ]
    },
    {
        "id": "HISB3",
        "text": "Nøgletal om befolkningen",
        "unit": "Antal",
        "updated": "2024-02-12T08:00:00",
        "firstPeriod": "1901"
```

