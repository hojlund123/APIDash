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
- **records**: list
  - **List Headers**:
    - **HourUTC**: String
      - Total Count: 100
      - Unique Count: 17
      - Missing Values: 0
      - Average Length: 19
      - Median Length: 19.0
      - Mode Length: N/A
      - Max Length: 19
      - Min Length: 19
    - **HourDK**: String
      - Total Count: 100
      - Unique Count: 17
      - Missing Values: 0
      - Average Length: 19
      - Median Length: 19.0
      - Mode Length: N/A
      - Max Length: 19
      - Min Length: 19
    - **PriceArea**: String
      - Total Count: 100
      - Unique Count: 6
      - Missing Values: 0
      - Average Length: 3.48
      - Median Length: 3.0
      - Mode Length: 3
      - Max Length: 6
      - Min Length: 3
    - **SpotPriceDKK**: Number
      - Total Count: 100
      - Unique Count: 49
      - Missing Values: 0
      - Mean: 410.35579674
      - Median: 337.7250065
      - Standard Deviation: 243.79381516284144
      - Variance: 59435.424311653696
      - Mode: 366.549988
      - Range: 910.939983
      - Max: 918.919983
      - Min: 7.98
    - **SpotPriceEUR**: Number
      - Total Count: 100
      - Unique Count: 49
      - Missing Values: 0
      - Mean: 55.01189995
      - Median: 45.2749995
      - Standard Deviation: 32.68273652256225
      - Variance: 1068.1612666032245
      - Mode: 49.139999
      - Range: 122.12000200000001
      - Max: 123.190002
      - Min: 1.07
