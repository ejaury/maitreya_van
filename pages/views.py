from django.views.generic import DetailView, ListView, TemplateView


class PageListView(ListView):
    context_object_name = 'object_list'
    template_name = 'pages/index.html'

    def get_context_data(self, **kwargs):
        context = super(PageListView, self).get_context_data(**kwargs)
        name = self.model._meta.verbose_name_plural
        context['title'] = name.title()
        return context


class PageDetailView(DetailView):
    context_object_name = 'object'
    template_name = 'pages/view_page.html'

    def get_context_data(self, **kwargs):
        context = super(PageDetailView, self).get_context_data(**kwargs)
        obj = kwargs.get('object')
        if obj and hasattr(obj, 'title'):
            context['title'] = obj.title
        else:
            context['title'] = self.model._meta.verbose_name.title()
        return context


class ContactView(TemplateView):
    template_name = 'pages/about/location.html'
