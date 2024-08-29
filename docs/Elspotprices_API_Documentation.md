# Elspotprices API Documentation

**URL**: https://api.energidataservice.dk/dataset/Elspotprices

## Fields
- **total**: value
- **limit**: value
- **dataset**: value
- **records**: list of dict
  - **HourUTC**: value
  - **HourDK**: value
  - **PriceArea**: value
  - **SpotPriceDKK**: value
  - **SpotPriceEUR**: value
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
            "HourUTC": "2024-08-29T21:00:00",
            "HourDK": "2024-08-29T23:00:00",
            "PriceArea": "SE4",
            "SpotPriceDKK": -6.04,
            "SpotPriceEUR": -0.81
        },
        {
            "HourUTC": "2024-08-29T21:00:00",
            "HourDK": "2024-08-29T23:00:00",
            "PriceArea": "SYSTEM",
            "SpotPriceDKK": 23.27,
            "SpotPriceEUR": 3.12
        },
        {
            "HourUTC": "2024-08-29T20:00:00",
            "HourDK": "2024-08-29T22:00:00",
            "PriceArea": "DK1",
            "SpotPriceDKK": 931.900024,
            "SpotPriceEUR": 124.93
        },
        {
            "HourUTC": "2024-08-29T20:00:00",
            "HourDK": "2024-08-29T22:00:00",
            "PriceArea": "DK2",
            "SpotPriceDKK": 932.429993,
            "SpotPriceEUR": 125.0
        },
        {
            "HourUTC": "2024-08-29T20:00:00",
            "HourDK": "2024-08-29T22:00:00",
            "PriceArea": "NO2",
            "SpotPriceDKK": 283.609985,
            "SpotPriceEUR": 38.02
        },
        {
            "HourUTC": "2024-08-29T20:00:00",
            "HourDK": "2024-08-29T22:00:00",
            "PriceArea": "SE3",
            "SpotPriceDKK": -0.07,
            "SpotPriceEUR": -0.01
        },
        {
            "HourUTC": "2024-08-29T20:00:00",
            "HourDK": "2024-08-29T22:00:00",
            "PriceArea": "SE4",
            "SpotPriceDKK": -0.07,
            "SpotPriceEUR": -0.01
        },
        {
            "HourUTC": "2024-08-29T20:00:00",
            "HourDK": "2024-08-29T22:00:00",
            "PriceArea": "SYSTEM",
            "SpotPriceDKK": 37.0,
            "SpotPriceEUR": 4.96
        },
        {
            "HourUTC": "2024-08-29T19:00:00",
            "HourDK": "2024-08-29T21:00:00",
            "PriceArea": "DK1",
            "SpotPriceDKK": 1238.26001,
            "SpotPriceEUR": 166.0
        },
        {
            "HourUTC": "2024-08-29T19:00:00",
            "HourDK": "2024-08-2
```

