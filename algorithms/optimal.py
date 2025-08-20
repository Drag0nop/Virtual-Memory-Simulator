# algorithms/optimal.py

class OptimalReplacement:
    def __init__(self, num_frames: int, reference_string: list):
        self.num_frames = num_frames
        self.frames = []
        self.page_faults = 0
        self.reference_string = reference_string
        self.current_index = 0

    def access_page(self, page: int):
        """
        Simulate accessing a page using Optimal replacement policy.
        """
        if page not in self.frames:
            self.page_faults += 1
            if len(self.frames) < self.num_frames:
                self.frames.append(page)
            else:
                # Find the page to replace: the one used farthest in the future
                farthest_use = -1
                victim = None
                for f in self.frames:
                    if f not in self.reference_string[self.current_index+1:]:
                        victim = f
                        break
                    else:
                        next_use = self.reference_string[self.current_index+1:].index(f)
                        if next_use > farthest_use:
                            farthest_use = next_use
                            victim = f

                self.frames.remove(victim)
                self.frames.append(page)

        self.current_index += 1
        return list(self.frames)

    def get_page_faults(self):
        return self.page_faults
