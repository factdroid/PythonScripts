#! python3
# mclip.py - A multi-clipboard program

import sys, pyperclip


TEXT = {
    'agree': """Yes I agree. That sounds fine to me""",
    'busy': """Sorry, can we do this a little later? Perhaps next week?""",
    'upsell': """Would you consider making this a regular thing? We could assist you monthly"""
}

if len(sys.argv) < 2:
    print('Usage: python mclip.py[keyphrase] - copy phrase text!')
    sys.exit()


key_phrase = sys.argv[1]

if key_phrase in TEXT:
    pyperclip.copy(TEXT[key_phrase])
    print('Text for '+key_phrase+' copied to clipboard')

else:
    print("There's no text for "+ key_phrase)

