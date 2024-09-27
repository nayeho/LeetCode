class MyCalendarTwo:

    def __init__(self):
        self.ranges = []
        self.overlaps = []

    def book(self, start: int, end: int) -> bool:
        for s, e in self.overlaps:
            if max(start, s) < min(end, e):
                return False

        for s, e in self.ranges:
            ss = max(start, s)
            ee = min(end, e)
            if ss < ee:
                self.overlaps.append((ss, ee))

        self.ranges.append((start, end))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)