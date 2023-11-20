# Discord-Slash-Command-Template

Discord-Slash-Command-Template is a simple template for creating Discord bots with slash commands. It provides a quick starting point for developers looking to implement a bot with Discord's slash command functionality.

## Requirements
Before running the bot, make sure to install the required dependencies listed in the `requirements.txt` file. You can do this by running the following command:

```bash
pip install -r requirements.txt
```

Setup
Create a new Discord application and add a bot to it through the Discord Developer Portal.
Copy the Bot Token generated for your bot.
Create a new file named .env in the root directory of the project.
Inside the .env file, add the following line and replace "YOUR_BOT_TOKEN" with the Bot Token you copied:

```env
TOKEN="YOUR_BOT_TOKEN"
```

## Usage
To run the bot, execute the following command in your terminal:

```bash
python main.py
```
The bot will now be active on your Discord server, ready to respond to slash commands.

## Adding Commands
To add new slash commands, refer to the Discord API documentation for slash commands. Add your command logic in the commands directory.


## Contributing
Feel free to contribute to the project by opening issues or submitting pull requests. Your feedback and improvements are highly appreciated.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
