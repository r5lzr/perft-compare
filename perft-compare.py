sample_txt = """
b2b9: 3768821
b2b3: 3768822
g2g3: 3472039
d5d6: 3835265
a2a4: 4387586
g2g4: 3338154
g2h3: 3819456
d5e6: 4727437
c3b1: 3996171
c3d1: 3995761
c3a4: 4628497
c3b5: 4317482
e5d3: 3288812
e5c4: 3494887
e5g4: 3415992
e5c6: 4083458
e5g6: 3949417
e5d7: 4404043
e5f7: 4164923
d2c1: 3793390
d2e3: 4407041
d2f4: 3941257
d2g5: 4370915
d2h6: 3967365
e2d1: 3074219
e2f1: 4095479
e2d3: 4066966
e2c4: 4182989
e2b5: 4032348
e2a6: 3553501
a1b1: 3827454
a1c1: 3814203
a1d1: 3568343
h1f1: 3685756
h1g1: 3989454
f3d3: 3949570
f3e3: 4477772
f3g3: 4669768
f3h3: 5067173
f3f4: 4327936
f3g4: 4514010
f3f5: 5271134
f3h5: 4743335
f3f6: 3975992
e1d1: 3559113
e1f1: 3377351
e1g1: 4119629
e1c1: 3551583
"""

stockfish_txt = """
a2a3: 4627439
b2b3: 3768824
g2g3: 3472039
d5d6: 3835265
a2a4: 4387586
g2g4: 3338154
g2h3: 3819456
d5e6: 4727437
c3b1: 3996171
c3d1: 3995761
c3a4: 4628497
c3b5: 4317482
e5d3: 3288812
e5c4: 3494887
e5g4: 3415992
e5c6: 4083458
e5g6: 3949417
e5d7: 4404043
e5f7: 4164923
d2c1: 3793390
d2e3: 4407041
d2f4: 3941257
d2g5: 4370915
d2h6: 3967365
e2d1: 3074219
e2f1: 4095479
e2d3: 4066966
e2c4: 4182989
e2b5: 4032348
e2a6: 3553501
a1b1: 3827454
a1c1: 3814203
a1d1: 3568344
h1f1: 3685756
h1g1: 3989454
f3d3: 3949570
f3e3: 4477772
f3g3: 4669768
f3h3: 5067173
f3f4: 4327936
f3g4: 4514010
f3f5: 5271134
f3h5: 4743335
f3f6: 3975992
e1d1: 3559113
e1f1: 3377351
e1g1: 4119629
e1c1: 3551583
"""


def parse_txt(text):
    move_node = {}

    move_node_array = text.strip().split("\n")

    for line in move_node_array:
        move, nodes = line.split(": ")
        move_node[move] = int(nodes)

    return move_node


def display_results(sample_perft, stockfish_perft):
    all_moves = sorted(set(sample_perft.keys()) | set(stockfish_perft.keys()))

    max_move_length = max(len(move) for move in all_moves)
    max_count_length = max(
        max(len(str(count)) for count in sample_perft.values()),
        max(len(str(count)) for count in stockfish_perft.values()),
    )
    min_column_width = max(max_count_length, len("SAMPLE"))

    header_format = f"{{move:<{max_move_length}}} | {{sample:<{min_column_width}}} | {{stockfish:<{min_column_width}}}"

    move = "MOVE"
    sample = "SAMPLE"
    stockfish = "STOCKFISH"
    print(header_format.format(move=move, sample=sample, stockfish=stockfish))

    line_format = f"{{move_type:<{max_move_length}}} | {{sample_nodes:<{min_column_width}}} | {{stockfish_nodes:<{min_column_width}}}"

    for move in all_moves:
        sample_count = sample_perft.get(move, "N/A")
        stockfish_count = stockfish_perft.get(move, "N/A")
        print(
            line_format.format(
                move_type=move,
                sample_nodes=sample_count,
                stockfish_nodes=stockfish_count,
            )
        )


def compare_perft(sample_perft, stockfish_perft):
    all_moves = sorted(set(sample_perft.keys()) | set(stockfish_perft.keys()))

    differences = []

    for move in all_moves:
        if move not in sample_perft:
            differences.append(f"{move} is in stockfish but not in sample")
        elif move not in stockfish_perft:
            differences.append(f"{move} is in sample but not in stockfish")
        elif sample_perft[move] != stockfish_perft[move]:
            differences.append(
                f"{move}: sample ({sample_perft[move]}) not equal to stockfish ({stockfish_perft[move]})"
            )

    if differences:
        print("Differences found:")
        for diff in differences:
            print(diff)
    else:
        print("No differences found, moves and nodes are equal.")


sample_perft = parse_txt(sample_txt)
stockfish_perft = parse_txt(stockfish_txt)

print()
display_results(sample_perft, stockfish_perft)
print()

compare_perft(sample_perft, stockfish_perft)
