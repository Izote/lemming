from .client import client


def save(input_list, table):
    ipa, description = [ui.get() for ui in input_list[0]]
    lit = ipa

    ipa_char, lit_char = ["ʼ", "ʔ", "ʃ"], ["'", "'", "x"]
    for i in range(len(ipa_char)):
        lit = lit.replace(ipa_char[i], lit_char[i])

    row = {"ipa": ipa, "transliteration": lit, "description": description}

    client.table(table).insert(row).execute()
