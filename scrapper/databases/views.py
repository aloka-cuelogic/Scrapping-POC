from databases.sulekha import sulekha


def index(request):
    place = raw_input("Enter city: ").lower()
    area = raw_input(
        "Enter area (For multiple area enter ,seprated values): ").lower()

    sulekha.parse_content(place, area)
