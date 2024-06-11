# EnergiDataService API Documentation

**URL**: https://api.energidataservice.dk/dataset/Elspotprices

## Sample Response
```
{
    "total": 1732551,
    "limit": 100,
    "dataset": "Elspotprices",
    "records": [
        {
            "HourUTC": "2024-06-11T21:00:00",
            "HourDK": "2024-06-11T23:00:00",
            "PriceArea": "DK1",
            "SpotPriceDKK": 366.549988,
            "SpotPriceEUR": 49.139999
        },
        {
            "HourUTC": "2024-06-11T21:00:00",
            "HourDK": "2024-06-11T23:00:00",
            "PriceArea": "DK2",
            "SpotPriceDKK": 366.549988,
            "SpotPriceEUR": 49.139999
        },
        {
            "HourUTC": "2024-06-11T21:00:00",
            "HourDK": "2024-06-11T23:00:00",
            "PriceArea": "NO2",
            "SpotPriceDKK": 337.540009,
            "SpotPriceEUR": 45.25
        },
        {
            "HourUTC": "2024-06-11T21:00:00",
            "HourDK": "2024-06-11T23:00:00",
            "PriceArea": "SE3",
            "SpotPriceDKK": 366.549988,
            "SpotPriceEUR": 49.139999
        },
        {
            "Hou
```

## Fields
- **total**: Number
  - Total Count: 1
  - Unique Count: 1
  - Missing Values: 0
  - Mean: 1732551
  - Median: 1732551
  - Standard Deviation: N/A
  - Variance: N/A
  - Mode: N/A
  - Range: N/A
  - Max: 1732551
  - Min: 1732551
- **limit**: Number
  - Total Count: 1
  - Unique Count: 1
  - Missing Values: 0
  - Mean: 100
  - Median: 100
  - Standard Deviation: N/A
  - Variance: N/A
  - Mode: N/A
  - Range: N/A
  - Max: 100
  - Min: 100
- **dataset**: String
  - Total Count: 1
  - Unique Count: 1
  - Missing Values: 0
  - Average Length: 12
  - Median Length: 12
  - Mode Length: N/A
  - Max Length: 12
  - Min Length: 12
- **records**: list of dictionaries
  - **HourUTC**: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 19
    - Median Length: 19
    - Mode Length: N/A
    - Max Length: 19
    - Min Length: 19
  - **HourDK**: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 19
    - Median Length: 19
    - Mode Length: N/A
    - Max Length: 19
    - Min Length: 19
  - **PriceArea**: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 3
    - Median Length: 3
    - Mode Length: N/A
    - Max Length: 3
    - Min Length: 3
  - **SpotPriceDKK**: Number
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Mean: 366.549988
    - Median: 366.549988
    - Standard Deviation: N/A
    - Variance: N/A
    - Mode: N/A
    - Range: N/A
    - Max: 366.549988
    - Min: 366.549988
  - **SpotPriceEUR**: Number
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Mean: 49.139999
    - Median: 49.139999
    - Standard Deviation: N/A
    - Variance: N/A
    - Mode: N/A
    - Range: N/A
    - Max: 49.139999
    - Min: 49.139999
