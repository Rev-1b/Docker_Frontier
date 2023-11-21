class TitleOffcanvasMixin:
    title = None
    show_offcanvas = True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = self.title
        context['show_offcanvas'] = self.show_offcanvas

        return context