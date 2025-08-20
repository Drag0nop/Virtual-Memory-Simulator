# ui/visualizer.py

import matplotlib.pyplot as plt

class Visualizer:
    @staticmethod
    def plot(reference_string: list, steps: list, algorithm: str):
        """
        Plot memory frames usage across simulation steps.
        - reference_string: sequence of pages accessed
        - steps: list of frame states at each step
        """
        plt.figure(figsize=(10, 6))
        for frame_index in range(len(steps[0])):
            frame_history = [step[frame_index] if frame_index < len(step) else -1 for step in steps]
            plt.plot(range(1, len(reference_string)+1), frame_history, marker="o", label=f"Frame {frame_index}")

        plt.xticks(range(1, len(reference_string)+1))
        plt.xlabel("Step")
        plt.ylabel("Page in Frame")
        plt.title(f"Page Replacement Simulation - {algorithm}")
        plt.legend()
        plt.grid(True)
        plt.show()
