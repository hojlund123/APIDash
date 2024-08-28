# DataForsyningen API Documentation

**URL**: https://api.dataforsyningen.dk/postnumre

## Sample Response
```
[
    {
        "href": "https://api.dataforsyningen.dk/postnumre/1050",
        "nr": "1050",
        "navn": "København K",
        "stormodtageradresser": null,
        "bbox": [
            12.5841266,
            55.67871944,
            12.58827962,
            55.68185111
        ],
        "visueltcenter": [
            12.58600133,
            55.68065246
        ],
        "kommuner": [
            {
                "href": "https://api.dataforsyningen.dk/kommuner/0101",
                "kode": "0101",
                "navn": "København"
            }
        ],
        "ændret": "2023-03-24T22:28:38.837Z",
        "geo_ændret": "2023-03-24T22:28:38.837Z",
        "geo_version": 2,
        "dagi_id": "191050"
    },
    {
        "href": "https://api.dataforsyningen.dk/postnumre/1051",
        "nr": "1051",
        "navn": "København K",
        "stormodtageradresser": null,
        "bbox": [
            12.58727138,
            55.67873773,
            12.59417472,
         
```

## Fields
list of dictionaries
  - **href**: String
  - **nr**: String
  - **navn**: String
  - **stormodtageradresser**: Unknown
  - **bbox**: list of Number
  - **visueltcenter**: list of Number
  - **kommuner**: list of Unknown
    - **href**: String
    - **kode**: String
    - **navn**: String
  - **ændret**: String
  - **geo_ændret**: String
  - **geo_version**: Number
  - **dagi_id**: String
