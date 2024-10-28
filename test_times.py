from times import compute_overlap_time, time_range
import pytest

import pytest

@pytest.mark.parametrize("large, short, expected", [
    # Generic case
    (
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
        [("2010-01-12 10:30:00", "2010-01-12 10:37:00"), 
         ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    ),
    # No overlap case
    (
        time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
        time_range("2010-02-12 10:30:00", "2010-02-12 10:45:00"),
        []
    ),
    # Intervals case
    (
        time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00", 2, 60),
        time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00", 2, 60),
        time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00", 2, 60)
    ),
    # Same time range case
    (
        time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
        time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
        [("2010-01-12 12:00:00", "2010-01-12 13:00:00")]
    ),
    # End first case
    (
        time_range("2010-01-12 13:00:00", "2010-01-12 12:00:00"),
        time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00"),
        [("2010-01-12 12:00:00", "2010-01-12 13:00:00")]
    )
])
def test_compute_overlap_time(large, short, expected):
    assert compute_overlap_time(large, short) == expected