from rufus.client import RufusClient
from rufus.content_filter import ContentFilter

def main():
    openai_api_key = "your_openai_api_key"  # Replace this with your OpenAI API key
    instructions = "We're making a chatbot for graduate admission process for UTA"
    url = "https://www.uta.edu/admissions/apply/graduate"
    crawl_depth = 2

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


if __name__ == "__main__":
    main()
