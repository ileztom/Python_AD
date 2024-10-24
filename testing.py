import pytest
from grades import calculate_average


def test_calculate_average():
    results = calculate_average('grades.csv')

    expected_results = [
        (78.25, 49.0),  # Alfalfa
        (82.75, 48.0),  # Alfred
        (55.25, 44.0),  # Gerty
        (36.5, 47.0),  # Android
        (71.5, 45.0),  # Bumpkin
        (76.0, 46.0),  # Rubble
        (14.75, 43.0),  # Noshow
        (34.0, 50.0),  # Buff
        (60.0, 83.0),  # Airpump
        (60.5, 97.0),  # Backus
        (46.25, 40.0),  # Carnivore
        (26.75, 45.0),  # Dandy
        (53.0, 77.0),  # Elephant
        (55.25, 90.0),  # Franklin
        (12.75, 4.0),  # George
        (20.25, 40.0)  # Heffalump
    ]

    for (average, final), (expected_average, expected_final) in zip(results, expected_results):
        assert round(average, 2) == expected_average, f"Expected {expected_average}, got {average}"
        assert round(final, 2) == expected_final, f"Expected {expected_final}, got {final}"
