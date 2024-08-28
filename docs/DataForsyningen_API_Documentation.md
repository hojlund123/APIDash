# DataForsyningen API Documentation

**URL**: https://api.dataforsyningen.dk/postnumre

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
            55.68095605
        ],
        "visueltcenter": [
            12.59022696,
            55.6798377
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
        "geo_version": 3,
        "dagi_id": "191051"
    },
    {
        "href": "https://api.dataforsyningen.dk/postnumre/1052",
        "nr": "1052",
        "navn": "København K",
        "stormodtageradresser": null,
        "bbox": [
            12.58736515,
            55.67813302,
            12.59274477,
            55.67957261
        ],
        "visueltcenter": [
            12.58954953,
            55.67906706
        ],
        "kommuner": [
            {
                "href": "https://api.dataforsyningen.dk/kommuner/0101",
                "kode": "0101",
                "navn": "København"
            }
        ],
        "ændret": "2023-10-03T21:40:22.645Z",
        "geo_ændret": "2023-10-03T21:40:22.645Z",
        "geo_version": 2,
        "dagi_id": "191052"
    },
    {
        "href": "https://api.dataforsyningen.dk/postnumre/1053",
        "nr": "1053",
        "navn": "København K",
        "stormodtageradresser": null,
        "bbox": [
            12.59005794,
            55.67748162,
            12.59131831,
            55.67856512
        ],
        "visueltcenter": [
            12.59073024,
            55.67798554
        ],
        "kommuner": [
            {
                "href": "https://api.dataforsyningen.dk/kommuner/0101",
                "kode": "0101",
                "navn": "København"
            }
        ],
        "ændret": "2018-04-30T15:23:13.528Z",
        "geo_ændret": "2014-11-04T16:01:00.879Z",
        "geo_version": 1,
        "dagi_id": "191053"
    },
    {
        "href": "https://api.dataforsyningen.dk/postnu
```

