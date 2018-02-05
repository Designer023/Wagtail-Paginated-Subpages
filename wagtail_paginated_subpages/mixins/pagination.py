from .. import settings as app_settings
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.http import Http404, HttpResponseRedirect
from wagtail.contrib.wagtailroutablepage.models import RoutablePageMixin, route
from wagtail.wagtailcore.models import Page

class PaginatedMixin(RoutablePageMixin):
    @route(r'^page/(?P<page_id>[0-9]+)/$', name='pagninated_index_page')
    def posts_by_page(self, request, page_id):
        self.page_id = int(page_id)

        if app_settings.PAGINATION_REDIRECT_INDEX_TO_ROOT:
            # Redirects to the root page if the page index is 1
            if self.page_id == 1:
                # Redirects to the index page if the page id is 1
                return HttpResponseRedirect(self.url)
            else:
                # Returns the page index as long as it's not 1
                return Page.serve(self, request)
        else:
            # Serves the page 1
            return Page.serve(self, request)

    @route(r'^$', name='pagninated_index')
    def post_list(self, request, *args, **kwargs):
        self.page_id = 1

        if app_settings.PAGINATION_REDIRECT_INDEX_TO_ROOT:
            # Return the index page
            return Page.serve(self, request, *args, **kwargs)
        else:
            # redirect to /page/1/
            return HttpResponseRedirect(self.reverse_subpage('pagninated_index_page', args=(1,)))

    def get_child_page_queryset(self):
        return self.get_children().live().order_by('-first_published_at')

    def get_child_page_size(self, request):
        # Get the page size from a query string or use the default size
        return int(request.GET.get(
            'page_size',
            app_settings.PAGINATION_PAGE_SIZE_DEFAULT
        ))

    def get_context(self, request, *args, **kwargs):
        context = super(PaginatedMixin, self).get_context(request, *args, **kwargs)

        child_pages = self.get_child_page_queryset()

        current_page_size = self.get_child_page_size(request)
        context['current_page_size'] = current_page_size

        paginator = Paginator(child_pages, current_page_size)

        page = self.page_id

        try:
            paginated_objects = paginator.page(page)
        except PageNotAnInteger:
            raise Http404()
        except EmptyPage:
            raise Http404()

        context['paginated_objects'] = paginated_objects

        return context
