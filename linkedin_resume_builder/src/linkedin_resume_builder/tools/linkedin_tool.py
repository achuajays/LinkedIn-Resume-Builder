from crewai.tools import BaseTool
from pydantic import BaseModel, Field
import requests
import os
from typing import Type

class LinkedInProfileInput(BaseModel):
    """Input schema for LinkedIn Profile Tool."""
    url: str = Field(..., description="LinkedIn profile URL to fetch data from")

class LinkedInProfileTool(BaseTool):
    name: str = "LinkedIn Profile Data Fetcher"
    description: str = "A tool that fetches profile data from LinkedIn using a profile URL"

    args_schema: Type[BaseModel] = LinkedInProfileInput

    def _run(self, url: str) -> str:
        """Fetch LinkedIn profile data"""
        api_url = "https://linkedin-data-api.p.rapidapi.com/get-profile-data-by-url"

        querystring = {"url": url}

        headers = {
            "x-rapidapi-key": os.environ["RAPIDAPI_KEY"],  # In a real implementation, you would want to secure this
            "x-rapidapi-host": "linkedin-data-api.p.rapidapi.com"
        }

        try:
            response = requests.get(api_url, headers=headers, params=querystring)
            response.raise_for_status()  # Raises an HTTPError for bad responses
            return str(response.json())
        except requests.exceptions.RequestException as e:
            return f"Error fetching LinkedIn data: {str(e)}"
