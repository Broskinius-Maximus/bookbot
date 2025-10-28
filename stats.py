def book_word_count(da_book):
        string_count = da_book.split()
        count = len(string_count)
        return count

def char_count(text:str):
	lowercase = text.lower()
	char_dict = {}
	for ch in lowercase:
		if ch not in char_dict:
			char_dict[ch] = 0
		char_dict[ch] += 1
	return char_dict

def sort_dict(item):
        return item["num"]

def get_character_count(char_dict):
	char_count_list = []
	for character, value in char_dict.items():
		balls = {"char":character,"num":value}
		char_count_list.append(balls)
	char_count_list.sort(key=sort_dict, reverse=True)
	return char_count_list
