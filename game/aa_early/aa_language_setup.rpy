init -999 python:
    import os
    if renpy.android:

        spanish_lang_file = os.path.join(config.gamedir, "language_spanish.txt")
        english_lang_file = os.path.join(config.gamedir, "language_english.txt")
        ptbr_lang_file = os.path.join(config.gamedir, "language_ptbr.txt")

        language = None
        if os.path.exists(spanish_lang_file):
            language = "spanish"
        elif os.path.exists(english_lang_file):
            language = "english"
        elif os.path.exists(ptbr_lang_file):
            language = "ptbr"
        else:
            language = "english"

        if language:
            persistent.language = language
        print("Debug")
