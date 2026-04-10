import anthropic

import os

# ----------------------------------------

# CONFIGURATION — paste your API key here

# ----------------------------------------

API_KEY = API_KEY = os.environ.get("ANTHROPIC_API_KEY")
# ----------------------------------------

# SYSTEM PROMPT — this is what tells Claude

# how to behave. We will iterate on this.

# ----------------------------------------

SYSTEM_PROMPT = """You are a friendly assistant for a small dorm interior decorating business. 

When a potential customer sends an inquiry, you write a warm, personalized email response on behalf of the business owner.

Your response should:

- Greet the customer by name if they provided one

- Acknowledge their style preferences and budget if mentioned

- Briefly explain how the service works (consultation, mood board, shopping list)

- Invite them to book a free 15-minute consultation call

- Sign off as "Dorm Decor Co."

Keep the tone warm, enthusiastic, and professional. Keep the email under 200 words."""

# ----------------------------------------

# FUNCTION — sends inquiry to Claude and

# returns the drafted response

# ----------------------------------------

def generate_response(customer_inquiry):

    client = anthropic.Anthropic(api_key=API_KEY)

    message = client.messages.create(

        model="claude-opus-4-5",

        max_tokens=1024,

        messages=[

            {

                "role": "user",

                "content": f"Please write a response to this customer inquiry:\n\n{customer_inquiry}"

            }

        ],

        system=SYSTEM_PROMPT

    )

    return message.content[0].text

# ----------------------------------------

# MAIN — runs the app from the command line

# ----------------------------------------

def main():

    print("=== Dorm Decor Inquiry Responder ===\n")

    print("Paste the customer inquiry below.")

    print("When done, press Enter twice.\n")

    lines = []

    while True:

        line = input()

        if line == "":

            break

        lines.append(line)

    customer_inquiry = "\n".join(lines)

    if not customer_inquiry.strip():

        print("No inquiry entered. Exiting.")

        return

    print("\nGenerating response...\n")

    response = generate_response(customer_inquiry)

    print("=== DRAFT RESPONSE ===\n")

    print(response)

    # Save output to a file

    with open("output.txt", "w") as f:

        f.write("CUSTOMER INQUIRY:\n")

        f.write(customer_inquiry)

        f.write("\n\nDRAFT RESPONSE:\n")

        f.write(response)

    print("\n=== Response saved to output.txt ===")

if __name__ == "__main__":

    main()
