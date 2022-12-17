class GameStat:
    """Track statistics for Alien Invasion."""
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_status()

    def reset_status(self):
        """Initialize statistics that can change during the game."""
        self.ship_left = self.ai_settings.ship_limit
