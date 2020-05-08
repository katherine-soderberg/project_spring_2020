
def test_input_is_csv():
    from kathodes_package import filesummary
    filename = 'sample.csv'
    output = filesummary.summarize(filename)
    assert output == "sample.csv has been summarized."
