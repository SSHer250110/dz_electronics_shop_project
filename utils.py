from pathlib import Path

ROOT_PATH = Path(__file__).parent
FILE_CSV = ROOT_PATH.joinpath("src", "items.csv")
FILE_TEST_CSV = ROOT_PATH.joinpath("tests", "items_test.csv")
EXC_FILE_TEST_CSV = ROOT_PATH.joinpath("tests", "items_test_exception.csv")
