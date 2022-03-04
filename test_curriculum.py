"""
Unit tests for the curriculum class
"""

from curriculum import Course, Curriculum


def test_init():
    '''testing init'''
    test_curr = Curriculum()
    assert (test_curr.university == "" and
            test_curr.degree_name == "" and
            test_curr.course_dict == {})


def test_init_values():
    '''testing initiating with given values'''
    x = Course()
    y = Course(course_code=4567, prerequisites=[x])
    test_curr = Curriculum("TAMS",
                           "High School Diploma with Honors",
                           [x, y])
    assert (test_curr.university == "TAMS" and
            test_curr.degree_name == "High School Diploma with Honors" and
            # course_dict will use a Course object as a key and list of prereqs
            # which will help with adding each key to a graph later.
            test_curr.course_dict["NONE 0"] == x and
            test_curr.course_dict["NONE 4567"] == y)


def test_prereq_recursion():
    '''Scenario:
       Course y is added with prereq x, prereq x is not in dict.
       expectation is x should also be added to the dict.'''
    x = Course()
    y = Course(prerequisites=[x])
    test_curr = Curriculum(course_list=[y])
    assert (str(test_curr.course_dict[str(x)]) == str(x) and
            str(test_curr.course_dict[str(y)]) == str(y))


def test_num_courses():
    x = Course()
    y = Course(course_code=4567, prerequisites=[x])
    test_curr = Curriculum()
    test_curr2 = Curriculum(course_list=[x, y])
    assert (test_curr.num_courses() == 0 and
            test_curr2.num_courses() == 2)
