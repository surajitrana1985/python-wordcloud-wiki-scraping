import wikipedia
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plot

IMAGE_PATH = "./assets/svg/"

def main():
    # Getting user search keyword
    search_keyword = get_user_input_keyword()
    if search_keyword != "":
        # Getting web scraping content from wikipedia
        wiki_content = get_wiki_data(search_keyword)
        # Plotting Word Cloud
        plot_word_cloud(wiki_content, search_keyword)

"""
 This function plots a wordcloud using WordCloud
 class within wordcloud python package and visualization
 is shown with the help of matplotlib library
"""
def plot_word_cloud(content, search_keyword):
    stopwords = set(STOPWORDS)
    wordcloud_visual = WordCloud(background_color="black",
                                 mask=None,
                                 max_words=1000,
                                 stopwords=stopwords,
                                 min_font_size=10,
                                 max_font_size=100)
    wordcloud_visual.generate(content)
    plot.figure(figsize=(10, 10), dpi=100)
    plot.imshow(wordcloud_visual)
    plot.axis("off")
    plot.savefig(IMAGE_PATH + search_keyword.lower() + ".svg", format="svg")

"""
This function returns wiki page content: string
"""
def get_wiki_data(keyword):
    title = wikipedia.search(keyword)[0]
    page = wikipedia.page(title)
    return page.content

"""
This function will get the user input search keyword
"""
def get_user_input_keyword():
    return input("Please type a keyword to search in Wikipedia (Press Enter/Return to quit) : ")


if __name__ == "__main__":
    main()
