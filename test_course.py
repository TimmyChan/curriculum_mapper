"""
Unit tests for the course class
"""

from curriculum import Course


def test_init():
    x = Course()
    assert (x.subject_code == "DATA" and x.course_code == 1234 and
            x.course_title == "Hello" and
            x.course_description == "From the other side" and
            x.prerequisites == [])


def test_init_with_param():
    x = Course()
    y = Course("DSCS", 5679, "To the left",
               "Everything you own", [x])
    assert (y.subject_code == "DSCS" and
            y.course_code == 5679 and
            y.course_title == "To the left" and
            y.course_description == "Everything you own" and
            y.prerequisites == [x])


def test_str():
    x = Course()
    assert str(x) == "DATA 1234"


def test_add_prereq():
    x = Course()
    y = Course("DSCS", 5679, "To the left", "Everything you own")
    y.add_prereq(x)
    assert y.prerequisites == [x]


def test_add_prereq_type():
    x = Course()
    x.add_prereq(5)
    assert x.prerequisites == []
