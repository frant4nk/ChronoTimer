from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.clock import Clock
from kivy.core.audio import SoundLoader

Config.set('kivy', 'keyboard_mode', 'systemandmulti')
Config.set("kivy", "keyboard_layout", 'qwerty')

# Boxlayout is the App class

class BoxLayoutDemo(App):

    def build(self):

        superBox = BoxLayout(orientation='vertical')
        horizontalBox = BoxLayout(orientation='horizontal', size_hint=(1, .10))
        self.timerInput = TextInput(text='15', halign='center', input_type='number')
        self.timerInput.font_size = 50
        self.timerInput.valign = 'center'
        # timerInput.bind(on_text_validate=on_enter)
        accept = Button(text='Ok', size_hint=(.25, 1))
        accept.bind(on_press=self.ok_callback)

        start = Button(text='Start', size_hint=(.25, 1))
        start.bind(on_press=self.start_callback)
        
        stop = Button(text='Stop', size_hint=(.25, 1))
        stop.bind(on_press=self.stop_callback)

        horizontalBox.add_widget(self.timerInput)
        horizontalBox.add_widget(accept)
        horizontalBox.add_widget(start)
        horizontalBox.add_widget(stop)

        verticalBox = BoxLayout(orientation='vertical')
        self.timerButton = Button(text=self.timerInput.text, font_size=70)
        self.timerButton.bind(on_press=self.resetTimer)
        

        verticalBox.add_widget(self.timerButton)

        superBox.add_widget(horizontalBox)
        superBox.add_widget(verticalBox)

        self.clockTimer = Clock#.schedule_interval(self.timer_callback, 1)
        self.clockTimer.schedule_interval(self.timer_callback, 1)

        self.sound = SoundLoader.load('beep.wav')

        return superBox


    def ok_callback(self, instance):
        self.timerButton.text = self.timerInput.text
   

    def start_callback(self, instance):
        self.clockTimer.schedule_interval(self.timer_callback, 1)


    def stop_callback(self, instance):
        self.clockTimer.unschedule(self.timer_callback)
        self.timerButton.text = self.timerInput.text


    def timer_callback(self, instance):
        if int(self.timerButton.text) > 0:
            self.timerButton.text = str(int(self.timerButton.text) - 1)
        if int(self.timerButton.text) == 0:
            self.sound.play()


    def resetTimer(self, instance):
        # reset sound
        self.timerButton.text = self.timerInput.text

# Instantiate and run the kivy app

if __name__ == '__main__':

    BoxLayoutDemo().run()