from factorio import blueprints
import os
import re
import time

def strip_illegal_fs_chars(in_string):
    """
    Strip all characters that are illegal in a windows file name

    List of characters can be found here
    https://support.microsoft.com/en-us/help/905231/information-about-the-characters-that-you-cannot-use-in-site-names--fo
    """
    sanitized_string = re.sub(r'[~#%&*{}\\:<>?/+|"]','_',in_string)
    if sanitized_string in ["", ".", ".."]:
        sanitized_string = "bp_" + time.time()
    return sanitized_string

def archive_blueprint(e_string):
    """Save a blueprint or blueprint book exchange string into individual json files"""
    blob = blueprints.EncodedBlob().from_exchange_string(e_string)
    label=strip_illegal_fs_chars(blob.label)

    if blob.item == "blueprint":
        blob.to_json_file(label+".json")
    elif blob.item == "blueprint-book":
        book = blueprints.BlueprintBook(blob)
        try:
            os.mkdir(label)
        except FileExistsError:
            print("Blueprint Book {0} already exists. Adding new blueprints to it, and overwriting duplicates.".format(label))
            print("WARNING:  Old blueprints are not removed!")
        os.chdir(label)
        for bp in book.blueprints:
            bp.to_json_file(strip_illegal_fs_chars(bp.label)+".json")
        os.chdir('..')
    else:
        raise RuntimeError("Exchange_String is neither a blueprint or a blueprint book")

bp_file = open('Exchange Strings.txt')
for e_string in bp_file:
    e_string = e_string.strip()
    # Skip empty lines and comments
    if e_string == "" or e_string.find('#') == 0:
        continue
    archive_blueprint(e_string)
