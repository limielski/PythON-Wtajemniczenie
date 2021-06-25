import re


def run_example():
    number_at_begin_txt = "+48 123 456 789 <- to jest numer"
    number_pattern = re.compile(r"\+(\d{2})((?: \d{3}){3})")
    number_match = number_pattern.search(number_at_begin_txt)
    print(number_match.group())

    number_at_end_txt = "To jest numer -> +48 123 456 789"
    number_match = number_pattern.search(number_at_end_txt)
    print(number_match.group())


if __name__ == "__main__":
    run_example()
