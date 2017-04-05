# Deterministic Finite Automaton

matrix = []
final_states = []

letter_count = 0
state_count = 0
final_states_count = 0


def read_file(file_path):
    file = open(file_path)

    file_buffer = file.read()
    file_tokens = file_buffer.split()

    start_state = int(file_tokens[0])

    letter_count = int(file_tokens[1])
    final_states_count = int(file_tokens[2])

    for i in range(3, int(final_states_count + 3)):
        final_states.append(file_tokens[i])

    file_tokens = file_tokens[3 + final_states_count:len(file_tokens)]
    state_count = len(file_tokens) / letter_count

    for i in range(int(state_count)):
        current_state_transitions = []
        for j in range(letter_count):
            current_state_transitions.append(file_tokens[i * letter_count + j])

        matrix.append(current_state_transitions)

    return start_state


def move(current_state, string):

    if len(string) != 0:
        current_letter = string[0];
        current_id = int(ord(current_letter) - ord('a'))

        if matrix[int(current_state)][current_id] != '_':
            return move(matrix[int(current_state)][current_id], string[1:])
        else:
            return False

    else:
        if current_state in final_states:
            return True
        else:
            return False


def main():
    start_state = read_file('automata1')
    print("current state : ", start_state)
    print(move(start_state, 'aaba'))


if __name__ == '__main__':
    main()
