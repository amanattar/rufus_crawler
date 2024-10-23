# scripts/run_rufus.py
from rufus.client import RufusClient
from rufus.content_filter import ContentFilter

def main():
    # Provide your OpenAI API key, URL, instructions, and depth here
    openai_api_key = "your_openai_api_key"  # Replace with your OpenAI API key
    url = "https://www.uta.edu/admissions/apply/graduate"
    instructions = "We're making a chatbot for graduate admission process for UTA"
    crawl_depth = 2  # You can change the depth as needed
    
    # Initialize the RufusClient to crawl and save content
    client = RufusClient(openai_api_key)
    client.crawl(url, depth=crawl_depth)

    # Convert the crawled text files into JSON
    crawled_data = client.convert_txt_to_json()

    # Initialize the content filter
    content_filter = ContentFilter(openai_api_key)

    # Filter the content based on the instruction
    filtered_data = content_filter.filter_content(instructions, crawled_data)
    
    # Save the filtered content to a new JSON file
    content_filter.save_filtered_data(filtered_data)

    # Cleanup intermediate files to only keep the final filtered JSON file
    client.cleanup_files()

if __name__ == "__main__":
    main()
