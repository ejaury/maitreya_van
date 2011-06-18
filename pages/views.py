from django.views.generic import DetailView, ListView, TemplateView


class ContextDataMixin(object):
    def get_context_data(self, **kwargs):
        context = super(ContextDataMixin, self).get_context_data(**kwargs)
        name = self.model._meta.verbose_name_plural
        context['title'] = name.title()
        return context


class PageListView(ContextDataMixin, ListView):
    context_object_name = 'object_list'
    template_name = 'pages/index.html'


class PageDetailView(ContextDataMixin, DetailView):
    context_object_name = 'object'
    template_name = 'pages/view_page.html'


class ContactView(TemplateView):
    template_name = 'pages/about/contact_us.html'
