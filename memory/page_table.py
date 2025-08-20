# memory/page_table.py

class PageTable:
    def __init__(self):
        """
        Initialize an empty page table.
        """
        self.table = {}  # Maps page -> frame index

    def add_entry(self, page: int, frame_index: int):
        """
        Add or update a page table entry.
        """
        self.table[page] = frame_index

    def remove_entry(self, page: int):
        """
        Remove an entry from the page table.
        """
        if page in self.table:
            del self.table[page]

    def get_frame_index(self, page: int):
        """
        Return the frame index for a given page, or None if not present.
        """
        return self.table.get(page)

    def contains(self, page: int) -> bool:
        """
        Check if the page is in the page table.
        """
        return page in self.table

    def get_table(self):
        """
        Return the entire page table.
        """
        return dict(self.table)
