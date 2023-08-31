# This script is intended to run in Glyphs' Python environment
# It will create a new tab with every possible pairing of letter glyphs in the font, without spaces between them.

import string

def create_letter_pairing_tab(font):
    all_glyph_names = [glyph.name for glyph in font.glyphs]
    letter_pairs = []

    # Filter out only the letter glyphs
    letter_glyph_names = [name for name in all_glyph_names if name in string.ascii_letters]
    
    # Generate all possible pairs of letter glyphs
    for first_glyph in letter_glyph_names:
        for second_glyph in letter_glyph_names:
            pair = f"/{first_glyph}/{second_glyph}"
            letter_pairs.append(pair)

    # Create the string and open in a new tab
    letter_pairs_string = " ".join(letter_pairs)
    font.newTab(letter_pairs_string)

if __name__ == '__main__':
    font = Glyphs.font
    create_letter_pairing_tab(font)
