# recsys-api-python

The Mortar Recsys API Client for Python is a Python wrapper to interact with the Mortar Recsys API.

## Recommendations For Single Item

To get recommendations for a single item id:

```python
from recsys.api.v1 import API
from recsys.api.v1 import items

### recsys credentials
email = 'myemail@me.org'
api_key = 'my-API-key'

### get results
api = API(email, api_key)
results = items.get_items(api, item_id)
```

## Recommendations For Multiple Items

To get recommendations for multiple item ids:

```python
from recsys.api.v1 import API
from recsys.api.v1 import multisources

### recsys credentials
email = 'myemail@me.org'
api_key = 'my-API-key'

### get results
api = API(email, api_key)
results = multisources.get_items(api, [item_id1, item_id2])
```

## Recommendations For User

```python
from recsys.api.v1 import API
from recsys.api.v1 import users

### recsys credentials
email = 'myemail@me.org'
api_key = 'my-API-key'

### get results
api = API(email, api_key)
results = users.get_items(api, user_id)
```


