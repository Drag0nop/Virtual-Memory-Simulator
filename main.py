# main.py

import sys
from file_io.input_loader import InputLoader
from ui.cli import CLI

def main():
    """
    Entry point for the Virtual Memory Simulator.
    Usage:
        python main.py <input_file>
    Example:
        python main.py data/sample_input1.txt
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        sys.exit(1)

    input_file = sys.argv[1]
    num_frames, reference_string, algorithm = InputLoader.load_from_file(input_file)

    cli = CLI()
    cli.run_simulation(num_frames, reference_string, algorithm)

if __name__ == "__main__":
    main()
