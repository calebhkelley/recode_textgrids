import textgrid
import os

def recode_syllable_final_s(file_path, output_dir, words_list):
    # Load the TextGrid
    tg = textgrid.TextGrid.fromFile(file_path)

    # Words are in the first tier and phonemes in the second tier
    words_tier = tg[0]
    phonemes_tier = tg[1]

    # Iterate over the words
    for word_interval in words_tier:
        word = word_interval.mark
        word_lower = word.lower()
        # Check if the lowercase version of the word is in the list
        for target_word in words_list:
            if word_lower == target_word.lower():
                # Find the position of capitalized 'S' in the word
                s_positions = [i for i, char in enumerate(target_word) if char == 'S']

                # Find corresponding phonemes
                start_time, end_time = word_interval.minTime, word_interval.maxTime
                phonemes = [phoneme for phoneme in phonemes_tier if start_time <= phoneme.minTime < end_time]

                # Change the specific 's' phoneme(s) to '*s'
                for pos in s_positions:
                    if pos < len(phonemes) and phonemes[pos].mark == 's':
                        phonemes[pos].mark = '*s'
                break  # Exit the loop once the word is found and processed

    # Save the modified TextGrid
    output_path = os.path.join(output_dir, os.path.basename(file_path))
    tg.write(output_path)

# Directory paths
input_dir = '/Users/calebkelley/PhonicData_1oct2023/aligned_txt_grids/test_nov21/'
output_dir = '/Users/calebkelley/PhonicData_1oct2023/aligned_txt_grids/test_nov21/new/'

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# List of words with capitalized 'S'
words_list = ['eS', 'consiSte', 'pequeñoS', 'criStaleS', 'loS', 'formaS', 'geométricaS', 
              'caracteríSticaS', 'fractaleS', 'copoS', 'eStán', 'compueStoS', 'pequeñaS', 
              'partículaS', 'áSperaS', 'eStructura', 'atmóSfera', 'gradoS', 'centígradoS', 
              'poSteriormente']

# Process each TextGrid file in the directory
for filename in os.listdir(input_dir):
    if filename.endswith('.TextGrid'):
        file_path = os.path.join(input_dir, filename)
        recode_syllable_final_s(file_path, output_dir, words_list)
