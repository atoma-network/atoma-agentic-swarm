import os

from crewai import LLM, Agent, Task
from crewai.project import CrewBase, agent, task
from crewai_tools import ScrapeWebsiteTool
from utils import get_github_tool, pdf_tee_paper_search_tool, pdf_whitepaper_search_tool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


def get_llm() -> LLM:
    return LLM(
        model=os.getenv("LLM_MODEL"),
        base_url=os.getenv("LLM_BASE_URL"),
        api_key=os.getenv("LLM_API_KEY"),
    )


@CrewBase
class AtomaAgenticWorkflows:
    """A CrewAI workflow implementation for Atoma's agent-based tasks.

    This crew orchestrates multiple specialized agents to perform research and reporting
    tasks across different domains including AI, cryptography, trusted hardware, and
    blockchain technologies.

    Attributes:
        agents_config (str): Path to the YAML configuration file for agent definitions
        tasks_config (str): Path to the YAML configuration file for task definitions
    """

    @agent
    def researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["researcher"],
            verbose=True,
            llm=get_llm(),
            tools=[
                get_github_tool(),
                pdf_whitepaper_search_tool(),
                pdf_tee_paper_search_tool(),
                ScrapeWebsiteTool(website_url="https://www.atoma.network"),
            ],
        )

    @task
    def research_task(self) -> Task:
        return Task(
            agent=self.researcher(),
            task=self.task_config["research_task"],
        )

    @agent
    def report_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["report_agent"],
            verbose=True,
            llm=get_llm(),
        )

    @task
    def report_task(self) -> Task:
        return Task(
            agent=self.report_agent(),
            task=self.task_config["report_task"],
        )

    @agent
    def content_generation_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["content_generation_agent"],
            verbose=True,
            llm=get_llm(),
            memory=False,
        )

    @task
    def content_generation_task(self) -> Task:
        return Task(
            agent=self.content_generation_agent(),
            task=self.task_config["content_generation_task"],
        )
