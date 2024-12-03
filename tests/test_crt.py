import pytest
from src.crt import retro_filter
from PIL import Image as im
import numpy as np
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt


def is_similar(im1: np.ndarray, im2: np.ndarray, threshold: float = 0.99) -> bool:
    similarity_index, diff = ssim(im1, im2, full=True, channel_axis=2)

    if similarity_index < threshold:
        plt.imshow(im1)
        plt.show()
        plt.imshow(im2)
        plt.show()
        plt.imshow(diff, cmap="gray")
        plt.title("Difference Image")
        plt.show()
        print(f"Image failed, similarity index: {similarity_index}")
    return similarity_index > threshold


def test_jpeg_crt():
    pinguin_result = retro_filter(
        ".\\tests\\test_images\\Pinguin.jpg", curvature=1.00, vignette_width=5
    )
    pinguin_answer = np.array(im.open(".\\tests\\test_images\\Pinguin_check.jpg"))
    assert is_similar(
        pinguin_result, pinguin_answer, 0.94
    ), "penguin.png failed the test"

    eebee_result = retro_filter(
        ".\\tests\\test_images\\Eebee.jpg",
        curvature=3.00,
        scanline_val=10,
        vignette_width=20,
    )
    eebee_answer = np.array(im.open(".\\tests\\test_images\\Eebee_check.jpg"))
    assert is_similar(eebee_answer, eebee_result, 0.94), "Eebee.jpg failed the test"


def test_png_crt():
    whomp_fortress_result = retro_filter(
        ".\\tests\\test_images\\whomp_fortress.png", curvature=4.00, vignette_width=50
    )
    whomp_fortress_answer = np.array(
        im.open(".\\tests\\test_images\\whomp_fortress_check.png")
    )
    assert is_similar(
        whomp_fortress_result, whomp_fortress_answer, 0.94
    ), "whomp_fortress.png failed the test"

    teletubies_result = retro_filter(
        ".\\tests\\test_images\\teletubbies.png", curvature=3.00, vignette_width=100
    )
    teletubies_answer = np.array(
        im.open(".\\tests\\test_images\\teletubbies_check.png")
    )
    assert is_similar(
        teletubies_result, teletubies_answer, 0.94
    ), "teletubbies.png failed the test"
