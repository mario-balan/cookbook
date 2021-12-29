import pytest

@pytest.fixture
def example_people_data():
    return [
        {
            "given_name": "Mario",
            "family_name": "Balan",
            "title": "Mid-Senior Software Engineer",
        },
        {
            "given_name": "Mariana",
            "family_name": "Gigliotti",
            "title": "Vice-President of Fun Ops",
        },
    ]

def test_format_data_for_display(example_people_data):
    assert format_data_for_display(example_people_data) == [
        "Mario Balan: Mid-Senior Software Engineer",
        "Mariana Gigliotti: Vice-President of Fun Ops",
    ]

def test_format_data_for_excel(example_people_data):
    assert format_data_for_excel(example_people_data) == """given,family,title
Mario,Balan,Mid-Senior Software Engineer
Mariana,Gigliotti,Vice-President of Fun Ops
"""
