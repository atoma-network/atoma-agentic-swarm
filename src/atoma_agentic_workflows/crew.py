from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task

# If you want to run a snippet of code before or after the crew starts, 
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class AtomaAgenticWorkflows():
	"""A CrewAI workflow implementation for Atoma's agent-based tasks.
    
    This crew orchestrates multiple specialized agents to perform research and reporting
    tasks across different domains including AI, cryptography, trusted hardware, and
    blockchain technologies.

    Attributes:
        agents_config (str): Path to the YAML configuration file for agent definitions
        tasks_config (str): Path to the YAML configuration file for task definitions
    """

	# Learn more about YAML configuration files here:
	# Agents: https://docs.crewai.com/concepts/agents#yaml-configuration-recommended
	# Tasks: https://docs.crewai.com/concepts/tasks#yaml-configuration-recommended
	agents_config = 'config/agents.yaml'
	tasks_config = 'config/tasks.yaml'

	# If you would like to add tools to your agents, you can learn more about it here:
	# https://docs.crewai.com/concepts/agents#agent-tools
	@agent
	def ai_researcher(self) -> Agent:
		"""Creates an AI research specialist agent.
        
        Returns:
			Agent: An agent configured to conduct AI-focused research
		"""	
		return Agent(
			config=self.agents_config['ai_researcher'],
			verbose=True
		)

	@agent
	def ai_reporting_analyst(self) -> Agent:
		"""Creates an AI reporting analyst agent.
        
        This agent specializes in analyzing and creating reports based on
        AI research findings.

        Returns:
			Agent: An agent configured for AI research analysis and reporting
		"""
		return Agent(
			config=self.agents_config['ai_reporting_analyst'],
			verbose=True
		)

	@agent
	def cryptography_researcher(self) -> Agent:
		"""Creates a cryptography researcher agent.
        
        Returns:
			Agent: An agent configured for cryptography research
		"""
		return Agent(
			config=self.agents_config['cryptography_researcher'],
			verbose=True
		)
	
	@agent
	def cryptography_reporting_analyst(self) -> Agent:
		"""Creates a cryptography reporting analyst agent.
        
        Returns:
			Agent: An agent configured for cryptography reporting analysis
		"""
		return Agent(
			config=self.agents_config['cryptography_reporting_analyst'],
			verbose=True
		)
	
	@agent
	def trusted_hardware_researcher(self) -> Agent:
		"""Creates a trusted hardware researcher agent.
        
        Returns:
			Agent: An agent configured for trusted hardware research
		"""
		return Agent(
			config=self.agents_config['trusted_hardware_researcher'],
			verbose=True
		)

	@agent
	def trusted_hardware_reporting_analyst(self) -> Agent:
		"""Creates a trusted hardware reporting analyst agent.
        
        Returns:
			Agent: An agent configured for trusted hardware reporting analysis
		"""
		return Agent(
			config=self.agents_config['trusted_hardware_reporting_analyst'],
			verbose=True
		)
	
	@agent
	def blockchain_researcher(self) -> Agent:
		"""Creates a blockchain researcher agent.
        
        Returns:
			Agent: An agent configured for blockchain research
		"""
		return Agent(
			config=self.agents_config['blockchain_researcher'],
			verbose=True
		)
	
	@agent
	def blockchain_reporting_analyst(self) -> Agent:
		"""Creates a blockchain reporting analyst agent.
        
        Returns:
			Agent: An agent configured for blockchain reporting analysis
		"""
		return Agent(
			config=self.agents_config['blockchain_reporting_analyst'],
			verbose=True
		)
	
	@agent
	def atoma_content_generation_promoter(self) -> Agent:
		"""Creates an Atoma content generation promoter agent.
        
        Returns:
			Agent: An agent configured for Atoma content generation promotion
		"""
		return Agent(
			config=self.agents_config['atoma_content_generation_promoter'],
			verbose=True
		)

	@agent
	def degen_community_manager(self) -> Agent:
		"""Creates a degen community manager agent.
        
        Returns:
			Agent: An agent configured for degen community management
		"""
		return Agent(
			config=self.agents_config['degen_community_manager'],
			verbose=True
		)
	
	@agent
	def discord_moderator(self) -> Agent:
		"""Creates a discord moderator agent.
        
        Returns:
			Agent: An agent configured for discord moderation
		"""
		return Agent(
			config=self.agents_config['discord_moderator'],
			verbose=True
		)
	
	# To learn more about structured task outputs, 
	# task dependencies, and task callbacks, check out the documentation:
	# https://docs.crewai.com/concepts/tasks#overview-of-a-task
	@task
	def ai_research_task(self) -> Task:
		"""Creates an AI research task.
        
        Returns:
			Task: A task configured for AI research
		"""
		return Task(
			config=self.tasks_config['ai_research_task'],
		)

	@task
	def ai_reporting_task(self) -> Task:
		"""Creates an AI reporting task.
        
        Returns:
			Task: A task configured for AI reporting
		"""
		return Task(
			config=self.tasks_config['ai_reporting_task'],
			output_file='report.md'
		)
	
	@task
	def cryptography_research_task(self) -> Task:
		"""Creates a cryptography research task.
        
        Returns:
			Task: A task configured for cryptography research
		"""
		return Task(
			config=self.tasks_config['cryptography_research_task'],
		)
	
	@task
	def cryptography_reporting_task(self) -> Task:
		"""Creates a cryptography reporting task.
        
        Returns:
			Task: A task configured for cryptography reporting
		"""
		return Task(
			config=self.tasks_config['cryptography_reporting_task'],
			output_file='report.md'
		)
	
	@task
	def trusted_hardware_research_task(self) -> Task:
		"""Creates a trusted hardware research task.
        
        Returns:
			Task: A task configured for trusted hardware research
		"""
		return Task(
			config=self.tasks_config['trusted_hardware_research_task'],
		)
	
	@task
	def trusted_hardware_reporting_task(self) -> Task:
		"""Creates a trusted hardware reporting task.
        
        Returns:
			Task: A task configured for trusted hardware reporting
		"""
		return Task(
			config=self.tasks_config['trusted_hardware_reporting_task'],
			output_file='report.md'
		)
	
	@task
	def blockchain_research_task(self) -> Task:
		"""Creates a blockchain research task.
        
        Returns:
			Task: A task configured for blockchain research
		"""
		return Task(
			config=self.tasks_config['blockchain_research_task'],
		)
	
	@task
	def blockchain_reporting_task(self) -> Task:
		"""Creates a blockchain reporting task.
        
        Returns:
			Task: A task configured for blockchain reporting
		"""
		return Task(
			config=self.tasks_config['blockchain_reporting_task'],
			output_file='report.md'
		)
	
	@task
	def atoma_report_tweet_task(self) -> Task:
		"""Creates an Atoma report tweet task.
        
        Returns:
			Task: A task configured for Atoma report tweet
		"""
		return Task(
			config=self.tasks_config['atoma_report_tweet_task'],
		)
	
	@task
	def atoma_community_tweet_task(self) -> Task:
		"""Creates an Atoma community tweet task.
        
        Returns:
			Task: A task configured for Atoma community tweet
		"""
		return Task(
			config=self.tasks_config['atoma_community_tweet_task'],
		)
	
	@task
	def atoma_research_tweet_task(self) -> Task:
		"""Creates an Atoma research tweet task.
        
        Returns:
			Task: A task configured for Atoma research tweet
		"""
		return Task(
			config=self.tasks_config['atoma_research_tweet_task'],
		)
	
	@task
	def atoma_announcement_tweet_task(self) -> Task:
		"""Creates an Atoma announcement tweet task.
        
        Returns:
			Task: A task configured for Atoma announcement tweet
		"""
		return Task(
			config=self.tasks_config['atoma_announcement_tweet_task'],
		)

	@crew
	def crew(self) -> Crew:
		"""Creates the AtomaAgenticWorkflows crew"""
		# To learn how to add knowledge sources to your crew, check out the documentation:
		# https://docs.crewai.com/concepts/knowledge#what-is-knowledge

		return Crew(
			agents=self.agents, # Automatically created by the @agent decorator
			tasks=self.tasks, # Automatically created by the @task decorator
			process=Process.sequential,
			verbose=True,
			# process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
		)
