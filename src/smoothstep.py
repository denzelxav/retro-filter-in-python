from typing import overload, Union

from numpy import ndarray, clip


@overload
def smoothstep(
    value: float, low_bound: float | ndarray, upp_bound: float | ndarray
) -> float:
    ...


@overload
def smoothstep(
    value: ndarray, low_bound: float | ndarray, upp_bound: float | ndarray
) -> ndarray:
    ...


def smoothstep(
    value: Union[float, ndarray],
    low_bound: float | ndarray,
    upp_bound: float | ndarray,
) -> Union[float, ndarray]:
    """Spreads values from the input array"""

    value = clip((value - low_bound) / (upp_bound - low_bound), 0, 1)
    return value * value * (3.0 - 2.0 * value)
