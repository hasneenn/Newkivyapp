import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.popup import Popup
import requests



class RecoveryApp(App):
    def build(self):
        self.title = 'Account recovery'
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        layoutt = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # إعداد اسمك في الأعلى
        name_label = Label(
            text="PY » hasneen Al Ali\n\nTelegram : @PY_50\n\n\n\n\nProgram Send Rest", 
            font_size=60, 
            color=(0, 1, 0, 1),  # اللون الأخضر
            bold=True,
            size_hint_y=None, 
            height=2400
        )
        layout.add_widget(name_label)
        # حاوية لرفع الإدخال وزر الإرسال إلى الوسط
        center_layout = BoxLayout(orientation='vertical', size_hint_y=None, height='200dp', padding=[50, 1100, 50, 1100])
        
        # حاوية لحقل الإدخال وزر الإرسال
        input_layout = BoxLayout(orientation='horizontal', size_hint_y=None, height='40dp', spacing=10)
        
        # حقل إدخال البريد الإلكتروني أو اسم المستخدم
        self.email_input = TextInput(hint_text='Enter Your Email or username', background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1), size_hint_x=0.8)
        input_layout.add_widget(self.email_input)
        
        # زر الإرسال
        send_button = Button(text='Send', on_press=self.send_recovery_email, background_color=(0.5, 0.5, 0.5, 1), size_hint_x=0.2)
        input_layout.add_widget(send_button)
        
        # إضافة حاوية الإدخال وزر الإرسال إلى حاوية الوسط
        center_layout.add_widget(input_layout)
        
        # إضافة حاوية الوسط إلى التخطيط الرئيسي
        layout.add_widget(center_layout)
        
        # إعداد الخلفية السوداء
        layout.canvas.before.clear()
        with layout.canvas.before:
            from kivy.graphics import Color, Rectangle
            Color(0, 0, 0, 1)
            self.rect = Rectangle(size=(800, 600), pos=layout.pos)

        layout.bind(size=self._update_rect, pos=self._update_rect)
        return layout

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

    def send_recovery_email(self, instance):
        email = self.email_input.text
        url = 'https://i.instagram.com/api/v1/accounts/send_recovery_flow_email/'
        headers = {
            'X-Pigeon-Session-Id': '2b712457-ffad-4dba-9241-29ea2f472ac5',
            'X-Pigeon-Rawclienttime': '1707104597.347',
            'X-IG-Connection-Speed': '-1kbps',
            'X-IG-Bandwidth-Speed-KBPS': '-1.000',
            'X-IG-Bandwidth-TotalBytes-B': '0',
            'X-IG-Bandwidth-TotalTime-MS': '0',
            'X-IG-VP9-Capable': 'false',
            'X-Bloks-Version-Id': '009f03b18280bb343b0862d663f31ac80c5fb30dfae9e273e43c63f13a9f31c0',
            'X-IG-Connection-Type': 'WIFI',
            'X-IG-Capabilities': '3brTvw==',
            'X-IG-App-ID': '567067343352427',
            'User-Agent': 'Instagram 100.0.0.17.129 Android (30/11; 320dpi; 720x1448; realme; RMX3231; RMX3231; RMX3231; ar_IQ; 161478664)',
            'Accept-Language': 'ar-IQ, en-US',
            'Cookie': 'mid=Zbu4xQABAAE0k2Ok6rVxXpTD8PFQ; csrftoken=dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK',
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
            'Accept-Encoding': 'gzip, deflate',
            'Host': 'i.instagram.com',
            'X-FB-HTTP-Engine': 'Liger',
            'Connection': 'keep-alive',
            'Content-Length': '364',
        }
        data = {
            'signed_body': 'ef02f559b04e8d7cbe15fb8cf18e2b48fb686dafd056b7c9298c08f3e2007d43.{"_csrftoken":"dG4dEIkWvAWpIj1B2M2mutWtdO1LiPCK","adid":"5e7df201-a1ff-45ec-8107-31b10944e25c","guid":"b0382b46-1663-43a7-ba90-3949c43fd808","device_id":"android-71a5d65f74b8fcbc","query":"%s"}' % email,
            'ig_sig_key_version': '4'
        }
        response = requests.post(url, headers=headers, data=data).json()

        try:
            rr = response['email']
            popup = Popup(title='Good Has been sent Email ', content=Label(text=rr), size_hint=(None, None), size=(1000, 300))
            popup.open()
        except:
            popup = Popup(title='Error username or Bind', content=Label(text=f"An error occurred\n"), size_hint=(None, None), size=(400, 400))
            popup.open()

if __name__ == '__main__':
    RecoveryApp().run()