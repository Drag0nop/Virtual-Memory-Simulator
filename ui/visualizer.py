# ui/visualizer.py

# import matplotlib.pyplot as plt

# class Visualizer:
#     @staticmethod
#     def plot(reference_string: list, steps: list, algorithm: str):
#         """
#         Plot memory frames usage across simulation steps.
#         - reference_string: sequence of pages accessed
#         - steps: list of frame states at each step
#         """
#         plt.figure(figsize=(10, 6))
#         for frame_index in range(len(steps[0])):
#             frame_history = [step[frame_index] if frame_index < len(step) else -1 for step in steps]
#             plt.plot(range(1, len(reference_string)+1), frame_history, marker="o", label=f"Frame {frame_index}")

#         plt.xticks(range(1, len(reference_string)+1))
#         plt.xlabel("Step")
#         plt.ylabel("Page in Frame")
#         plt.title(f"Page Replacement Simulation - {algorithm}")
#         plt.legend()
#         plt.grid(True)
#         plt.show()

# ui/visualizer.py

import matplotlib.pyplot as plt
import numpy as np

class Visualizer:
    @staticmethod
    def plot(reference_string: list, frame_history: list, page_faults: list, algorithm: str):
        """
        Grid-style visualization of memory frames for page replacement.
        - reference_string: sequence of pages accessed
        - frame_history: list of frame states at each step
        - page_faults: list of bools indicating page faults
        - algorithm: algorithm name
        """
        num_steps = len(reference_string)
        num_frames = len(frame_history[0])

        fig, ax = plt.subplots(figsize=(num_steps * 0.7, num_frames * 0.7))
        ax.set_xlim(0, num_steps)
        ax.set_ylim(0, num_frames)

        # Draw grid
        for i in range(num_frames + 1):
            ax.axhline(i, color='black', linewidth=1)
        for j in range(num_steps + 1):
            ax.axvline(j, color='black', linewidth=1)

        # Fill cells with page numbers
        for step in range(num_steps):
            for frame in range(num_frames):
                page = frame_history[step][frame] if frame < len(frame_history[step]) else ""
                color = "lightcoral" if page_faults[step] else "lightgreen"
                ax.text(step + 0.5, num_frames - frame - 0.5, str(page),
                        ha='center', va='center', fontsize=12,
                        bbox=dict(facecolor=color, edgecolor='black', boxstyle='round,pad=0.3'))

        ax.set_xticks(np.arange(num_steps) + 0.5)
        ax.set_xticklabels(reference_string)
        ax.set_yticks([])
        ax.set_title(f"{algorithm} Page Replacement Simulation", fontsize=14)
        ax.set_xlabel("Reference String Steps")
        plt.show()
