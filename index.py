import base64

# Convert audio file to base64 string
def audio_to_base64_string(audio_file_path):
    with open(audio_file_path, "rb") as audio_file:
        audio_data = audio_file.read()
        base64_string = base64.b64encode(audio_data).decode("utf-8")
    return base64_string

# Convert base64 string back to audio file
def base64_string_to_audio(base64_string, output_audio_file_path):
    audio_data = base64.b64decode(base64_string)
    with open(output_audio_file_path, "wb") as audio_file:
        audio_file.write(audio_data)

# Example usage
audio_file_path = "boom.mp3"
base64_string = audio_to_base64_string(audio_file_path)
print("Base64 String:", base64_string)

output_audio_file_path = "new_boom.mp3"
base64_string_to_audio(base64_string, output_audio_file_path)
