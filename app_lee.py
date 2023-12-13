import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

class KeywordService:
    def __init__(self, user_type):
        self.user_type = user_type

    def show_menu(self):
        root = tk.Tk()
        style = ttk.Style()
        style.theme_use("clam")  # Tkinter의 clam 테마를 사용합니다.

        root.title("Keyword Service Menu")

        menu_label = ttk.Label(root, text="Select a Menu", font=('Helvetica', 16, 'bold'))
        menu_label.pack(pady=10)

        menu_options = ["1. Daily Popular Keywords", "2. View Interesting News", "3. View Keyword Trend", "4. View Top Keywords"]

        if self.user_type == "admin":
            menu_options = ["1. Manage Press", "2. Add/Modify/Delete Articles", "3. Manage Reporters", "4. Check Reporter Diligence"]

        menu_listbox = tk.Listbox(root, font=('Helvetica', 12))
        for option in menu_options:
            menu_listbox.insert(tk.END, option)

        menu_listbox.pack(pady=10)

        select_button = ttk.Button(root, text="Select", command=lambda: self.execute_menu(menu_listbox.get(tk.ACTIVE)))
        select_button.pack(pady=10)

        root.mainloop()

    def execute_menu(self, selected_menu):
        if selected_menu.startswith("1."):
            if self.user_type == "admin":
                self.manage_press()
            else:
                self.daily_popular_keywords()
        elif selected_menu.startswith("2."):
            if self.user_type == "admin":
                self.add_modify_delete_articles()
            else:
                self.view_interesting_news()
        elif selected_menu.startswith("3."):
            if self.user_type == "admin":
                self.manage_reporters()
            else:
                self.view_keyword_trend()
        elif selected_menu.startswith("4."):
            if self.user_type == "admin":
                self.check_reporter_diligence()
            else:
                self.view_top_keywords()

    # 나머지 메소드는 이전과 동일하게 유지합니다.

    def authenticate(self):
        # 사용자 인증 및 로그인
        root = tk.Tk()
        root.withdraw()  # Tkinter 창을 숨깁니다.

        user_id = simpledialog.askstring("Login", "Enter your ID:")
        password = simpledialog.askstring("Login", "Enter your password:", show='*')

        # 여기에 실제 로그인 처리를 구현하면 됩니다.
        # 예를 들어, 사용자 ID와 비밀번호를 확인하고, 관리자 여부를 판단하여 반환합니다.
        # 아래는 간단한 예시입니다. 실제 구현에 맞게 수정해주세요.
        if user_id == "admin" and password == "1234":
            return "admin"
        elif user_id == "user" and password == "1234":
            return "user"
        else:
            messagebox.showerror("Login Failed", "Invalid ID or password.")
            return None

# GUI 실행
root = tk.Tk()
app = KeywordService(None)
user_type = app.authenticate()

if user_type:
    app = KeywordService(user_type)
    app.show_menu()

root.mainloop()
