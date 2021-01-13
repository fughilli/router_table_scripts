import fractions

from util import FormatImproper

kFootInches = 12
board_width = 5 * kFootInches
inner_spacing = fractions.Fraction('7.75')
wall_thickness = fractions.Fraction('0.75')
num_ribs = 6
outer_spacing = (board_width - (num_ribs - 1) *
                 inner_spacing - (num_ribs + 2) * wall_thickness) / 2



print("Inner spacing:", FormatImproper(inner_spacing),
      "outer spacing:", FormatImproper(outer_spacing))

line_positions = []
line_position = fractions.Fraction('0')

line_positions.append(line_position)
line_position += wall_thickness
line_positions.append(line_position)
line_position += outer_spacing
line_positions.append(line_position)
line_position += wall_thickness
for _ in range(5):
    line_positions.append(line_position)
    line_position += inner_spacing
    line_positions.append(line_position)
    line_position += wall_thickness
line_positions.append(line_position)
line_position += outer_spacing
line_positions.append(line_position)
line_position += wall_thickness
line_positions.append(line_position)

print(''.join(['{}\n'.format(FormatImproper(_)) for _ in line_positions]))
