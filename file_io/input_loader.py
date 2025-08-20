# io/input_loader.py

class InputLoader:
    @staticmethod
    def load_from_file(filepath: str):
        """
        Load simulation input from a text file.
        Format:
            Frames: <number>
            Reference String: <space-separated pages>
            Algorithm: <FIFO/LRU/Optimal>
        """
        num_frames = 0
        reference_string = []
        algorithm = "FIFO"

        with open(filepath, "r") as file:
            for line in file:
                if line.startswith("Frames"):
                    num_frames = int(line.split(":")[1].strip())
                elif line.startswith("Reference String"):
                    reference_string = list(map(int, line.split(":")[1].strip().split()))
                elif line.startswith("Algorithm"):
                    algorithm = line.split(":")[1].strip()

        return num_frames, reference_string, algorithm

    @staticmethod
    def load_from_input(num_frames: int, reference_string: list, algorithm: str = "FIFO"):
        """
        Directly pass input (useful for testing).
        """
        return num_frames, reference_string, algorithm
