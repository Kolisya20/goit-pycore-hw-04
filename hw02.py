def get_cats_info(path):
    cats_data = []

    try:
        with open(path, 'r', encoding='utf-8') as fh:
            lines = [line.strip() for line in fh.readlines()]
        for line in lines:
            id, name, age = line.split(',')
            cats_data.append({"id": id, "name": name, "age": age})
    except FileNotFoundError:
        print(f"File was not found: {path}")
    except ValueError:
        print("Data conversion error. Please check the file format.")
    except Exception as e:
        print(f"An error occurred: {e}")

    return cats_data

cats_info = get_cats_info("cats_data.txt")
print(cats_info)
