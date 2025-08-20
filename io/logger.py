# io/logger.py

import os

class Logger:
    def __init__(self, output_dir="data/results"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def log_step(self, step: int, page: int, frames: list, page_fault: bool):
        """
        Print a step of the simulation.
        """
        fault_status = "Yes" if page_fault else "No"
        print(f"Step {step:<3} | Page {page:<3} | Frames: {frames} | Page Fault: {fault_status}")

    def log_summary(self, total_faults: int, total_references: int):
        """
        Print final summary.
        """
        hits = total_references - total_faults
        print("\n=== Simulation Summary ===")
        print(f"Total References : {total_references}")
        print(f"Total Page Faults: {total_faults}")
        print(f"Total Hits       : {hits}")
        print(f"Hit Ratio        : {hits/total_references:.2f}")
        print(f"Fault Ratio      : {total_faults/total_references:.2f}")

    def save_summary(self, filename: str, total_faults: int, total_references: int):
        """
        Save results into a text file.
        """
        filepath = os.path.join(self.output_dir, filename)
        hits = total_references - total_faults
        with open(filepath, "w") as f:
            f.write("=== Simulation Summary ===\n")
            f.write(f"Total References : {total_references}\n")
            f.write(f"Total Page Faults: {total_faults}\n")
            f.write(f"Total Hits       : {hits}\n")
            f.write(f"Hit Ratio        : {hits/total_references:.2f}\n")
            f.write(f"Fault Ratio      : {total_faults/total_references:.2f}\n")
        print(f"\nResults saved to {filepath}")
