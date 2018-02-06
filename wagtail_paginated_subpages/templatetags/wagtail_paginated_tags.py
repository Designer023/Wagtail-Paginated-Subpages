from django import template

from .. import settings as app_settings

register = template.Library()


def render_pagination(context, page, paginated_objects):
    """
    Manages the context and logic to create the necessary pagination
    :param context: page context
    :param page: Page: The root page with the child pages
    :param paginated_objects: List of paginated sub page objects
    :return: template vars to create paginated template
    """
    request = context['request']
    current_page_size = context['current_page_size']

    # Load app settings
    default_page_sizes = app_settings.PAGINATION_DEFAULT_PAGE_SIZES
    default_page_size = app_settings.PAGINATION_PAGE_SIZE_DEFAULT

    pagination_query_string = ''
    render_prev_next = True
    if current_page_size != default_page_size:
        pagination_query_string = '?page_size={}'.format(current_page_size)
        render_prev_next = False

    return {
        'request': request,
        'page': page,
        'paginated_objects': paginated_objects,
        'default_page_size': default_page_size,
        'default_page_sizes': default_page_sizes,
        'current_page_size': current_page_size,
        'pagination_query_string': pagination_query_string,
        'render_prev_next': render_prev_next
    }


def paginationpageurl(context, page, url_name, page_id, qs):
    """
    Enhanced version  of wagtails own 'routablepageurl' that adds handling
    for the routing of page 1 and
    :param context: page context
    :param page: Page: The root page with the child pages
    :param url_name: sting: the url named pattern for paginated pages
    :param page_id: int: he paginated page number
    :param qs: string: Optional query string for handling page sizes
    :return: string: url for the paginated page
    """
    request = context['request']
    base_url = page.relative_url(request.site)

    # Check if /page/1/ is being routed to the root page or
    # if root page is routed to /page/1/ and set the sub_page_url
    if app_settings.PAGINATION_REDIRECT_INDEX_TO_ROOT and page_id == 1:
        sub_page_url = ''
    else:
        sub_page_url = page.reverse_subpage(url_name, args=(page_id,))

    # Return full page url with sub page routing and querystring
    return base_url + sub_page_url + qs


register.inclusion_tag(
    'wagtail_paginated_subpages/pagination.html',
    takes_context=True,
    name='render_pagination'
)(render_pagination)


register.inclusion_tag(
    'wagtail_paginated_subpages/pagination_meta.html',
    takes_context=True,
    name='render_pagination_meta'
)(render_pagination)


register.simple_tag(
    takes_context=True
)(paginationpageurl)
