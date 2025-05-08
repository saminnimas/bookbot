from stats import (count_words, 
                   count_characters, 
                   create_report_dict,
                   sort_report_dict)
import sys


def get_book_text(filepath: str):
    file_contents = ''
    with open(filepath, encoding="utf8") as f:
        file_contents = f.read()

    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_content = get_book_text(str(sys.argv[1]))
        num_words = count_words(book_content)
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {str(sys.argv[1])}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        print("--------- Character Count -------")

        report_dict = create_report_dict(count_characters(book_content))
        sorted_report_dict = sort_report_dict(report_dict)

        for dicts in sorted_report_dict:
            print(f"{dicts['char']}: {dicts['num']}")
        print("============= END ===============")


if __name__ == '__main__':
    main()