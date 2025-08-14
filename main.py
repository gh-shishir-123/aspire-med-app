from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

questions = [
    {
        "question": "ভিটামিন D কোথায় তৈরি হয়?",
        "options": ["লিভার", "ত্বক", "কিডনি", "অগ্ন্যাশয়"],
        "answer": "ত্বক"
    },
    {
        "question": "মানবদেহে সবচেয়ে বড় অঙ্গ কোনটি?",
        "options": ["ত্বক", "লিভার", "ফুসফুস", "হৃদপিণ্ড"],
        "answer": "ত্বক"
    }
]

class MCQScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', **kwargs)
        self.index = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_widgets()
        q = questions[self.index]
        self.add_widget(Label(text=q["question"], font_size=24))
        for option in q["options"]:
            btn = Button(text=option, font_size=20)
            btn.bind(on_press=self.check_answer)
            self.add_widget(btn)

    def check_answer(self, instance):
        correct = questions[self.index]["answer"]
        if instance.text == correct:
            self.score += 1
        self.index += 1
        if self.index < len(questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.clear_widgets()
        self.add_widget(Label(text=f"✅ স্কোর: {self.score} / {len(questions)}", font_size=28))

class SquadApp(App):
    def build(self):
        return MCQScreen()

if __name__ == "__main__":
    SquadApp().run()

