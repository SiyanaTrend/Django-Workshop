from django import template

register = template.Library()


@register.simple_tag(takes_context=True)
def url_query_append(context, field, value):
    query_params = context['request'].GET.copy()  # request.GET is read-only, that why use copy()
    query_params[field] = value
    # {'text': 'bella', 'page': 1} -> ?text=bella&page=1
    return query_params.urlencode()
