import numpy as np
from PIL import Image as im
from numpy import ndarray

from src.smoothstep import smoothstep


def retro_filter(
    input_image: str | np.ndarray,
    curvature: int | float = 2,
    vignette_width: int | float = 10,
    scanline_val: int | float | None = None,
) -> ndarray[int | ndarray[int]]:
    """Takes a rgb image or path to image and adds a CRT effect to it.

    Parameters:
        input_image (str | np.ndarray): Image to be processed or path to that image.
        curvature (int | float): Curvature intensity, smaller values give a greater curvature.
        vignette_width (int | float): Width of the vignette.
        scanline_val (int | float | None): Periodicity of the scan lines, is set to image height when left empty.

    Returns:
        numpy.ndarray: numpy array containing pixels of the image with CRT effects added.
    """

    if isinstance(input_image, str):
        opened_image = im.open(input_image)
        image = np.array(opened_image)
    elif isinstance(input_image, np.ndarray):
        image = input_image
    else:
        return NotImplemented

    new_image = np.zeros_like(image)

    screenheight, screenwidth, channels = image.shape
    if scanline_val is None:
        scanline_val = screenheight

    # Makes a meshgrid of the pixel coordinates so calculations can be done on each pixel
    y_coords, x_coords = np.meshgrid(
        np.arange(screenheight), np.arange(screenwidth), indexing="ij"
    )

    # Create uv map of the coordinates for easier calculations.
    uv = np.stack(
        (y_coords / (screenheight - 1), x_coords / (screenwidth - 1)), axis=-1
    )

    uv = uv * 2 - 1  # Centers the uv map so it spans from -1 to 1.
    offset = (
        uv / curvature
    )  # Creates curvature map. Values in the center are close to zero and curve less than values at the borders which are closer to 1 or -1
    uv += uv * offset * offset  # Adds curved uv coordinates to the uv map.
    inverted_uv = 1 - np.abs(
        uv
    )  # Gets inverted uv coordinates for later use in the vignette
    uv = uv * 0.5 + 0.5  # Converts the uv coordinates back to a range from 0 to 1.

    y = uv[..., 0] * (screenheight - 1)
    x = uv[..., 1] * (screenwidth - 1)

    y = np.clip(y.astype(int), 0, screenheight - 1)
    x = np.clip(x.astype(int), 0, screenwidth - 1)

    # A vignette mask is made by taking the inverted uv map, where the values at the edge are closer to 0 and
    # values at the center closer to 1, and disperse the values between the edges and the vignette border.
    vignette_vector = np.array(
        [vignette_width / screenheight, vignette_width / screenwidth]
    )
    vignette = smoothstep(inverted_uv, 0, vignette_vector)

    # waves that oscillate the RGB values a little, creating the illusion of scan lines.
    sin_vals = np.sin(y_coords * scanline_val + 1) * 0.15 + 1
    cos_vals = np.cos(y_coords * scanline_val + 1) * 0.10 + 1

    new_image[..., 0] = np.clip(
        image[y, x, 0] * sin_vals * vignette[..., 0] * vignette[..., 1], 0, 255
    )
    new_image[..., 1] = np.clip(
        image[y, x, 1] * cos_vals * vignette[..., 0] * vignette[..., 1], 0, 255
    )
    new_image[..., 2] = np.clip(
        image[y, x, 2] * sin_vals * vignette[..., 0] * vignette[..., 1], 0, 255
    )
    return new_image[..., :3].copy()
