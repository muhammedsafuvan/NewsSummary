from typing import Optional
from newspaper import Article

from domain_model import NewsSummaryDomainModel, GetNewsRequest
from fastapi import FastAPI

def scrape_news_article(url: str) -> Optional[NewsSummaryDomainModel]:

    try:
        # Initialize Article object
        article = Article(url)

        # download article content
        article.download()

        # Parse downloaded article content
        article.parse()

        # apply nlp
        article.nlp()

        # Extract relevant data from the article
        data = {
            "authors": article.authors,
            "title": article.title,
            "published_date": article.publish_date,
            "summary": article.summary,
            "top_image": article.top_image,
        }

        # Create a NewsSummaryDomainModel object from extracted data
        news_summary_dm = NewsSummaryDomainModel(**data)
        
        return news_summary_dm
    except Exception as e:
        # Handle unexpected exceptions
        print(f"An unexpected error occurred: {e}")
        return None



app = FastAPI()   
@app.get('/summarize/')
async def summarize(request: GetNewsRequest) -> NewsSummaryDomainModel:
    response = scrape_news_article(request.url)
    return response

    
