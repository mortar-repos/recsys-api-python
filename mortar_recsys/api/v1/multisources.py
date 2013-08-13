def get_items(api, item_ids, limit=None, facet_field=None, facet_value=None):
    params = {'limit': limit}
    if facet_field and facet_value:
        params['facet.field'] = facet_field
        params['f.%s.facet.target_value' % facet_field] = facet_value
    url = 'multisources?' + ''.join(['item_id=%s&' % item_id for item_id in item_ids])
    url = url[:-1]
    return api.get(url, params)


