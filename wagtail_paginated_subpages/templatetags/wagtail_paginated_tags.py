from django import template

from .. import settings as app_settings

register = template.Library()


@register.inclusion_tag('wagtail_paginated_subpages/pagination.html', takes_context=True)
def render_pagination(context, page, paginated_objects):
    request = context['request']
    current_page_size = context['current_page_size']

    # Load app settings
    redirect_index_to_root = app_settings.PAGINATION_REDIRECT_INDEX_TO_ROOT
    default_page_sizes = app_settings.PAGINATION_DEFAULT_PAGE_SIZES
    default_page_size = app_settings.PAGINATION_PAGE_SIZE_DEFAULT

    pagination_query_string = ''
    render_prev_next = True
    if current_page_size != default_page_size:
        pagination_query_string = '?page_size={}'.format(current_page_size)
        render_prev_next = False

    return {
        'request': request,
        'page':page,
        'paginated_objects': paginated_objects,
        'default_page_size': default_page_size,
        'default_page_sizes': default_page_sizes,
        'current_page_size': current_page_size,
        'pagination_query_string': pagination_query_string,
        'render_prev_next': render_prev_next
    }


@register.inclusion_tag('wagtail_paginated_subpages/pagination_meta.html', takes_context=True)
def render_pagination_meta(context, page, paginated_objects):
    request = context['request']
    current_page_size = context['current_page_size']

    # Load app settings
    default_page_size = app_settings.PAGINATION_PAGE_SIZE_DEFAULT

    render_prev_next = True
    if current_page_size != default_page_size:
        # Non standard so alert SEO that page is non indexed and google
        render_prev_next = False

    return {
        'request': request,
        'page':page,
        'paginated_objects': paginated_objects,
        'render_prev_next': render_prev_next
    }


@register.simple_tag(takes_context=True)
def paginationpageurl(context, page, url_name, page_id, qs, *args, **kwargs):

    request = context['request']
    base_url = page.relative_url(request.site)

    if app_settings.PAGINATION_REDIRECT_INDEX_TO_ROOT and page_id == 1:
        routed_url = ''
    else:
        routed_url = page.reverse_subpage(url_name, args=(page_id,))

    return base_url + routed_url + qs
