def __str__(self):
        return f"Device: {self.name!r} ({self.connected_by})"
        # !r prints out the __repr__ version of the name
    