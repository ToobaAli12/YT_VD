import pytube
# Function to download video from URL
def download_video(url, resolution='720p', download_dir='C:\\Users\\HP 6470b\\Documents'):

    try:
        # Create YouTube object
        youtube = pytube.YouTube(url)
        
        # Get the highest resolution video stream
        stream = youtube.streams.get_by_resolution(resolution)
        
        # Download the video
        stream.download(output_path=download_dir )
        
        
        print('Video downloaded successfully!')
        
    except Exception as e:
        print(f'Error: {e}')

# Main program
if __name__ == '__main__':
    # Input video URL and resolution
    url = input('Enter the video URL: ')
    resolution = input('Enter the desired resolution (default is 720p): ')
    
    # Call the download_video function
    download_video(url, resolution)