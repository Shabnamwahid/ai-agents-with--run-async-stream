import os
import asyncio
from dotenv import load_dotenv
import google.generativeai as genai

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Create a Gemini flash agent
agent = genai.GenerativeModel("gemini-1.5-flash")

# User prompt
prompt = input("Enter your prompt: ")

# ---------
# Agent Level
# ---------

async def agent_run():
    print("\n[Agent Level] run()")
    response = await agent.generate_content_async(prompt)
    print(response.text)

def agent_run_sync():
    print("\n[Agent Level] run_sync()")
    response = agent.generate_content(prompt)
    print(response.text)

async def agent_stream():
    print("\n[Agent Level] stream()")
    stream = await agent.generate_content_async(prompt, stream=True)
    async for chunk in stream:
        print(chunk.text, end="")
    print()

# -------------
# Run Level
# -------------

async def run_level_run():
    print("\n[Run Level] run()")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = await model.generate_content_async(prompt)
    print(response.text)

def run_level_run_sync():
    print("\n[Run Level] run_sync()")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    print(response.text)

async def run_level_stream():
    print("\n[Run Level] stream()")
    model = genai.GenerativeModel("gemini-1.5-flash")
    stream = await model.generate_content_async(prompt, stream=True)
    async for chunk in stream:
        print(chunk.text, end="")
    print()

# ------------
# Global Level
# ------------

def global_run_sync():
    print("\n[Global Level] run_sync()")
    response = genai.GenerativeModel("gemini-1.5-flash").generate_content(prompt)
    print(response.text)

async def global_stream():
    print("\n[Global Level] stream()")
    model = genai.GenerativeModel("gemini-1.5-flash")
    stream = await model.generate_content_async(prompt, stream=True)
    async for chunk in stream:
        print(chunk.text, end="")
    print()

# ----------
# Choose model
# ----------

async def main():
    options = {
        "1": agent_run,
        "2": lambda: agent_run_sync(),
        "3": agent_stream,
        "4": run_level_run,
        "5": lambda: run_level_run_sync(),
        "6": run_level_stream,
        "8": lambda: global_run_sync(),
        "9": global_stream,
    }

    while True:
        print("\nSelect Option to Run:")
        print("1. Agent Level - run")
        print("2. Agent Level - run_sync")
        print("3. Agent Level - stream")
        print("4. Run Level - run")
        print("5. Run Level - run_sync")
        print("6. Run Level - stream")
        print("7. Global Level - run")
        print("8. Global Level - run_sync")
        print("9. Global Level - stream")
        print("0. Exit")

        choice = input("Enter (0-9): ")

        if choice == "0":
            print("Exiting.")
            break
        elif choice in options:
            func = options[choice]
            if asyncio.iscoroutinefunction(func):
                await func()
            else:
                func()
        else:
            print("! Invalid Choice.")

# Run the main function
if __name__ == "__main__":
    asyncio.run(main())



    


# terminal pr uv run main.py ya python main.py bhi chala sakty hain