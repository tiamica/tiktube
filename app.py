import os
import requests
from gtts import gTTS
from moviepy.editor import ImageClip, concatenate_videoclips, AudioFileClip
from pytrends.request import TrendReq
from TikTokApi import TikTokApi
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload
from google.oauth2 import service_account
from PIL import Image, ImageDraw, ImageFont
import textwrap

# Fetch trending topics using Google Trends
def get_trending_topics():
    pytrends = TrendReq(hl='en-US', tz=360)
    trending = pytrends.trending_searches(pn='united_states')
    return trending.head(5)[0].tolist()

# Generate text-to-speech audio
def generate_audio(text, filename="audio.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)

# Create a background image with text
def create_background_image(text, filename="background.jpg"):
    # Create a blank image with a random color
    from random import randint
    bg_color = (randint(0, 255), (randint(0, 255)), (randint(0, 255)))
    image = Image.new("RGB", (1080, 1920), bg_color)
    draw = ImageDraw.Draw(image)

    # Load a font
    try:
        font = ImageFont.truetype("arial.ttf", 60)
    except IOError:
        font = ImageFont.load_default()

    # Wrap text and draw it on the image
    wrapped_text = textwrap.fill(text, width=30)
    text_width, text_height = draw.textsize(wrapped_text, font=font)
    draw.text(((1080 - text_width) / 2, (1920 - text_height) / 2), wrapped_text, font=font, fill="white")

    # Save the image
    image.save(filename)

# Create a video using an image and audio
def create_video(image_path, audio_path, output_path="output.mp4"):
    audio = AudioFileClip(audio_path)
    image_clip = ImageClip(image_path).set_duration(audio.duration)
    video = concatenate_videoclips([image_clip])
    video = video.set_audio(audio)
    video.write_videofile(output_path, fps=24)

# Upload video to TikTok
def upload_to_tiktok(video_path, caption):
    with TikTokApi() as api:
        api.upload_video(video_path, caption=caption)

# Upload video to YouTube
def upload_to_youtube(video_path, title, description):
    credentials = service_account.Credentials.from_service_account_file(
        'credentials.json', scopes=['https://www.googleapis.com/auth/youtube.upload']
    )
    youtube = build('youtube', 'v3', credentials=credentials)
    request = youtube.videos().insert(
        part="snippet,status",
        body={
            "snippet": {
                "title": title,
                "description": description,
                "tags": ["trending", "news"],
                "categoryId": "22"
            },
            "status": {
                "privacyStatus": "public"
            }
        },
        media_body=MediaFileUpload(video_path)
    )
    response = request.execute()
    print("Uploaded to YouTube:", response['id'])

# Main function
def main():
    # Step 1: Get trending topics
    topics = get_trending_topics()
    print("Trending Topics:", topics)

    # Step 2: Generate content
    topic = topics[0]  # Use the first trending topic
    generate_audio(f"Today's trending topic is {topic}")
    create_background_image(f"Trending: {topic}", "background.jpg")
    create_video("background.jpg", "audio.mp3", "output.mp4")

    # Step 3: Upload to TikTok
    upload_to_tiktok("output.mp4", f"Trending: {topic}")

    # Step 4: Upload to YouTube
    upload_to_youtube("output.mp4", f"Trending: {topic}", f"Today's trending topic is {topic}")

if __name__ == "__main__":
    main()