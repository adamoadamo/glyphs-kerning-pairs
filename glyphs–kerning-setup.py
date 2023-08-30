# Intended to run in Glyphs' Python environment

# Define some special cases as constants
SPECIAL_PAIRS = [
    ('W', 'A'),
    ('A', 'V'),
    ('T', 'o'),
    # ... add more special cases
]

def analyze_metrics(font):
    cap_height = font.selectedFontMaster.capHeight
    x_height = font.selectedFontMaster.xHeight
    baseline = 0
    descender = font.selectedFontMaster.descender
    return cap_height, x_height, baseline, descender

def set_side_bearings(glyph):
    # Example logic: set side bearings based on glyph width
    width = glyph.width
    if width < 200:
        glyph.LSB = 20
        glyph.RSB = 20
    elif 200 <= width < 500:
        glyph.LSB = 30
        glyph.RSB = 30
    else:
        glyph.LSB = 40
        glyph.RSB = 40

def calculate_ideal_spacing(left_glyph, right_glyph, cap_height, x_height):
    # Special Cases
    if (left_glyph.name, right_glyph.name) in SPECIAL_PAIRS:
        return -20

    # Generic Logic
    return 0

def analyze_kerning_for_glyphs(font, cap_height, x_height):
    all_glyph_names = [glyph.name for glyph in font.glyphs]
    kerning_dict = {}
    
    # Setting side bearings for each glyph
    for glyph_name in all_glyph_names:
        glyph = font.glyphs[glyph_name]
        set_side_bearings(glyph)
        
    for left_glyph_name in all_glyph_names:
        for right_glyph_name in all_glyph_names:
            left_glyph = font.glyphs[left_glyph_name]
            right_glyph = font.glyphs[right_glyph_name]
            ideal_spacing = calculate_ideal_spacing(left_glyph, right_glyph, cap_height, x_height)

            # Handling Kerning Groups
            left_kerning_group = left_glyph.leftKerningGroup
            right_kerning_group = right_glyph.rightKerningGroup
            kerning_key = (left_kerning_group or left_glyph_name, right_kerning_group or right_glyph_name)

            # Update the dictionary
            kerning_dict[kerning_key] = ideal_spacing
    
    return kerning_dict

if __name__ == '__main__':
    font = Glyphs.font
    cap_height, x_height, baseline, descender = analyze_metrics(font)
    
    print(f"Cap Height: {cap_height}")
    print(f"x-Height: {x_height}")
    print(f"Baseline: {baseline}")
    print(f"Descender Depth: {descender}")

    kerning_dict = analyze_kerning_for_glyphs(font, cap_height, x_height)
    
    # Sample output
    print("Sample Kerning Pairs:")
    for pair, value in list(kerning_dict.items())[:10]:
        print(f"{pair}: {value}")
