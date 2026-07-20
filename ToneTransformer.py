import os
from google import genai
from google.genai import types
from dotenv import load_dotenv  # <-- Fixed the import here

# Automatically load the .env file from the project root
load_dotenv() 

def generate_marketing_copy(
    product_name: str,
    platform: str,
    tone: str,
    raw_description: str,
    temperature: float,
    top_p: float
) -> str:
    """
    Transforms a raw product description into tailored marketing copy
    using dynamic prompt injection and custom model inference parameters.
    """
    # The client will now successfully find the key loaded by load_dotenv()
    client = genai.Client()

    # Inject variables into a dynamic string template
    prompt = f"""
    You are an expert copywriter. Take the following raw product details 
    and transform them into highly engaging marketing copy optimized for the target platform.

    ---
    Product Name: {product_name}
    Target Platform: {platform}
    Desired Tone: {tone}
    Raw Description: {raw_description}
    ---

    Requirements:
    - Adhere strictly to the style norms, length limits, and features (like hashtags, emojis, or subject lines) typical of {platform}.
    - Ensure the text perfectly reflects a {tone} voice.
    """

    # Handle system parameters like Temperature and Top_P to control model creativity
    config = types.GenerateContentConfig(
        temperature=temperature,
        top_p=top_p,
    )

    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=config
        )
        return response.text
    except Exception as e:
        return f"An error occurred during generation: {e}"


def main():
    print("====================================================")
    print("   AUTOMATED COPYWRITING & TONE TRANSFORMER APP")
    print("====================================================\n")

    # Double-check that load_dotenv() actually found the key
    if not os.environ.get("GEMINI_API_KEY"):
        print("Error: GEMINI_API_KEY could not be found in your .env file.")
        print("Please ensure your .env file is in the root 'Decodelabs' folder and contains:")
        print("GEMINI_API_KEY=your_actual_key_here")
        return

    # Gather User Inputs dynamically
    product_name = input("Enter Product Name: ").strip()
    platform = input("Enter Platform (e.g., LinkedIn, Instagram, Email): ").strip()
    tone = input("Enter Desired Tone (e.g., Professional, Witty, Energetic): ").strip()
    raw_description = input("Enter Raw Product Description: ").strip()

    # Handle system creativity parameters with safe fallbacks
    try:
        temp_input = input("Enter Temperature (0.0 to 1.0, default 0.7): ").strip()
        temperature = float(temp_input) if temp_input else 0.7
        
        top_p_input = input("Enter Top_P (0.0 to 1.0, default 0.95): ").strip()
        top_p = float(top_p_input) if top_p_input else 0.95
    except ValueError:
        print("\nInvalid number entered for Temperature or Top_P. Using defaults (0.7, 0.95).")
        temperature = 0.7
        top_p = 0.95

    print("\n[Processing...] Generating your tailored marketing copy...\n")

    # Run the generation engine
    output_copy = generate_marketing_copy(
        product_name=product_name,
        platform=platform,
        tone=tone,
        raw_description=raw_description,
        temperature=temperature,
        top_p=top_p
    )

    print("==================== GENERATED COPY ====================")
    print(output_copy)
    print("========================================================")


if __name__ == "__main__":
    main()