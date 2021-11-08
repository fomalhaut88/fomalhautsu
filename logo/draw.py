import svgwrite


SIZE = 256
ALPHA = 3.0
HEIGHT = SIZE * 3 // 4
THICKNESS = SIZE // 8
COLOR = "#f50"


def draw_line(dwg, a, b):
    dwg.add(dwg.line(a, b, stroke=COLOR, stroke_width=THICKNESS))


def draw_tip(dwg, c):
    dwg.add(dwg.circle(c, THICKNESS / 2, fill=COLOR))


if __name__ == "__main__":
    width = HEIGHT / ALPHA * 3

    dwg = svgwrite.Drawing(profile='tiny', viewBox=f"0 0 {SIZE} {SIZE}")

    # Lines
    draw_line(dwg,
        (SIZE / 2 - width / 2, SIZE / 2 + HEIGHT / 2),
        (SIZE / 2 - width / 2 + HEIGHT / ALPHA, SIZE / 2 - HEIGHT / 2)
    )
    draw_line(dwg,
        (SIZE / 2 - width / 2 + HEIGHT / ALPHA, SIZE / 2 - HEIGHT / 2),
        (SIZE / 2 - width / 2 + HEIGHT / ALPHA * 2, SIZE / 2 + HEIGHT / 2)
    )
    draw_line(dwg,
        (SIZE / 2 - width / 2, SIZE / 2 + HEIGHT / 2),
        (SIZE / 2 - width / 2 + HEIGHT / ALPHA * 3, SIZE / 2 - HEIGHT / 2)
    )

    # Tips
    draw_tip(dwg,
        (SIZE / 2 - width / 2, SIZE / 2 + HEIGHT / 2)
    )
    draw_tip(dwg,
        (SIZE / 2 - width / 2 + HEIGHT / ALPHA, SIZE / 2 - HEIGHT / 2)
    )
    draw_tip(dwg,
        (SIZE / 2 - width / 2 + HEIGHT / ALPHA * 2, SIZE / 2 + HEIGHT / 2)
    )
    draw_tip(dwg,
        (SIZE / 2 - width / 2 + HEIGHT / ALPHA * 3, SIZE / 2 - HEIGHT / 2)
    )

    dwg.saveas("../frontend/src/assets/logo.svg")
