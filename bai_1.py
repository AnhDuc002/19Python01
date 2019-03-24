import library_bai_1
str_path = "config.txt"

#Read_file
print(library_bai_1.read(str_path))

#Write_file
print(library_bai_1.write(str_path))

#Delete_file
print(" ")

#get_number_of_word
print("SỐ từ: ", library_bai_1.get_number_of_word(str_path))

#get_number_of_characters
print("Số ký tự: ", library_bai_1.get_number_of_characters(str_path)

#get_the_number_of_duplicate_word
n_o_word = library_bai_1.get_number_of_word(str_path)
n_o_d_word = library_bai_1.get_the_number_of_duplicate_word(str_path)
n_o_n_d_word = int(n_o_word) - int(n_o_d_word)
print('tổng số từ không lặp lại:',n_o_n_d_word)

#get_the_number_of_duplicate_characters
n_o_character = library_bai_1.get_number_of_character(str_path)
n_o_d_character = library_bai_1.get_the_number_of_duplicate_characters(str_path)
n_o_n_d_character = int(n_o_character) - int(n_o_d_character)
print('tổng số ký tự không lặp lại:',n_o_n_d_character)


