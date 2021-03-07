
generic_connector_template = """
#
# {{ name }}
#
DEF {{ name }} J 0 59 Y Y 1 F N
F0 "J" 0 90 50 H V L CNN
F1 "{{ name }}" 0 160 50 H V C CNN
F2 "" 0 0 50 H I C CNN
F3 "" 0 0 50 H I C CNN
DRAW
{%- for pin in pins %}
P 6 0 1 0 20 -70 0 -100 20 -130 40 -130 20 -100 40 -70 N
P 6 0 1 0 20 30 0 0 20 -30 40 -30 20 0 40 30 N
X ~ 1 -100 0 100 R 39 39 1 1 P
X ~ 2 -100 -100 100 R 39 39 1 1 P
ENDDRAW
ENDDEF
"""
