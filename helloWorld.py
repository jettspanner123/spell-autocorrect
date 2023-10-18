import customtkinter as CTK
import sys
from textblob import TextBlob

if __name__ == "__main__":
    CTK.set_appearance_mode("Dark")
    CTK.set_default_color_theme("dark-blue")

    main_windows = CTK.CTk();
    main_windows.geometry("700x700")
    main_windows.resizable(False, False)
    main_windows.title("Spell Corrector.")

    main_framer = CTK.CTkFrame(master=main_windows)
    main_framer.pack(pady=20, padx=20, fill="both", expand=True)

    Lable = CTK.CTkLabel(master=main_framer, text="spell autocorrect tool".upper(), font=("Dyuthi", 35, "bold", "underline"))
    Lable.pack(pady=40, padx=30)


    user_input_label = CTK.CTkLabel(main_framer, text="enter user input: ".upper(), font=('Dyuthi', 20, "bold"))
    user_input_label.place(relx=0.20, rely=0.25, anchor=CTK.CENTER)
    user_input = CTK.CTkEntry(main_framer, width=600, height=50, font=('Dyuthi', 15, "bold"))
    user_input.place(relx=0.5, rely=0.33, anchor=CTK.CENTER)


    stringVar = CTK.StringVar()

    def autocorrect_it():
        user_input_text = user_input.get()
        correct_text = TextBlob(user_input_text).correct()
        stringVar.set(correct_text)


    change_button = CTK.CTkButton(master=main_framer, text="Correct", font=('Dyuthi', 32, "bold"), width=600, height=65,
                                  text_color="white",
                                  command=autocorrect_it
                                  )
    change_button.place(relx=0.5, rely=0.45, anchor=CTK.CENTER)

    autocorrect_label = CTK.CTkLabel(main_framer, text="autocorrect word: ".upper(), font=('Dyuthi', 20, "bold"))
    autocorrect_label.place(relx=0.23, rely=0.55, anchor=CTK.CENTER)
    autocorrect_input = CTK.CTkEntry(main_framer, textvariable=stringVar, width=600, height=50, font=('Dyuthi', 15, "bold"))
    autocorrect_input.place(relx=0.5, rely=0.63, anchor=CTK.CENTER)

    clear_button = CTK.CTkButton(master=main_framer, text="Clear", font=('Dyuthi', 32, "bold"), width=600, height=65,
                                  )
    clear_button.place(relx=0.5, rely=0.75, anchor=CTK.CENTER)

    exit_button = CTK.CTkButton(master=main_framer, command=lambda: sys.exit(), text="<", font=("Dyuthi", 32, "bold"), width=600, height=65, fg_color="#b10c13")
    exit_button.place(relx=0.5, rely=0.89, anchor=CTK.CENTER)

    main_windows.mainloop()
