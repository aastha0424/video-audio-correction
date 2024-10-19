import openai

def correct_transcription(transcription_text):
    openai.api_key = "22ec84421ec24230a3638d1b51e3a7dc"  # Update the API key here

    response = openai.Completion.create(
        engine="gpt-4o",  # Change this to the correct engine name if needed
        prompt=f"Correct the following transcription:\n{transcription_text}",
        max_tokens=1500
    )

    return response.choices[0].text.strip()
