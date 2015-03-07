# -*- coding: utf-8 -*-
from drf_pdf import renderer


class TestRenderer(object):
    """Test for DRF-PDF Renderer"""

    def test_render(self, pdf_file_sample):

        with open(pdf_file_sample, 'r') as f:
            file_data = f
            ret = renderer.PDFRenderer().render(file_data)

        assert ret == file_data
