# OpenAI-Whisper-STT
Video to Audio Transcription using OpenAI-Whisper
=================================================

Description:
-------------
This Python script processes a given media file by first checking whether it is a video file. If it is, the script converts the video into an audio file using FFmpeg. Then, it leverages the OpenAI-Whisper model to transcribe the audio. The transcription is output with timestamped segments, and any temporary files generated during processing are deleted afterward.

Features:
----------
• **Media File Detection:** Determines whether the given file is a video by inspecting its MIME type.
• **Video-to-Audio Conversion:** Uses FFmpeg to convert video files (e.g., .mp4) to an audio format (.m4a) while preserving the original audio codec.
• **Speech-to-Text Transcription:** Utilizes the OpenAI-Whisper model (using the “turbo” variant by default) to convert spoken words into text. It also checks for CUDA-enabled GPUs (if available) to accelerate performance.
• **Timestamped Output:** Formats and prints the transcription with corresponding timestamps in the format HH:MM:SS.
• **Cleanup:** Deletes the temporary audio file after transcription if a conversion was performed.

Prerequisites:
---------------
Before running the script, ensure that the following software and libraries are installed:

1. **Python 3.7 or later**
   - The script is written in Python and requires version 3.7 or above.

2. **FFmpeg**
   - FFmpeg is needed for converting video files to audio.
   - Installation examples:
     - **Ubuntu/Debian:** `sudo apt-get install ffmpeg`
     - **macOS (Homebrew):** `brew install ffmpeg`
     - **Windows:** Download the executable from [ffmpeg.org](https://ffmpeg.org/) and ensure it is added to your system PATH.

3. **PyTorch**
   - Required by the Whisper model for model inference.
   - Install using pip (ensure you pick the version appropriate for your system):
     ```
     pip install torch
     ```

4. **OpenAI-Whisper**
   - Used for speech-to-text transcription.
   - Install via pip:
     ```
     pip install openai-whisper
     ```

5. **Python Standard Libraries**
   - Modules such as `mimetypes`, `os`, `subprocess`, and `warnings` are part of the Python standard library.

Usage:
-------
1. **Configure File Paths:**
   - Modify the `file_path` variable (set to `"test_video.mp4"` by default) to point to your video or audio file.
   - The `cov_audio_file_path` variable is used to store the temporary audio file (default: `"cov_audio.m4a"`).

2. **Run the Script:**
   - Execute the script in your terminal or command prompt:
     ```
     python <script_name>.py
     ```
     Replace `<script_name>.py` with the actual file name of the script.

3. **Output:**
   - If the file is detected as a video, it will be converted to an audio file.
   - The Whisper model then transcribes the audio, and you will see segmented transcription output with timestamps printed in your console.
   - Any temporary files created during conversion will be deleted after transcription.

Troubleshooting:
----------------
• **FFmpeg Not Found:** Ensure FFmpeg is installed and that its executable is accessible via your system PATH.
• **GPU Availability:** If you do not have a CUDA-enabled GPU, the script will default to CPU mode, which may be slower.
• **Permission Issues:** Verify that you have the appropriate read/write permissions for the files and directories involved, especially when deleting temporary files.
• **Transcription Errors:** Make sure the audio quality is sufficient for accurate transcription. Check that the correct file is being processed.

Customization:
---------------
• **Changing the Whisper Model:**
  - Currently, the script loads the “turbo” version of the model. You can replace `"turbo"` with another variant supported by OpenAI-Whisper if desired.
  
• **Output Format:**
  - The transcription segments are formatted as `[HH:MM:SS] text`. Feel free to modify the time or text formatting to better suit your needs.

License:
---------
This script is provided for educational and demonstration purposes. You are free to modify and use it according to your needs.

Support:
---------
For further assistance, consult the documentation for:
- [FFmpeg](https://ffmpeg.org/documentation.html)
- [PyTorch](https://pytorch.org/docs/stable/index.html)
- [OpenAI-Whisper](https://github.com/openai/whisper)
  
Feedback, questions, or suggestions are welcome!
