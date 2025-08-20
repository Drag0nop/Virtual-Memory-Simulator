# algorithms/lru.py

class LRUReplacement:
    def __init__(self, num_frames: int):
        self.num_frames = num_frames
        self.frames = []
        self.page_faults = 0
        self.recent_usage = []  # Tracks order of usage

    def access_page(self, page: int):
        """
        Simulate accessing a page using LRU replacement policy.
        """
        if page not in self.frames:
            self.page_faults += 1
            if len(self.frames) < self.num_frames:
                self.frames.append(page)
            else:
                # Replace least recently used page
                lru_page = self.recent_usage.pop(0)
                self.frames.remove(lru_page)
                self.frames.append(page)
        else:
            # If page is already in memory, refresh usage order
            self.recent_usage.remove(page)

        # Always update usage order
        self.recent_usage.append(page)
        return list(self.frames)

    def get_page_faults(self):
        return self.page_faults
