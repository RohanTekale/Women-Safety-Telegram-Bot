# Women Safety Telegram Bot

The **Women Safety Bot** is a powerful Telegram bot aimed at enhancing women's safety. It provides features like emergency alerts, location sharing, and voice-activated commands, allowing users to alert their pre-configured emergency contacts in critical situations.

This bot leverages the Telegram API, Twilio for SMS alerts, Nominatim for real-time geolocation and reverse geocoding, and Python for backend development.

## Features

- **Emergency Alert System**: Sends SMS alerts to pre-configured emergency contacts with the user’s live location.
- **Location Sharing**: Automatically requests and shares the user’s live location.
- **Voice-Activated Commands**: Optional feature to enable voice-activated alerts in dangerous situations.
- **Geolocation and Reverse Geocoding**: Converts coordinates to a readable address using the Nominatim API (OpenStreetMap).
- **User-Friendly Interface**: Simple command-based interaction for easy use in emergencies.
- **Highly Customizable**: Adaptable to additional features, contacts, and services as needed.

## Technologies Used

- **Language**: Python
- **Telegram Bot API**: For bot functionality and messaging
- **Twilio API**: For sending SMS notifications
- **Nominatim (Geopy)**: For geolocation and reverse geocoding
- **AsyncIO**: For handling asynchronous operations and requests
- **Logging**: For monitoring bot activity and errors
- **Voice Commands (Optional)**: Using Python libraries for speech recognition (future implementation)

## Customization

- **Additional Contacts**: You can modify the bot to notify multiple contacts by adding more phone numbers in the Twilio configuration.
- **Voice Commands**: For hands-free operation, enable the voice-activated emergency alert feature by integrating the `speechrecognition` library.

## Troubleshooting

### Common Issues
- **Twilio SMS Not Sending**: Check your Twilio credentials, ensure your Twilio number is valid, and verify that the recipient’s number is formatted correctly.
- **Location Not Shared**: Make sure your device has location services enabled and that Telegram has permission to access it.
- **Bot Not Responding**: Verify that the bot token is correct and the bot is running without errors.

## Logs

All errors and activities are logged in the `/logs/bot.log` file. Check this file for troubleshooting bot-related issues.

## Future Enhancements

- **Voice Command Integration**: Enable users to trigger alerts using voice commands for hands-free operation.
- **Multiple Contacts Notification**: Alert multiple emergency contacts simultaneously.
- **Email Integration**: Send email notifications along with SMS.
- **User Registration**: Allow users to register their own contacts through the bot.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

## Contributions

Contributions, issues, and feature requests are welcome! Feel free to check the issues page or submit a pull request.


