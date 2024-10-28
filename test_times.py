from times import compute_overlap_time, time_range

def test_generic_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 10:45:00")]
    assert compute_overlap_time(large, short) == expected

def test_notOverlap_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-02-12 10:30:00", "2010-02-12 10:45:00")
    expected = []
    assert compute_overlap_time(large, short) == expected


def test_intervals_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 2, 60)
    short = time_range("2010-01-12 10:30:00", "2010-01-12 13:00:00", 2, 60)
    expected = [("2010-01-12 10:30:00","2010-01-12 10:37:00"), ("2010-01-12 10:38:00", "2010-01-12 13:00:00")]
    assert compute_overlap_time(large, short) == expected

def test_same_case():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 13:00:00")
    short = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
    expected = [("2010-01-12 10:00:00","2010-01-12 13:00:00")]
    assert compute_overlap_time(large, short) == expected