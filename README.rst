==========================
Wagtail Paginated Subpages
==========================

A simple Django Wagtail app to add paginated pages under a root page using
a mixin /template tag approach.

Quick start
-----------


1. Add "wagtail_paginated_subpages" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'wagtail_paginated_subpages',
    ]

2. import the mixin and include it before the Page (or other) classes::

    from wagtail_paginated_subpages.mixins.pagination import PaginatedMixin


    class ContentPage(PaginatedMixin, BaseCMSPage):

        pass

3. Use the paginated content in a paginated page template::

    {% for page in paginated_objects %}
            <h2>{{ page.title }}</h2>
        {% endfor %}
    </ul>

4. Use the pagination template tag to add pagination::

    {% load wagtail_paginated_tags %}
    {% render_pagination page=page paginated_objects=paginated_objects %}

5. Navigate to page with child pages and list of child pages should be present
