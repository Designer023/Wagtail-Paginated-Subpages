==========================
Wagtail Paginated Subpages
==========================

A simple Django Wagtail app to add paginated pages under a root page using
a mixin /template tag approach.

Adds paginated urls under and page where the mixin is used::

    /the-original-page/
    /the-original-page/page/1/
    /the-original-page/page/99/

Quick start
-----------

1. Install "wagtail-paginated-subpages" using pip::

    pip install wagtail-paginated-subpages

2. Add "wagtail_paginated_subpages" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'wagtail_paginated_subpages',
    ]

3. import the mixin and include it before the Page (or other) classes::

    from wagtail_paginated_subpages.mixins.pagination import PaginatedMixin

    class ContentPage(PaginatedMixin, Page):

        pass

4. Use the paginated content in a paginated page template::

    <ul>
        {% for page in paginated_objects %}
            <h2>{{ page.title }}</h2>
        {% endfor %}
    </ul>

5. Use the pagination template tag to add pagination::

    {% load wagtail_paginated_tags %}
    {% render_pagination page=page paginated_objects=paginated_objects %}

6. Navigate to page with child pages and list of child pages should be present


Customisation
-------------

By default page 1 is automatically redirected to the base page url
(for SEO). This can be updated to redirect the base page to /page/1/ if
preferred::

    PAGINATION_REDIRECT_INDEX_TO_ROOT = True # redirects /page/1/ to page.url
    PAGINATION_REDIRECT_INDEX_TO_ROOT = False # redirects page.url to /page/1/

Pages are paginated by 12::

    PAGINATION_PAGE_SIZE_DEFAULT = 99 # Number of items per page

Page size options to show in the 'Show:' list::

    PAGINATION_DEFAULT_PAGE_SIZES = [12, 24, 48, 96] # Options for page sizes


By default the mixin returns all child pages for the current page, however
this query can be changed by defining a get_child_page_queryset::

    class ContentPage(PaginatedMixin, BaseCMSPage):

        def get_child_page_queryset(self):
            return self.get_children().live().order_by('-first_published_at')

Pagination markup can be customised by creating a new template in::

    templates/wagtail_paginated_subpages/pagination.html

By design the list of child pages has not been designed as a template tags as
there are too many ways to style the lists of content for it to be worthwhile.
These can be updated by simply updating the markup from step 3.

Canonical meta tags can be added to the page header using::

    {% load wagtail_paginated_tags %}
    {% render_pagination_meta page=page paginated_objects=paginated_objects %}

