from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!

class Artifact(Actor):
    
    def __init__(self):
        """Constructs a new Artifact."""
        super().__init__()
        self._point = 1
    
    def set_point(self, point):
        """Set the points for artifacts.
        Args:
            value (int): The given point value."""
        self._point = point

    def get_point(self):
        """gets the points value of Artifact.
        Returns:
            value (int): The artifact's point value."""
        return self._point    

        

    

    