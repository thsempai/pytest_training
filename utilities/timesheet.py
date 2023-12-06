class TimeSheet:
    def __init__(self):
        self.lines = {}

    def add_line(self, date, hours, comment):
        if date in self.lines:
            raise KeyError(f"Date '{date}' exists in this Timesheet.")
        self.lines[date] = (hours, comment)

        #sort self.lines
        self.lines = {date: self.lines[date] for date in sorted(self.lines)}

    def update_line(self, date, hours, comment):
        if date not in self.lines:
            raise KeyError(f"Date '{date}' not found in this Timesheet.")
        
        self.lines[date] = (hours, comment)
        
    def __iter__(self):
        for date, value in self.lines.items():
            yield date, value[0], value[1]