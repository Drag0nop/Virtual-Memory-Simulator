# algorithms/fifo.py

from collections import deque

class FIFOReplacement:
    def __init__(self, num_frames: int):
        self.num_frames = num_frames
        self.frames = []
        self.page_faults = 0
        self.queue = deque()

    def access_page(self, page: int):
        """
        Simulate accessing a page using FIFO replacement policy.
        """
        if page not in self.frames:
            self.page_faults += 1
            if len(self.frames) < self.num_frames:
                self.frames.append(page)
                self.queue.append(page)
            else:
                victim = self.queue.popleft()
                self.frames.remove(victim)
                self.frames.append(page)
                self.queue.append(page)
        return list(self.frames)

    def get_page_faults(self):
        return self.page_faults
