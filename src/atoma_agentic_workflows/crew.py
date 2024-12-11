import os

from crewai import LLM, Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import ScrapeWebsiteTool
from utils import get_github_tool, pdf_tee_paper_search_tool, pdf_whitepaper_search_tool

# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators


def get_llm() -> LLM:
    return LLM(
        model="gpt-4o",
        api_key=os.getenv("OPENAI_API_KEY"),
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

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    @agent
    def researcher(self) -> Agent:
        """
        Create the researcher agent.
        """
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
        """
        Create the research task.
        """
        research_task_config = self.tasks_config["research_task"]
        return Task(
            agent=self.researcher(),
            description=research_task_config["description"],
            expected_output=research_task_config["expected_output"],
        )
    
    @agent
    def report_agent(self) -> Agent:
        """
        Create the report agent.
        """
        return Agent(
            config=self.agents_config["report_agent"],
            verbose=True,
            llm=get_llm(),
        )

    @task
    def report_task(self) -> Task:
        """
        Create the report task.
        """
        report_task_config = self.tasks_config["reporting_task"]
        return Task(
            agent=self.report_agent(),
            description=report_task_config["description"],
            expected_output=report_task_config["expected_output"],
        )

    @agent
    def content_generation_agent(self) -> Agent:
        """
        Create the content generation agent.
        """
        return Agent(
            config=self.agents_config["content_generation_agent"],
            verbose=True,
            llm=get_llm(),
        )

    @task
    def content_generation_task(self) -> Task:
        """
        Create the content generation task.
        """
        content_generation_task_config = self.tasks_config["atoma_community_tweet_task"]
        return Task(
            agent=self.content_generation_agent(),
            description=content_generation_task_config["description"],
            expected_output=content_generation_task_config["expected_output"],
        )

    @crew
    def crew(self):
        """
        Create the crew with the agents and tasks.
        """
        return Crew(
            agents=[
                self.researcher(),
                self.report_agent(),
                self.content_generation_agent(),
            ],
            tasks=[
                self.research_task(),
                self.report_task(),
                self.content_generation_task(),
            ],
            process=Process.sequential,
            verbose=True,
        )
