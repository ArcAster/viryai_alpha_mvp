from langchain_openai import ChatOpenAI
from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
load_dotenv()

import asyncio

task="""
   ### Prompt for Shopping Audit Agent – HEB Online Grocery Query

**Objective:**  
Visit [HEB online](https://www.heb.com/), search for the required grocery items, add them to the cart, select an appropriate delivery window, and complete the checkout process using TWINT.

**Important:**
- Make sure that you don't select more than it's needed for each article.
- After your search, if you click  the "Add to Cart" button, it adds the item to the basket.
---

### Step 1: Navigate to the Website
- Open [HEB Online](https://www.heb.com/).

---

### Step 2: search for specific keyword

**important**
- after entering a search term press "enter" to submit the search

#### Shopping List:

**collagen**
- observe all items in the top row 

create a json list of all items from the top row

**Important:** Ensure efficiency and accuracy throughout the process."""

browser = Browser()

agent = Agent(
   task=task,
    llm=ChatOpenAI(model="gpt-4o"),
    browser=browser,
    )

async def main():
    await agent.run()
    input("Press Enter to close the browser...")
    await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
