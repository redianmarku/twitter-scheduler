# Twitter Scheduler Application

This Python application allows you to schedule and post tweets at specified intervals using the Twitter API. The program provides a simple GUI for entering API credentials, tweets, and scheduling intervals.

## Features

- User-friendly GUI for entering Twitter API credentials.
- Schedule multiple tweets to be posted at specified intervals.
- Display user information after successful authentication.

## Prerequisites

Before running this application, ensure you have the following installed:

- Python 3.x
- `tkinter` for the GUI
- `x_pyAPI` Python package for interacting with the Twitter API.

### Required Python Packages

You can install the required Python packages using `pip`:

```bash
pip install tk x_pyAPI
```

## Usage

1. **Download the Script**: Clone the repository or download the script directly.

   ```bash
   git clone https://github.com/yourusername/twitter-scheduler.git
   cd twitter-scheduler
   ```

2. **Run the Script**:

   - Open a terminal in the directory containing the script.
   - Run the script using Python:

   ```bash
   python twitter_scheduler.py
   ```

3. **Enter API Credentials**:

   - In the application window, enter your Twitter API `Consumer Key` and `Consumer Secret`.
   - Click the "Authenticate" button to authenticate with Twitter.

4. **Enter Tweets and Schedule**:
   - In the "Tweets" box, enter the tweets you want to schedule, each on a new line.
   - In the "Schedule Interval" box, specify the interval in seconds between each tweet.
   - Click the "Start the program" button to begin scheduling.

## Customization

### Interval

The interval between tweets can be adjusted by entering a different value in the "Schedule Interval in seconds" box. The interval must be a positive number.

### Tweets

You can add multiple tweets in the "Tweets" box, with each tweet on a new line. The program will post the tweets in the order they appear.

## Error Handling

- If the API credentials are incorrect or missing, the program will display an error message.
- The program checks for valid input in the schedule interval and tweets box, displaying error messages if any issues are found.

## Contributing

If you find a bug or want to contribute to the project, feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
