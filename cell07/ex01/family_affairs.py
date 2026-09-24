def find_the_redheads(family_dict):
    return [name for name, color in family_dict.items() if color == "red"]

if __name__ == "__main__":
    dupont_family = {
        "florian": "red",
        "marie": "blond",
        "virginie": "brunette",
        "david": "red",
        "franck": "red"
    }
    print(find_the_redheads(dupont_family))