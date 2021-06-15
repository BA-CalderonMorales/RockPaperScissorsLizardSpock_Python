class Player:
    # region Thoughts before starting project
    """
    As a player, the game should have an option of having a
    human go up against an AI, or a human going up against
    another human.
    """

    # endregion
    def __init__(self, real_or_artificial):
        self.player = real_or_artificial  # Can be an AI or human
        self.lives = 3  # Dictates player lives
