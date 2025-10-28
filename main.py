from stats import book_word_count, char_count, get_character_count
import sys


def get_book_text(path_to_file):
	with open(path_to_file) as f:
		return f.read()

def main():
	if len(sys.argv) != 2:
	        print("Usage: python3 main.py <path_to_book>")
        	sys.exit(1)
	da_way = sys.argv[1]

	text = get_book_text(da_way)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {da_way}...")
	print("----------- Word Count ----------")
	total = book_word_count(text)
	print(f"Found {total} total words")

	counts = char_count(text)
	sorted_counts = get_character_count(counts)

	print("--------- Character Count -------")
	for item in sorted_counts:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['num']}")
	print("============= END ===============")
main()
