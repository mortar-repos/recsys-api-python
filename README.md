# recsys-api-python

The Mortar Recsys API Client for Python is a Python wrapper to interact with the Mortar Recsys API.

## Recommendations For Single Item

To get recommendations for a single item id:

```python
from mortar_recsys.api.v1.api import API
from mortar_recsys.api.v1 import items

### recsys credentials
api_id  = 'my-API-id'
api_key = 'my-API-key'

### get results
api = API(api_id, api_key)
results = items.get_items(api, item_id)
```

## Recommendations For Multiple Items

To get recommendations for multiple item ids:

```python
from mortar_recsys.api.v1.api import API
from mortar_recsys.api.v1 import multisources

### recsys credentials
api_id  = 'my-API-id'
api_key = 'my-API-key'

### get results
api = API(api_id, api_key)
results = multisources.get_items(api, [item_id1, item_id2])
```

## Recommendations For User

```python
from mortar_recsys.api.v1.api import API
from mortar_recsys.api.v1 import users

### recsys credentials
api_id  = 'my-API-id'
api_key = 'my-API-key'

### get results
api = API(api_id, api_key)
results = users.get_items(api, user_id)
```


