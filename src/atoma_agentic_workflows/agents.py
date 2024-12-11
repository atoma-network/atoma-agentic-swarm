import os

from crewai import Agent
from crewai_tools import GithubSearchTool, PDFSearchTool, RagTool, WebsiteSearchTool
from dotenv import load_dotenv


def load_env_vars():
    load_dotenv()
