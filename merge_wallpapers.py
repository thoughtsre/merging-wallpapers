from screeninfo import get_monitors
from PIL import Image

def print_section(msg: str, divider: str = "#"*50):
    print("\n")
    print(divider)
    print(msg)
    print(divider)

    return

if __name__ == "__main__":

    wallpapers = []

    print_section("Getting monitor information.\nPlease enter paths to wallpapers accordingly.")

    for i, m in enumerate(get_monitors()):

        print("\n")
        print("---- Monitor {} ----".format(i + 1))
        print(m)

        aspect_ratio = m.width / m.height

        print("\n")
        print("---- Monitor Description ----")
        if (aspect_ratio > 1):
            print("This monitor is in landscape mode.")
        else:
            print("This monitor is in portrait mode.")

        if (m.x == 0):
            print("This is the left-most monitor.")

        if (m.y == 0):
            print("This monitor is at the bottom.")

        print("\n")
        p = input("Enter path to wallpaper for this monitor:\n")

        wallpapers.append((m, p))

    max_width = max([_[0].width + _[0].x for _ in wallpapers])
    max_height = max([_[0].height + _[0].y for _ in wallpapers])

    print_section("Final Wallpaper Dimensions")
    print(f"Width: {max_width}")
    print(f"Height: {max_height}")


    print_section("Generating merged wallpaper")

    final_wallpaper = Image.new("RGBA", (max_width, max_height))

    for m, p in wallpapers:

        with Image.open(p) as im:

            print(f"Imputing {p} for {m}")

            im_ = im.resize((m.width, m.height))

            final_wallpaper.paste(im_, (m.x, m.y))

    print_section("Writing output")
    try:
        final_wallpaper.save("output.png")
    except e:
        raise e
    else:
        print("Output successfully written!")



