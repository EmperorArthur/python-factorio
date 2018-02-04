from factorio import blueprints
import os

def append_exchange_string(in_blob, out_file_handle):
    """Convert a blueprint or book to an exchange string, and append it to a file"""
    blueprint_string = in_blob.to_exchange_string()
    out_file_handle.write("#"+in_blob.label+":\n")
    out_file_handle.write(blueprint_string)
    out_file_handle.write('\n\n')

def exchange_blueprints(archive_dir, exchange_file_name):
    """Convert a blueprint archive into exchange strings and store them in the exchange file"""
    exchange_file = open(exchange_file_name, 'w')
    for file_folder in os.scandir(archive_dir):
        if file_folder.is_file() and os.path.splitext(file_folder.name)[1] == ".json":
            blueprint = blueprints.EncodedBlob().from_json_file(file_folder.path)
            print("Creating exchange string for blueprint     :  " + blueprint.label)
            append_exchange_string(blueprint,exchange_file)
        if file_folder.is_dir():
            book=blueprints.BlueprintBook()
            book.set_name(file_folder.name)
            print("Creating exchange string for blueprint book:  " + book.label)
            for json_file in os.scandir(file_folder.path):
                if json_file.is_file() and os.path.splitext(json_file.name)[1] == ".json":
                    blueprint = blueprints.EncodedBlob().from_json_file(json_file.path)
                    print("  Adding blueprint:  " + blueprint.label)
                    book.add_blueprint(blueprint)
                    book.update('version',blueprint.version)
            append_exchange_string(book,exchange_file)
            
exchange_blueprints('.', 'Exchange Strings.txt')