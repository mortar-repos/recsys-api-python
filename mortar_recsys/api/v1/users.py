def get_items(api, user_id, limit=None, facet_field=None, facet_value=None):
    params = {'limit': limit}
    if facet_field and facet_value:
        params['facet.field'] = facet_field
        params['f.%s.facet.target_value' % facet_field] = facet_value
    return api.get('users/%s' % user_id, params)


