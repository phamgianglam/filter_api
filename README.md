# filter_api

## Introduction 
This is filter record api endpoint which is responsible for record all filter
which used to fetch products from product service 

## Design
This services currently have three operation:
- GET /filter: which is use for all recorded filter.

- POST /product: Add an filter to database.

### GET /filter:
-   page and size are paging param.

-   Sample return data:
```json
[  
  {
    "id": "f3f03831-9027-48b6-952d-28b74e24c8dd",
    "search": [
      "name:vpn",
      "name:remote"
    ],
    "sort": "price:asc",
    "price": "20-50",
    "date": "2022-01-01T13:40:40.603227"
  }
]
```

### POST /filter
- Sample request data:
```json
{
  "search": [
    "name:vpn",
    "name:remote"
  ],
  "sort": "price:asc",
  "price": "20-50",
  "date": "2022-01-01T13:40:40.603227"
}
```