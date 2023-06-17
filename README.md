# Haqbaat Bot ⚖️♀

Haqbaat is a WhatsApp bot designed to empower and uplift Pakistani women by providing them an easy interface to access information regarding their rights in Pakistan. The bot is built to interact with users in Roman Urdu, making it convenient for women to communicate and obtain information easily.

## Purpose and Features ✨

The purpose of the Haqbaat WhatsApp Bot is to provide an accessible platform for Pakistani women to engage with the bot and gain knowledge about women's rights. The bot aims to empower women by delivering information, resources, and support through the convenience of WhatsApp.

Features of the Haqbaat WhatsApp Bot include:

- Answering questions about women's rights
- Providing educational resources and materials
- Offering guidance and support

## Prerequisites 🔑

To run and deploy the Haqbaat WhatsApp Bot, you will need the following:

1. Twilio Account: Create a Twilio account and obtain your Account SID and Auth Token.

2. WhatsApp Sandbox: Set up a WhatsApp Sandbox in your Twilio account to receive and send messages.

3. Python: Install Python on your local machine. The recommended version is Python 3.x.

4. Ngrok: Download and install Ngrok from the official website (https://ngrok.com/) based on your operating system.

5. OpenAI API: Sign up for the OpenAI API and obtain your Secret API key from user settings (you may require a paid account for this).

## Installation and Usage 🚀💻

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/haqbaat-bot.git
   ```

2. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

3. Create a `.env` file in the root directory of the project.

4. Add the following lines to the `.env` file:

   ```plaintext
   TWILIO_ACCOUNT_SID=your_account_sid
   TWILIO_AUTH_TOKEN=your_auth_token
   OPENAI_API_KEY=your_openai_api_key
   TWILIO_NUMBER= your_twilio_number
   RECEIPENT_NUMBER= your_number
   ```

   Replace `your_account_sid`, `your_auth_token`, `your_openai_api_key`, `your_twilio_number`, and `your_number` with your actual credentials.


5. Run the local server:

   ```bash
   python3 main.py
   ```

6. Start Ngrok to create a public URL for your local server:

   ```bash
   ngrok http 5000
   ```

7. Update the WhatsApp sandbox with the Ngrok URL. Set the incoming message webhook to `<your_ngrok_url>/message` , leave the callback url box empty.

9. Your Haqbaat WhatsApp Bot is now ready to use! Send a message to the WhatsApp sandbox number to interact with the bot and receive information about women's rights.

## Contributing 🤝🌟

Contributions to the Haqbaat WhatsApp Bot project are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.


🙋‍♀️🌟 Let's empower Pakistani women together!
