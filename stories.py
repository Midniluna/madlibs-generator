"""Madlibs Stories."""

# List of stories:
# stories = ["Test1", "test2", "test3", "test4", "test5"]

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
        """'words' must be a list, text is the story contents"""

        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


story = Story(
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

# story2 = Story(
#     ["place", "noun", "verb", "adjective", "plural_noun"],
#     """Once upon a time in a long-ago {place}, there lived a
#        large {adjective} {noun}. It loved to {verb} {plural_noun}."""
# )

# story1 = Story(["occupation", "noun", "verb", "adjective", "noun", "verb", "adjective", "noun", "verb", "noun"], """Today a {occupation} named {noun} came to our school to talk to us about her job. She said the most important skill you need to know to do her job is to be able to {verb} around (a) {adjective} {noun}. She said it was easy for her to learn her job because she loved to {verb} when she was my age--and that helps a lot! If you're considering her profession, I hope you can be near (a) {adjective} {noun}. That's very important! If you get too distracted in that situation you won't be able to {verb} next to (a) {noun}!""")