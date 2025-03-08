# Auto Content Generator for TikTok and YouTube Reels

This Python app automatically generates and posts TikTok and YouTube Reels content based on trending topics from the internet. It dynamically creates background images for each video.

## Features
- Fetches trending topics using Google Trends.
- Generates a video with text-to-speech audio and a dynamic background image.
- Uploads the video to TikTok and YouTube.

## Prerequisites
1. Python 3.8 or higher.
2. Install the required libraries:
   ```bash
   pip install requests gtts moviepy pytrends TikTokApi google-api-python-client google-auth pillow
   ```

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/tiamica/tiktube.git

2. Create a virtual environment:
   ```bash
   python -m venv venv
   # On posix:source venv/bin/activate 
   # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration
1. Create a `.env` file in the root directory:
   ```
   TIKTOK_API_KEY=your_tiktok_api_key
   YOUTUBE_API_KEY=your_youtube_api_key
   ```

## Usage
1. Run the script:  
   ```bash
   python app.py
   ```

2. Follow the prompts to generate and post content.

## Contributing
1. Fork the repository.
2. Create a new branch for your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Create a pull request.   

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact  
For questions or feedback, please contact at [your_email@example.com](mailto:games@tiamica.com).
