import logging
from django.views.generic import TemplateView

logger = logging.getLogger(__name__)


class MainPageView(TemplateView):
    logger.info('index.html accessed!')
    template_name = 'index.html'


class AboutPageView(TemplateView):
    logger.info('about.html accessed!')
    template_name = 'about.html'
