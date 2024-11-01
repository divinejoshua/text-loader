import secrets
import string
import time

target_text = "Hello world"
target_text_list = target_text.split()
existing_text_list = []
existing_text = ""
total_random_character = 1
letter_iteration_index = 0
word_iteration_index = 0




# initializing size of string

# While the extsting text and target text arent the same 
while existing_text != target_text:
    time.sleep(0.05)

    random_character = ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase)
              for i in range(total_random_character))

    print(existing_text+random_character)

    current_word = target_text_list[word_iteration_index]


    if(random_character == current_word[letter_iteration_index]):
        existing_text_list.append("")
        existing_text_list[word_iteration_index] = existing_text_list[word_iteration_index] + random_character
        letter_iteration_index = letter_iteration_index + 1

        if(target_text_list[word_iteration_index] == existing_text_list[word_iteration_index]):
            existing_text = existing_text + existing_text_list[word_iteration_index]
            word_iteration_index = word_iteration_index + 1
            current_word = target_text_list[word_iteration_index]
            letter_iteration_index = 0

            if(len(target_text) ==len(existing_text)):
                break
            else:
                existing_text = existing_text + " "
