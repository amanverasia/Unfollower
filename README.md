# Unfollower
<pre>                                                                                                         
@@@  @@@  @@@  @@@  @@@@@@@@   @@@@@@   @@@       @@@        @@@@@@   @@@  @@@  @@@  @@@@@@@@  @@@@@@@   
@@@  @@@  @@@@ @@@  @@@@@@@@  @@@@@@@@  @@@       @@@       @@@@@@@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  
@@!  @@@  @@!@!@@@  @@!       @@!  @@@  @@!       @@!       @@!  @@@  @@!  @@!  @@!  @@!       @@!  @@@  
!@!  @!@  !@!!@!@!  !@!       !@!  @!@  !@!       !@!       !@!  @!@  !@!  !@!  !@!  !@!       !@!  @!@  
@!@  !@!  @!@ !!@!  @!!!:!    @!@  !@!  @!!       @!!       @!@  !@!  @!!  !!@  @!@  @!!!:!    @!@!!@!   
!@!  !!!  !@!  !!!  !!!!!:    !@!  !!!  !!!       !!!       !@!  !!!  !@!  !!!  !@!  !!!!!:    !!@!@!    
!!:  !!!  !!:  !!!  !!:       !!:  !!!  !!:       !!:       !!:  !!!  !!:  !!:  !!:  !!:       !!: :!!   
:!:  !:!  :!:  !:!  :!:       :!:  !:!   :!:       :!:      :!:  !:!  :!:  :!:  :!:  :!:       :!:  !:!  
::::: ::   ::   ::   ::       ::::: ::   :: ::::   :: ::::  ::::: ::   :::: :: :::    :: ::::  ::   :::  
 : :  :   ::    :    :         : :  :   : :: : :  : :: : :   : :  :     :: :  : :    : :: ::    :   : :  </pre>
                                                                                                         
This Python script allows you to track changes in Instagram followers over time for multiple accounts. It detects new followers and those who have unfollowed since the last check, organizing data for each tracked account in separate folders.

## Features

- Track followers for any public Instagram account
- Detect new followers and unfollowers
- Support for two-factor authentication (2FA)
- Option for one-time checks or scheduled automatic checks
- Organizes data for each tracked account in separate folders

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.6 or higher installed on your system
- pip (Python package installer)

## Installation

1. Clone this repository or download the `unfollower.py` file.

2. Install the required Python packages:

   ```
   pip install instagrapi
   ```

## Usage

1. Open a terminal or command prompt.

2. Navigate to the directory containing `unfollower.py`.

3. Run the script:

   ```
   python unfollower.py
   ```

4. Follow the prompts:
   - Enter your Instagram username
   - Enter your Instagram password (input will be hidden)
   - If you have 2FA enabled, you'll be prompted to enter the OTP sent to your device
   - Enter the Instagram username you want to track
   - Enter the interval in minutes for automatic checks (or press Enter for a one-time check)

5. The script will display the results, showing new followers and unfollowers since the last check.

## Automatic Checks

If you choose to run automatic checks:

- The script will continue running, performing checks at the specified interval.
- Press Ctrl+C to stop the script at any time.

## Data Storage

The script creates a new folder for each tracked Instagram account, named after the target username. Inside this folder, it stores the follower data in a file named `followers.json`. This organization allows you to track multiple accounts while keeping their data separate.

## Security Note

This script requires your Instagram login credentials. Always ensure you're running the script in a secure environment. Never share your credentials or the `followers.json` files with others.

## Compliance

Ensure that your use of this tool complies with Instagram's terms of service and API usage policies. Excessive use may result in temporary or permanent restrictions on your Instagram account.

## Troubleshooting

If you encounter login issues:

- Ensure your username and password are correct.
- If using 2FA, make sure you're entering the correct OTP.
- Instagram may temporarily block login attempts if you make too many in a short period. Wait a while before trying again.

## Contributing

Contributions to improve the script are welcome. Please feel free to submit a Pull Request.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).
