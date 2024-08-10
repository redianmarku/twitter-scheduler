import tkinter as tk
from tkinter import messagebox, simpledialog
from x_pyAPI import X_API
import threading
import time


class TwitterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Twitter Schedular")

        self.Xapi = None

        tk.Label(root, text="Consumer Key: ").grid(row=0, column=0, padx=10, pady=10)
        self.consumer_key_entry = tk.Entry(root)
        self.consumer_key_entry.grid(row=0, column=1, padx=10, pady=10)

        tk.Label(root, text="Consumer Secret: ").grid(row=1, column=0, padx=10, pady=10)
        self.consumer_key_entry_secret = tk.Entry(root)
        self.consumer_key_entry_secret.grid(row=1, column=1, padx=10, pady=10)

        self.auth_button = tk.Button(root, text="Authenticate", command=self.authenticate)
        self.auth_button.grid(row=2, columnspan=2, padx=10)

        #This is going to show user info
        self.user_info_label = tk.Label(root, text="",  justify="left")
        self.user_info_label.grid(row=3, columnspan=2, padx=10, pady=10)

        #Tweeet imput box
        tk.Label(root, text="Tweets: ").grid(row=4, column=0, padx=10, pady=10)
        self.tweet_box = tk.Text(root, height=5, width=50)
        self.tweet_box.grid(row=4, column=1, padx=10, pady=10)

        tk.Label(root, text="Schedule Interval in seconds: ").grid(row=5, column=0, padx=10, pady=10)
        self.schedule_entry = tk.Entry(root)
        self.schedule_entry.grid(row=5, column=1, padx=10, pady=10)

        self.start_button = tk.Button(root, text="Start the program", command=self.start)
        self.start_button.grid(row=6, columnspan=2, padx=10)

        
    def authenticate(self):
        consumer_key = self.consumer_key_entry.get()
        constumer_secret = self.consumer_key_entry_secret.get()

        if not consumer_key or not constumer_secret:
            messagebox.showerror("Error", "Please put the api keys")
            return
        
        self.Xapi = X_API(consumer_key, constumer_secret)
        self.Xapi.authorize()

        user_info = self.Xapi.get_user_info()

        if user_info:
            self.user_info_label.config(
                text=f"Name: {user_info['name']}\n Username: {user_info['username']} \n Description: {user_info['description']}"
            )
        else:
            messagebox.showerror("Error", "Failed to authenticate")


        
    def start(self):
        interval = self.schedule_entry.get()

        if not interval.isdigit():
            messagebox.showerror("Error", "Please put number of interval in seconds")
            return
        
        seconds = int(interval)
        if seconds <= 0:
            messagebox.showerror("Error", "Please put number greater then 0 for seconds")
            return
        
        tweets = self.tweet_box.get("1.0", tk.END).strip().split('\n')
        if not  tweets:
            messagebox.showerror("Error", "There is not tweets to schedule")
            return
        
        self.schedule_thread = threading.Thread(target=self.schedule, args=(tweets, seconds))
        self.schedule_thread.start()

    
    def schedule(self, tweets, seconds):
        while tweets:
            tweet = tweets.pop(0)
            response = self.Xapi.post_tweet(tweet)
            if response:
                print(f"Tweet posted: {tweet}")
            else:
                print(f"Failed to post tweet: {tweet}")

            time.sleep(seconds)

        print("Finished posting all tweets.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TwitterApp(root)
    root.mainloop()
