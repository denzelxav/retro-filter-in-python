import pytest
from src.crt import retro_filter
from PIL import Image as im


def jpeg_crt_test():
    pinguin_result = im.open(retro_filter(".\\test_images\\Pinguin.jpg", curvature=1.00, vignette_width=5))
    pinguin_answer = im.open(".\\test_images\\Pinguin_check.jpg")
    assert pinguin_result == pinguin_answer