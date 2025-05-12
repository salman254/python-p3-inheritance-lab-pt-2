# lib/chatty_student.py

from student import Student

class ChattyStudent(Student):
    def hello(self):
        # Call the parent method
        super().hello()
        # Add the additional chatty message
        print("How are you doing today? I'm okay, but I'm kind of tired. "
              "Did you watch The Walking Dead last night? You didn't?! "
              "Oh man, it was so crazy! What, you don't want any spoilers? "
              "Okay well let me just tell you who died...")

    def raise_hand(self):
        # Print the parent method 10 times
        for _ in range(10):
            super().raise_hand()
