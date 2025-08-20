# ui/cli.py

from file_io.input_loader import InputLoader
from file_io.logger import Logger
from algorithms.fifo import FIFOReplacement
from algorithms.lru import LRUReplacement
from algorithms.optimal import OptimalReplacement
from ui.visualizer import Visualizer

class CLI:
    def __init__(self):
        self.logger = Logger()

    def run_simulation(self, num_frames: int, reference_string: list, algorithm: str):
        """
        Run simulation using selected algorithm with grid-style visualization.
        """
        algo = None
        if algorithm.upper() == "FIFO":
            algo = FIFOReplacement(num_frames)
        elif algorithm.upper() == "LRU":
            algo = LRUReplacement(num_frames)
        elif algorithm.upper() == "OPTIMAL":
            algo = OptimalReplacement(num_frames, reference_string)
        else:
            print(f"Unknown algorithm: {algorithm}")
            return

        print(f"\n=== Running {algorithm.upper()} Simulation ===\n")

        frame_history = []
        page_faults = []

        for step, page in enumerate(reference_string, 1):
            prev_frames = list(algo.frames)
            frames = algo.access_page(page)
            page_fault = (frames != prev_frames or page not in prev_frames)

            # Log step
            self.logger.log_step(step, page, frames, page_fault)

            # Save for visualization
            frame_history.append(list(frames))
            page_faults.append(page_fault)

        # Log summary
        total_faults = algo.get_page_faults()
        self.logger.log_summary(total_faults, len(reference_string))

        # Show visualization
        Visualizer.plot(reference_string, frame_history, page_faults, algorithm.upper())
