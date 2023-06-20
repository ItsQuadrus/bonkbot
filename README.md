# BonkBot

This is a Discord bot built using discord.py with slash commands. It can query Bonk.io API. It still is in WIP and only contains the `!status` command at the moment.

## Features

- Retrieves player data based on the type specified.
- Supports the following player types: classic, arrows, grapple, custom, simple, and total.
- Responds to the `!status` slash command.

## Requirements

- Python 3.7 or higher

## Installation
### One-liner with line breaks
*Bash*
```bash
git clone https://github.com/ItsQuadrus/BonkBot.git
cd BonkBot
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
echo "DISCORD_TOKEN=your-token-here" > .env #
py src
```
*Windows (cmd)*
```bat
git clone https://github.com/ItsQuadrus/BonkBot.git
cd BonkBot
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
echo DISCORD_TOKEN=your-token-here > .env
py src
```

### Manual installation

1. Clone the repository:

```bash
git clone https://github.com/ItsQuadrus/BonkBot.git
```

2. Create a virtual environment:
   - Navigate to the project's directory.
   - Run the following command to create a new virtual environment:
     ```bash
     python -m venv venv
     ```

2. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate.bat
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. Install project dependencies:
   - Run the following command to install the required packages:
     ```bash
     pip install -r requirements.txt
     ```

4. Create a file named `.env` in the root directory of the project and add the following:

```env
DISCORD_TOKEN=your-token-here
```

5. Run the bot:

```bash
py src
```

6. Invite the bot to your server and type `!status`.

## License
This project is licensed under the [Creative Commons Attribution 3.0 Unported License](https://creativecommons.org/licenses/by/3.0/).

You are free to use this code for any purpose, commercial or non-commercial. **Attribution is required: you must give credit to the original author.**

You also need to **indicate if changes were made.** e.g. "Translation of BonkBot by ItsQuadrus"