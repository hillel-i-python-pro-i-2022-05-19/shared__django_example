import logging

from django.views.generic import TemplateView


class Example1View(TemplateView):
    template_name = "middleware_example/page.html"

    def get_context_data(self, **kwargs):
        logging.getLogger("django").info("Some action")

        context_data = super().get_context_data(**kwargs)

        # Here some unique logic.
        context_data["message"] = "Example 1"

        return context_data


class Example2View(TemplateView):
    template_name = "middleware_example/page.html"

    def get_context_data(self, **kwargs):
        logging.getLogger("django").info("Some action")

        context_data = super().get_context_data(**kwargs)

        # Here some unique logic.
        context_data["message"] = "Example 2"

        return context_data
