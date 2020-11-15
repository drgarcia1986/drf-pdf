# coding: utf-8
from rest_framework.renderers import BaseRenderer


class PDFRenderer(BaseRenderer):

    """ Renderer for PDF binary content. """

    media_type = 'application/pdf'
    format = 'pdf'
    charset = 'ISO-8859-2'
    render_style = 'binary'

    def render(self, data, media_type=None, renderer_context=None):
        """
        Return the PDF data as it is
        """
        return data
