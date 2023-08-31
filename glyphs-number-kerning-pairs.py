# This script is intended to run in Glyphs' Python environment.
# It will create a new tab with every possible pairing of number glyphs in the font, without spaces between them.

def create_number_pairing_tab(font):
    all_glyph_names = [glyph.name for glyph in font.glyphs]
    number_pairs = []

    # Filter out only the number glyphs
    number_glyph_names = [name for name in all_glyph_names if name in ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']]
    
    # Generate all possible pairs of number glyphs
    for first_glyph in number_glyph_names:
        for second_glyph in number_glyph_names:
            pair = f"/{first_glyph}/{second_glyph}"
            number_pairs.append(pair)

    # Create the string and open in a new tab
    number_pairs_string = " ".join(number_pairs)
    font.newTab(number_pairs_string)

if __name__ == '__main__':
    font = Glyphs.font
    create_number_pairing_tab(font)
