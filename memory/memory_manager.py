# memory/memory_manager.py

class MemoryManager:
    def __init__(self, num_frames: int):
        """
        Initialize memory manager with given number of frames.
        """
        self.num_frames = num_frames
        self.frames = [-1] * num_frames  # -1 means empty frame
        self.page_table = {}  # Maps page -> frame index

    def is_page_in_memory(self, page: int) -> bool:
        """
        Check if the page is already loaded in memory.
        """
        return page in self.page_table

    def load_page(self, page: int, frame_index: int):
        """
        Load the page into the given frame index.
        """
        self.frames[frame_index] = page
        self.page_table[page] = frame_index

    def remove_page(self, page: int):
        """
        Remove a page from memory (used during replacement).
        """
        if page in self.page_table:
            frame_index = self.page_table[page]
            self.frames[frame_index] = -1
            del self.page_table[page]

    def get_frames(self):
        """
        Return the current frame contents.
        """
        return self.frames
