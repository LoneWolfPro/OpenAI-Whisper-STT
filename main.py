import mimetypes
import os
import subprocess
import torch
import whisper
import warnings


def is_video_file():
    """
    Get the file type
    Return Boolean value
    """
    mime_type, _ = mimetypes.guess_type(file_path)
    return mime_type and mime_type.startswith("video")


def video_to_audio():
    """
    Convert video file->audio file,
    if it is a video file, convert it,
    if it is an audio file, do not convert it
    """
    global audio_file_path

    if is_video_file():
        command = f"ffmpeg -y -i {file_path} -vn -acodec copy {cov_audio_file_path}"  # Use ffmpeg to convert video files to .m4a files
        subprocess.run(command, shell=True)
        print(f"Conversion successful: {cov_audio_file_path}")
        audio_file_path = cov_audio_file_path  # Set the audio file path to the converted .m4a file path
    else:
        print(f"{file_path} is not a video file and does not need to be converted.")
        audio_file_path = file_path  # Set the audio file path to the original file path


def transcribe_audio():
    """
    Call OpenAI-Whisper for STT (speech to text)
    """

    def check_gpu():
        """
        Check if there is an available CUDA GPU and output
        """
        if torch.cuda.is_available():
            print(f"GPU is available: {torch.cuda.get_device_name(0)}")
        else:
            print("GPU is not available, Audio recognition can be slow.")

    def check_device():
        """
        Return "cuda" if a CUDA GPU is available
        Return "cpu" otherwise
        """
        return "cuda" if torch.cuda.is_available() else "cpu"

    warnings.simplefilter("ignore", UserWarning)  # Ignore warning messages
    check_gpu()
    device = check_device()
    print(f"Using device: {device}")
    model = whisper.load_model("turbo").to(device)
    result = model.transcribe(audio_file_path)

    if result["text"] is None:
        raise ValueError("Transcription failed, no result returned.")
    segments = result["segments"]
    time_text_list = []  # List of raw output containing time and text
    result = []  # Formatted list
    for segment in segments:
        start_time = segment["start"]
        formatted_time = f"{int(start_time // 3600):02}:{int((start_time % 3600) // 60):02}:{int(start_time % 60):02}"
        text = segment["text"]
        time_text_list.append((formatted_time, text))
    for time, text in time_text_list:
        result.append(f"[{time}] {text}")
    output = "\n".join(result)
    print(output)


def remove_cov_file():
    if(is_video_file()):
        try:
            os.remove(cov_audio_file_path)
            print(f"File {cov_audio_file_path} deleted successfully")
        except FileNotFoundError:
            print(f"File {cov_audio_file_path} not found")
        except PermissionError:
            print(f"Permission denied: unable to delete {cov_audio_file_path}")
        except Exception as e:
            print(f"Error: {e}")



def main():
    video_to_audio()
    transcribe_audio()
    remove_cov_file()


file_path = r"test_video.mp4" # File to be identified
audio_file_path = r""
cov_audio_file_path = r"cov_audio.m4a"
main()