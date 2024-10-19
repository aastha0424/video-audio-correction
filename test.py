import openai

def test_openai_api():
    # Set up the Azure OpenAI API key and endpoint
    openai.api_key = "22ec84421ec24230a3638d1b51e3a7dc"  # Update the API key here
    openai.api_base = "https://internshala.openai.azure.com"  # Base URL for Azure
    openai.api_type = "azure"
    openai.api_version = "2024-08-01-preview"  # Use the correct API version

    try:
        # Create a simple request to the Azure OpenAI ChatCompletion endpoint
        response = openai.ChatCompletion.create(
            deployment_id="gpt-4o",  # Use the deployment ID for Azure
            messages=[
                {"role": "user", "content": "Hello, how are you today?"}  # Simple test prompt
            ],
            max_tokens=50
        )

        # Print the response from the API
        print("Response from OpenAI:")
        print(response.choices[0].message['content'].strip())

    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    test_openai_api()
