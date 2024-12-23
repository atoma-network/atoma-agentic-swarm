import os

from crewai import LLM, Agent
from crewai_tools import GithubSearchTool, PDFSearchTool, RagTool, WebsiteSearchTool

# Constants for LLM configuration
TEMPERATURE = 0.5  # Controls randomness in LLM responses (0.0 = deterministic, 1.0 = maximum randomness)
TOP_P = 0.9  # Controls diversity of token selection during text generation (higher values = more diverse)


def get_github_tool() -> GithubSearchTool:
    tool = GithubSearchTool(
        github_repo=os.getenv("GITHUB_REPO"),
        gh_token=os.getenv("GITHUB_AUTH_ACCESS_TOKEN"),
        content_types=["code", "issue", "pr"],
    )
    return tool


def get_github_docs_tool() -> GithubSearchTool:
    tool = GithubSearchTool(
        github_repo=os.getenv("GITHUB_DOCS_REPO"),
        gh_token=os.getenv("GITHUB_AUTH_ACCESS_TOKEN"),
        content_types=["code"],
    )
    return tool


def pdf_whitepaper_search_tool() -> PDFSearchTool:
    tool = PDFSearchTool(
        pdf=os.getenv("WHITEPAPER_PDF_PATH"),
    )
    return tool


def pdf_tee_paper_search_tool() -> PDFSearchTool:
    tool = PDFSearchTool(
        pdf=os.getenv("TEE_PDF_PATH"),
    )
    return tool
