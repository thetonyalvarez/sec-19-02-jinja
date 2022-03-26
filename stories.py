"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, words, text):
        """Create story with words and template text."""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story_1 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)
story_2 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """A good vacation place is one where you can ride {adjective} {plural_noun}, {verb} and see a {noun}. Try going to {place}."""
)
story_3 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Today I went to the zoo at {place} I saw a {adjective} {noun} with {plural_noun}, so I {verb}."""
)
story_4 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """My fabulous camp group went to {place} amusement park. It was a
{adjective} park with lots of cool {plural_nouns}
and enjoyable {noun}. And I {verb}."""
)
story_5 = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """When I go to the {place} with my {plural_noun} there are lots of games to play. I spend
lots of time there with my friends. In the game X-Men
you can be a {noun} . The
point of the game is to {verb} every
robot. You also need to save {adjective} people. Then you can
go to the next level. """
)
