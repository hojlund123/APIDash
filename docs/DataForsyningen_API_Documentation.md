# DataForsyningen API Documentation

**URL**: https://api.dataforsyningen.dk/postnumre

## Sample Response
```
[
    {
        "href": "https://api.dataforsyningen.dk/postnumre/1050",
        "nr": "1050",
        "navn": "K\u00f8benhavn K",
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
                "navn": "K\u00f8benhavn"
            }
        ],
        "\u00e6ndret": "2023-03-24T22:28:38.837Z",
        "geo_\u00e6ndret": "2023-03-24T22:28:38.837Z",
        "geo_version": 2,
        "dagi_id": "191050"
    },
    {
        "href": "https://api.dataforsyningen.dk/postnumre/1051",
        "nr": "1051",
        "navn": "K\u00f8benhavn K",
        "stormodtageradresser": null,
        "bbox": [
            12.58727138,
            55.67873773,
         
```

## Fields
list of dictionaries
  - **href**:     - Type: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 45
    - Median Length: 45
    - Mode Length: N/A
    - Max Length: 45
    - Min Length: 45
  - **nr**:     - Type: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 4
    - Median Length: 4
    - Mode Length: N/A
    - Max Length: 4
    - Min Length: 4
  - **navn**:     - Type: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 11
    - Median Length: 11
    - Mode Length: N/A
    - Max Length: 11
    - Min Length: 11
  - **stormodtageradresser**:     - Type: Unknown
  - **bbox**: list of items
    - Type: Number
    - Total Count: 4
    - Unique Count: 4
    - Missing Values: 0
    - Mean: 34.1332441925
    - Median: 34.13349953
    - Standard Deviation: 24.88038002905929
    - Variance: 619.0333103904123
    - Mode: 12.5841266
    - Range: 43.09772451
    - Max: 55.68185111
    - Min: 12.5841266
  - **visueltcenter**: list of items
    - Type: Number
    - Total Count: 2
    - Unique Count: 2
    - Missing Values: 0
    - Mean: 34.133326894999996
    - Median: 34.133326894999996
    - Standard Deviation: 30.47252004689151
    - Variance: 928.574478008205
    - Mode: 12.58600133
    - Range: 43.094651129999995
    - Max: 55.68065246
    - Min: 12.58600133
  - **kommuner**: list of items
    - **href**:       - Type: String
      - Total Count: 1
      - Unique Count: 1
      - Missing Values: 0
      - Average Length: 44
      - Median Length: 44
      - Mode Length: N/A
      - Max Length: 44
      - Min Length: 44
    - **kode**:       - Type: String
      - Total Count: 1
      - Unique Count: 1
      - Missing Values: 0
      - Average Length: 4
      - Median Length: 4
      - Mode Length: N/A
      - Max Length: 4
      - Min Length: 4
    - **navn**:       - Type: String
      - Total Count: 1
      - Unique Count: 1
      - Missing Values: 0
      - Average Length: 9
      - Median Length: 9
      - Mode Length: N/A
      - Max Length: 9
      - Min Length: 9
  - **ændret**:     - Type: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 24
    - Median Length: 24
    - Mode Length: N/A
    - Max Length: 24
    - Min Length: 24
  - **geo_ændret**:     - Type: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 24
    - Median Length: 24
    - Mode Length: N/A
    - Max Length: 24
    - Min Length: 24
  - **geo_version**:     - Type: Number
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Mean: 2
    - Median: 2
    - Standard Deviation: N/A
    - Variance: N/A
    - Mode: N/A
    - Range: 0
    - Max: 2
    - Min: 2
  - **dagi_id**:     - Type: String
    - Total Count: 1
    - Unique Count: 1
    - Missing Values: 0
    - Average Length: 6
    - Median Length: 6
    - Mode Length: N/A
    - Max Length: 6
    - Min Length: 6
