# EnergiDataService API Documentation

**URL**: https://api.energidataservice.dk/dataset/Elspotprices

## Sample Response
```
{
    "total": 1745822,
    "limit": 100,
    "dataset": "Elspotprices",
    "records": [
        {
            "HourUTC": "2024-08-29T21:00:00",
            "HourDK": "2024-08-29T23:00:00",
            "PriceArea": "DK1",
            "SpotPriceDKK": 821.280029,
            "SpotPriceEUR": 110.099998
        },
        {
            "HourUTC": "2024-08-29T21:00:00",
            "HourDK": "2024-08-29T23:00:00",
            "PriceArea": "DK2",
            "SpotPriceDKK": 821.280029,
            "SpotPriceEUR": 110.099998
        },
        {
            "HourUTC": "2024-08-29T21:00:00",
            "HourDK": "2024-08-29T23:00:00",
            "PriceArea": "NO2",
            "SpotPriceDKK": 293.600006,
            "SpotPriceEUR": 39.360001
        },
        {
            "HourUTC": "2024-08-29T21:00:00",
            "HourDK": "2024-08-29T23:00:00",
            "PriceArea": "SE3",
            "SpotPriceDKK": -6.04,
            "SpotPriceEUR": -0.81
        },
        {
            "HourUT
```

## Fields
- **total**: Number
- **limit**: Number
- **dataset**: String
- **records**: list of Unknown
  - **HourUTC**: String
  - **HourDK**: String
  - **PriceArea**: String
  - **SpotPriceDKK**: Number
  - **SpotPriceEUR**: Number
