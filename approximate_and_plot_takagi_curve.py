from typing import Callable, Final, Union, Tuple
from typing_extensions import TypeAlias

Number: TypeAlias = Union[float, int]
TriangleWaveFunction: TypeAlias = Callable[[float], Number]
IntervalEndPoints: TypeAlias = Tuple[Number, Number]


def calculate_triangle_wave_at_specific_point(argument: float) -> Number:
    if argument.is_integer():
        return 0
    floor: int = int(argument) - int(argument < 0)
    distance: float = argument - floor
    CUTOFF_POINT: Final[float] = 0.5
    IS_CLOSER_TO_FLOOR: Final[bool] = distance < CUTOFF_POINT
    solution: Number = (1 - distance, distance)[int(IS_CLOSER_TO_FLOOR)]
    return solution


def approximate_takagi_curve_at_specific_point(
    argument: float,
    *,
    precision: int = 10**3,
    trianlge_wave_function: TriangleWaveFunction = calculate_triangle_wave_at_specific_point,
) -> Number:
    power_of_two: Number = 0.5
    from functools import reduce

    solution: float = reduce(
        lambda x, y: x + y,
        [
            trianlge_wave_function((power_of_two := power_of_two * 2) * argument)
            / power_of_two
            for _ in precision * "."
        ],
    )
    return solution


def plot_takagi_curve() -> None:
    import numpy as np
    import matplotlib.pyplot as plt

    STEP_LENGTH: Final[float] = 1e-4

    interval_end_points_of_plot: IntervalEndPoints = (0, 1)

    x = np.arange(
        interval_end_points_of_plot[0], interval_end_points_of_plot[1], STEP_LENGTH
    )
    y = list(map(approximate_takagi_curve_at_specific_point, x))

    plt.plot(x, y)
    plt.xlabel("x")
    plt.ylabel("blanc(x)")
    plt.show()


if __name__ == "__main__":
    plot_takagi_curve()
